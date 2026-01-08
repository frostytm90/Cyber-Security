#!/usr/bin/env python3
"""
Security Log Analyzer

A Python script for parsing and monitoring authentication logs to detect
security events including failed login attempts, privilege escalations,
and potential brute-force attacks.

Author: Security Analyst
Version: 1.0
"""

import re
from datetime import datetime
import os
import sys
import argparse
import json

# Regular expressions for parsing auth.log
command_regex = r"^(\S+)\s+(\d+)\s+(\d{2}:\d{2}:\d{2})\s+server\s+sudo\[(\d+)\]:\s+(\S+)\s+:\s+TTY=pts/\d+\s+;\s+PWD=\S+\s+;\s+USER=\S+\s+;\s+COMMAND=(.+)$"
user_regex = r"^(\S+)\s+(\d+)\s+(\d{2}:\d{2}:\d{2})\s+server\s+(useradd|userdel|passwd|su|sudo)\[(\d+)\]:\s+(.*)$"
sudo_command_regex = r"^(\S+)\s+(\d+)\s+(\d{2}:\d{2}:\d{2})\s+server\s+sudo\[(\d+)\]:\s+(\S+)\s+:\s+TTY=pts/\d+\s+;\s+PWD=\S+\s+;\s+USER=root\s+;\s+COMMAND=(.+)$"
sudo_failure_regex = r"^(\S+)\s+(\d+)\s+(\d{2}:\d{2}:\d{2})\s+server\s+sudo\[(\d+)\]:\s+pam_unix\(sudo:auth\):\s+authentication\s+failure;\s+logname=\S+\s+uid=\d+\s+euid=\d+\s+tty=\S+\s+ruser=\S*\s+rhost=\S+\s+user=(\S+)$"
hydra_attack_regex = r"^(\S+)\s+(\d+)\s+(\d{2}:\d{2}:\d{2})\s+server\s+sshd\[(\d+)\]:\s+(Failed|Accepted)\s+password\s+for\s+(\S+)\s+from\s+(\S+)\s+port\s+(\d+)\s+ssh2$"

class LogAnalyzer:
    """
    Main class for analyzing security logs
    """
    
    def __init__(self, log_file_path, output_file_path, year=None):
        """
        Initialize the LogAnalyzer
        
        Args:
            log_file_path (str): Path to the input log file
            output_file_path (str): Path to the output file
            year (int): Year for log entries (defaults to current year)
        """
        self.log_file_path = log_file_path
        self.output_file_path = output_file_path
        self.current_year = year or datetime.now().year
        self.log_entries = []
        self.statistics = {
            'total_entries': 0,
            'commands': 0,
            'user_changes': 0,
            'sudo_commands': 0,
            'failed_sudo': 0,
            'failed_logins': 0,
            'successful_logins': 0,
            'potential_attacks': 0
        }
        
    def parse_line(self, line):
        """
        Parse a single log line and extract relevant information
        
        Args:
            line (str): Log line to parse
            
        Returns:
            tuple: (timestamp, formatted_entry) or None if no match
        """
        # Parse command usage
        match = re.match(command_regex, line)
        if match:
            timestamp_str = f"{self.current_year} {match.group(1)} {match.group(2)} {match.group(3)}"
            try:
                timestamp = datetime.strptime(timestamp_str, '%Y %b %d %H:%M:%S')
            except ValueError:
                return None
            user = match.group(5)
            command = match.group(6)
            self.statistics['commands'] += 1
            return (timestamp, f"Command Log - Timestamp: {timestamp}, User: {user}, Command: {command}\n")
        
        # Monitor user authentication changes
        match = re.match(user_regex, line)
        if match:
            timestamp_str = f"{self.current_year} {match.group(1)} {match.group(2)} {match.group(3)}"
            try:
                timestamp = datetime.strptime(timestamp_str, '%Y %b %d %H:%M:%S')
            except ValueError:
                return None
            event = match.group(4)
            details = match.group(6)
            self.statistics['user_changes'] += 1
            
            if event == "useradd":
                return (timestamp, f"User Add - Timestamp: {timestamp}, New user added: {details}\n")
            elif event == "userdel":
                return (timestamp, f"User Delete - Timestamp: {timestamp}, User removed: {details}\n")
            elif event == "passwd":
                return (timestamp, f"Password Change - Timestamp: {timestamp}, Password changed: {details}\n")
            elif event == "sudo":
                self.statistics['sudo_commands'] += 1
                return (timestamp, f"ALERT!!!! sudo Command - Timestamp: {timestamp}, User used sudo command: {details}\n")
        
        # Monitor sudo command usage
        match = re.match(sudo_command_regex, line)
        if match:
            timestamp_str = f"{self.current_year} {match.group(1)} {match.group(2)} {match.group(3)}"
            try:
                timestamp = datetime.strptime(timestamp_str, '%Y %b %d %H:%M:%S')
            except ValueError:
                return None
            user = match.group(5)
            command = match.group(6)
            self.statistics['sudo_commands'] += 1
            return (timestamp, f"sudo Command - Timestamp: {timestamp}, User: {user}, Command: {command}\n")
        
        # Monitor failed sudo attempts
        match = re.match(sudo_failure_regex, line)
        if match:
            timestamp_str = f"{self.current_year} {match.group(1)} {match.group(2)} {match.group(3)}"
            try:
                timestamp = datetime.strptime(timestamp_str, '%Y %b %d %H:%M:%S')
            except ValueError:
                return None
            user = match.group(5)
            self.statistics['failed_sudo'] += 1
            self.statistics['potential_attacks'] += 1
            return (timestamp, f"ALERT! Failed sudo - Timestamp: {timestamp}, User: {user}, Command: sudo command failed\n")
        
        # Monitor Hydra attack logs
        match = re.match(hydra_attack_regex, line)
        if match:
            timestamp_str = f"{self.current_year} {match.group(1)} {match.group(2)} {match.group(3)}"
            try:
                timestamp = datetime.strptime(timestamp_str, '%Y %b %d %H:%M:%S')
            except ValueError:
                return None
            status = match.group(5)
            target_user = match.group(6)
            ip_address = match.group(7)
            port = match.group(8)
            
            if status == "Failed":
                self.statistics['failed_logins'] += 1
                self.statistics['potential_attacks'] += 1
                return (timestamp, f"Hydra Attack - Failed login attempt - Timestamp: {timestamp}, User: {target_user}, IP: {self.sanitize_ip(ip_address)}, Port: {port}\n")
            elif status == "Accepted":
                self.statistics['successful_logins'] += 1
                return (timestamp, f"Hydra Attack - Successful login - Timestamp: {timestamp}, User: {target_user}, IP: {self.sanitize_ip(ip_address)}, Port: {port}\n")
        
        return None
    
    def sanitize_ip(self, ip):
        """
        Sanitize IP addresses for privacy
        
        Args:
            ip (str): IP address to sanitize
            
        Returns:
            str: Sanitized IP address
        """
        # For demonstration purposes, partially mask the IP
        parts = ip.split('.')
        if len(parts) == 4:
            return f"{parts[0]}.{parts[1]}.XXX.XXX"
        return "XXX.XXX.XXX.XXX"
    
    def analyze(self):
        """
        Main analysis function that processes the log file
        """
        print(f"[+] Starting log analysis...")
        print(f"[+] Reading from: {self.log_file_path}")
        
        # Check if input file exists
        if not os.path.exists(self.log_file_path):
            print(f"[-] Error: Input file '{self.log_file_path}' not found!")
            return False
        
        # Process log file
        try:
            with open(self.log_file_path, 'r') as infile:
                for line_num, line in enumerate(infile, 1):
                    entry = self.parse_line(line.strip())
                    if entry:
                        self.log_entries.append(entry)
                        self.statistics['total_entries'] += 1
                    
                    # Progress indicator
                    if line_num % 1000 == 0:
                        print(f"[*] Processed {line_num} lines...")
        
        except Exception as e:
            print(f"[-] Error reading log file: {str(e)}")
            return False
        
        print(f"[+] Finished processing {self.statistics['total_entries']} relevant entries")
        
        # Sort entries by timestamp
        print(f"[+] Sorting entries chronologically...")
        self.log_entries.sort(key=lambda x: x[0])
        
        # Write output
        print(f"[+] Writing results to: {self.output_file_path}")
        try:
            with open(self.output_file_path, 'w') as outfile:
                # Write header
                outfile.write("="*60 + "\n")
                outfile.write("Security Log Analysis Report\n")
                outfile.write(f"Generated: {datetime.now()}\n")
                outfile.write("="*60 + "\n\n")
                
                # Write statistics
                outfile.write("=== Statistics ===\n")
                for key, value in self.statistics.items():
                    outfile.write(f"{key.replace('_', ' ').title()}: {value}\n")
                outfile.write("\n" + "="*60 + "\n\n")
                
                # Write log entries
                outfile.write("=== Parsed Log Entries ===\n\n")
                for entry in self.log_entries:
                    outfile.write(entry[1])
        
        except Exception as e:
            print(f"[-] Error writing output file: {str(e)}")
            return False
        
        print(f"[+] Analysis complete!")
        self.print_summary()
        return True
    
    def print_summary(self):
        """
        Print analysis summary to console
        """
        print("\n" + "="*60)
        print("ANALYSIS SUMMARY")
        print("="*60)
        print(f"Total Relevant Entries: {self.statistics['total_entries']}")
        print(f"Commands Executed: {self.statistics['commands']}")
        print(f"User Account Changes: {self.statistics['user_changes']}")
        print(f"Sudo Commands: {self.statistics['sudo_commands']}")
        print(f"Failed Sudo Attempts: {self.statistics['failed_sudo']}")
        print(f"Failed Login Attempts: {self.statistics['failed_logins']}")
        print(f"Successful Logins: {self.statistics['successful_logins']}")
        print(f"Potential Security Threats: {self.statistics['potential_attacks']}")
        print("="*60)

def main():
    """
    Main entry point for the script
    """
    parser = argparse.ArgumentParser(
        description='Analyze authentication logs for security events',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python log_analyzer.py -i auth.log -o parsed_logs.txt
  python log_analyzer.py -i /var/log/auth.log -o /tmp/analysis.txt -y 2024
        """)
    
    parser.add_argument('-i', '--input', 
                       default='simulated_auth.log',
                       help='Input log file path (default: simulated_auth.log)')
    parser.add_argument('-o', '--output',
                       default='parsed_logs.txt',
                       help='Output file path (default: parsed_logs.txt)')
    parser.add_argument('-y', '--year',
                       type=int,
                       default=datetime.now().year,
                       help='Year for log entries (default: current year)')
    
    args = parser.parse_args()
    
    # Create analyzer instance
    analyzer = LogAnalyzer(args.input, args.output, args.year)
    
    # Run analysis
    success = analyzer.analyze()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
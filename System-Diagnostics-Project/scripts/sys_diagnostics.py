#!/usr/bin/env python3

"""
System Diagnostics and Information Extractor
Cross-platform Python implementation
"""

import subprocess
import platform
import socket
import psutil
import requests
import os
import re
from datetime import datetime
from pathlib import Path

class SystemDiagnostics:
    def __init__(self):
        self.system = platform.system()
        self.separator = "-" * 30
        
    def print_separator(self):
        """Print visual separator"""
        print(self.separator)
    
    def get_public_ip(self):
        """Get public IP address"""
        try:
            response = requests.get('https://ifconfig.io', timeout=5)
            public_ip = response.text.strip()
            return public_ip
        except Exception as e:
            return f"Unable to fetch: {e}"
    
    def get_private_ip(self):
        """Get private IP address"""
        try:
            hostname = socket.gethostname()
            private_ip = socket.gethostbyname(hostname)
            # Filter out loopback
            if private_ip.startswith("127."):
                # Try to get actual private IP
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))
                private_ip = s.getsockname()[0]
                s.close()
            return private_ip
        except Exception as e:
            return f"Unable to fetch: {e}"
    
    def get_mac_address(self):
        """Get MAC address with privacy masking"""
        try:
            import uuid
            mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
            # Mask middle portions for privacy
            mac_parts = mac.split(':')
            if len(mac_parts) == 6:
                masked_mac = f"{mac_parts[0]}:XX:XX:{mac_parts[3]}:{mac_parts[4]}:{mac_parts[5]}"
                return masked_mac
            return mac
        except Exception as e:
            return f"Unable to fetch: {e}"
    
    def get_cpu_processes(self):
        """Get top 5 CPU consuming processes"""
        try:
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'username']):
                try:
                    processes.append(proc.info)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            
            # Sort by CPU usage
            processes.sort(key=lambda x: x.get('cpu_percent', 0), reverse=True)
            return processes[:5]
        except Exception as e:
            return []
    
    def get_memory_usage(self):
        """Get memory usage statistics"""
        try:
            mem = psutil.virtual_memory()
            swap = psutil.swap_memory()
            
            return {
                'total': self.bytes_to_human(mem.total),
                'used': self.bytes_to_human(mem.used),
                'free': self.bytes_to_human(mem.free),
                'available': self.bytes_to_human(mem.available),
                'percent': mem.percent,
                'swap_total': self.bytes_to_human(swap.total),
                'swap_used': self.bytes_to_human(swap.used),
                'swap_free': self.bytes_to_human(swap.free)
            }
        except Exception as e:
            return {}
    
    def get_active_services(self):
        """Get active system services (Linux specific)"""
        if self.system != "Linux":
            return "Service listing is only available on Linux systems"
        
        try:
            result = subprocess.run(
                ['systemctl', 'list-units', '--type=service', '--state=active', '--no-pager'],
                capture_output=True,
                text=True,
                check=False
            )
            return result.stdout
        except Exception as e:
            return f"Unable to fetch services: {e}"
    
    def get_largest_files(self, directory=None):
        """Get top 10 largest files in directory"""
        if directory is None:
            directory = Path.home()
        else:
            directory = Path(directory)
        
        try:
            files = []
            for path in directory.rglob('*'):
                if path.is_file():
                    try:
                        size = path.stat().st_size
                        files.append((path, size))
                    except (PermissionError, OSError):
                        continue
            
            # Sort by size
            files.sort(key=lambda x: x[1], reverse=True)
            
            # Return top 10
            return [(str(f[0]), self.bytes_to_human(f[1])) for f in files[:10]]
        except Exception as e:
            return []
    
    def bytes_to_human(self, bytes_value):
        """Convert bytes to human readable format"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_value < 1024.0:
                return f"{bytes_value:.1f}{unit}"
            bytes_value /= 1024.0
        return f"{bytes_value:.1f}PB"
    
    def run_diagnostics(self):
        """Run all diagnostics and display results"""
        print("\n" + "="*50)
        print("   SYSTEM DIAGNOSTICS REPORT")
        print("="*50)
        print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"System: {self.system} - {platform.release()}")
        
        # Public IP
        self.print_separator()
        print("PUBLIC IP ADDRESS:")
        public_ip = self.get_public_ip()
        print(f"Your External/Public IP Address is: {public_ip}")
        
        # Private IP
        self.print_separator()
        print("PRIVATE IP ADDRESS:")
        private_ip = self.get_private_ip()
        print(f"Your Internal/Private IP Address is: {private_ip}")
        
        # MAC Address
        self.print_separator()
        print("MAC ADDRESS:")
        mac = self.get_mac_address()
        print(f"Your MAC Address is: {mac}")
        
        # CPU Processes
        self.print_separator()
        print("TOP 5 CPU PROCESSES:")
        processes = self.get_cpu_processes()
        if processes:
            print(f"{'PID':<10} {'USER':<15} {'CPU%':<10} {'MEM%':<10} {'NAME':<30}")
            print("-" * 75)
            for proc in processes:
                pid = proc.get('pid', 'N/A')
                user = proc.get('username', 'N/A')[:15]
                cpu = proc.get('cpu_percent', 0)
                mem = proc.get('memory_percent', 0)
                name = proc.get('name', 'N/A')[:30]
                print(f"{pid:<10} {user:<15} {cpu:<10.1f} {mem:<10.1f} {name:<30}")
        
        # Memory Usage
        self.print_separator()
        print("MEMORY USAGE:")
        mem_info = self.get_memory_usage()
        if mem_info:
            print(f"Total: {mem_info['total']}")
            print(f"Used: {mem_info['used']} ({mem_info['percent']:.1f}%)")
            print(f"Free: {mem_info['free']}")
            print(f"Available: {mem_info['available']}")
            print(f"\nSwap Total: {mem_info['swap_total']}")
            print(f"Swap Used: {mem_info['swap_used']}")
            print(f"Swap Free: {mem_info['swap_free']}")
        
        # Active Services (Linux only)
        if self.system == "Linux":
            self.print_separator()
            print("ACTIVE SERVICES:")
            services = self.get_active_services()
            if isinstance(services, str) and len(services) > 0:
                # Limit output to first 20 lines for brevity
                lines = services.split('\n')[:20]
                for line in lines:
                    print(line)
                if len(services.split('\n')) > 20:
                    print(f"... and {len(services.split('\n')) - 20} more services")
        
        # Largest Files
        self.print_separator()
        print("TOP 10 LARGEST FILES IN HOME DIRECTORY:")
        large_files = self.get_largest_files()
        if large_files:
            for i, (filepath, size) in enumerate(large_files, 1):
                # Truncate long paths for display
                display_path = filepath
                if len(filepath) > 60:
                    display_path = "..." + filepath[-57:]
                print(f"{i:2}. {size:>10} - {display_path}")
        
        self.print_separator()
        print("\nDiagnostics complete!")

def main():
    """Main entry point"""
    try:
        # Check for required modules
        required_modules = ['psutil', 'requests']
        missing_modules = []
        
        for module in required_modules:
            try:
                __import__(module)
            except ImportError:
                missing_modules.append(module)
        
        if missing_modules:
            print("Missing required modules. Please install:")
            for module in missing_modules:
                print(f"  pip install {module}")
            return
        
        # Run diagnostics
        diag = SystemDiagnostics()
        diag.run_diagnostics()
        
    except KeyboardInterrupt:
        print("\n\nDiagnostics interrupted by user.")
    except Exception as e:
        print(f"Error running diagnostics: {e}")

if __name__ == "__main__":
    main()
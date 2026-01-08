# System Diagnostics and Information Extractor

## Objective

This project presents a comprehensive bash shell script designed to analyze and extract critical information from a computer system's network infrastructure. The purpose is to evaluate the system's connectivity, performance, and resource utilization by gathering data about public/private IP addresses, MAC addresses, CPU usage, memory usage, active system services, and file storage patterns.

The goal is to provide system administrators and security professionals with a quick snapshot of the system's current state and offer insights for optimization and security enhancement.

## Skills Learned

### Network Analysis and Configuration
- Retrieving and differentiating between public and private IP addresses
- Understanding MAC address structure and privacy implications
- Working with network interfaces using Linux networking tools

### System Resource Monitoring
- Analyzing CPU usage and identifying resource-intensive processes
- Monitoring memory utilization and understanding memory metrics
- Evaluating system performance indicators

### Process Management
- Using process monitoring commands (`ps`, `aux`)
- Sorting and filtering processes by resource consumption
- Understanding process priorities and system load

### Service Management
- Working with systemd and systemctl commands
- Identifying and analyzing active system services
- Understanding service states and dependencies

### File System Analysis
- Locating and analyzing large files in the system
- Using find and du commands for disk usage analysis
- Implementing efficient file searching techniques

### Shell Scripting Proficiency
- Writing modular bash scripts with functions
- Implementing proper error handling and output formatting
- Using command substitution and variable assignment
- Creating user-friendly output with visual separators

### Command-Line Tool Mastery
- Proficiency with curl for network requests
- Advanced usage of grep with regular expressions
- Utilizing awk for text processing and data extraction
- Combining multiple commands with pipes

### Security and Privacy Awareness
- Implementing MAC address masking for privacy
- Understanding security implications of exposed system information
- Following best practices for sensitive data handling

### Documentation Skills
- Creating comprehensive technical reports
- Explaining complex commands and their flags
- Providing clear code explanations with examples

## Tools Used

1. **curl** - Fetching external IP address from web services
2. **ip** - Managing and displaying network interface information
3. **grep** - Pattern matching and text filtering with regular expressions
4. **awk** - Text processing and data extraction
5. **ps** - Process status and monitoring
6. **free** - Memory usage statistics
7. **systemctl** - System service management
8. **find** - File system searching
9. **du** - Disk usage calculation
10. **sort** - Data sorting with human-readable units
11. **head** - Limiting output to specified lines

## Methodologies

### Network Information Gathering

#### Public IP Address Retrieval
* **Method**: Using curl to fetch the public-facing IP address from an external service
* **Command**: `curl -s ifconfig.io`
* **Purpose**: Identifies the system's internet-facing address for external communication

#### Private IP Address Extraction
* **Method**: Parsing network interface data to extract local network addresses
* **Command**: `ip addr show | grep -Eo 'inet [0-9.]+' | grep -v '127.0.0.1'`
* **Purpose**: Identifies internal network addressing for local communication

#### MAC Address Retrieval with Privacy Masking
* **Method**: Extracting MAC address and masking sensitive portions
* **Command**: Complex awk processing to mask middle octets
* **Purpose**: Maintains privacy while providing network interface identification

### System Resource Analysis

#### CPU Usage Monitoring
* **Method**: Listing processes sorted by CPU consumption
* **Command**: `ps aux --sort=%cpu | head -n 6`
* **Purpose**: Identifies resource-intensive processes affecting system performance

#### Memory Usage Assessment
* **Method**: Displaying memory statistics in human-readable format
* **Command**: `free -h`
* **Purpose**: Evaluates available memory and potential bottlenecks

### Service and File System Analysis

#### Active Service Enumeration
* **Method**: Querying systemd for active services
* **Command**: `systemctl list-units --type=service --state=active`
* **Purpose**: Identifies running services for security and performance assessment

#### Large File Detection
* **Method**: Finding and sorting files by size in home directory
* **Command**: `find "$HOME" -type f -exec du -h {} + | sort -rh | head -n 10`
* **Purpose**: Identifies storage usage patterns and potential cleanup opportunities

## Implementation Details

### Script Structure

The script is organized into modular components:

1. **Shebang Declaration**: `#!/bin/bash` - Specifies the interpreter
2. **Helper Functions**: Visual separator for improved readability
3. **Network Information Module**: IP and MAC address extraction
4. **Resource Monitoring Module**: CPU and memory analysis
5. **Service Analysis Module**: Active service enumeration
6. **File System Module**: Large file identification

### Key Features

#### Visual Output Formatting
```bash
separator () {
    echo "---------- ---------- ----------"
}
```
Creates clear visual separation between different sections of output for enhanced readability.

#### Variable Storage
All retrieved information is stored in variables for potential reuse:
- `$public_ip` - External IP address
- `$private_ip` - Internal IP address  
- `$mac_add` - Masked MAC address

#### Privacy Protection
The MAC address is partially masked to protect sensitive information:
- Keeps first octet for vendor identification
- Masks second and third octets with "XX"
- Preserves last three octets for uniqueness

### Command Breakdown Examples

#### Public IP Retrieval
```bash
public_ip=$(curl -s ifconfig.io)
```
- `curl`: HTTP client for web requests
- `-s`: Silent mode (no progress output)
- `ifconfig.io`: Service returning public IP
- `$()`: Command substitution storing result

#### Private IP Extraction
```bash
private_ip=$(ip addr show | grep -Eo 'inet [0-9.]+' | grep -v '127.0.0.1' | awk '{print $2}')
```
- `ip addr show`: Display all network interfaces
- `grep -Eo 'inet [0-9.]+'`: Extract IPv4 addresses
- `grep -v '127.0.0.1'`: Exclude loopback
- `awk '{print $2}'`: Extract IP field

## Discussion

### System Analysis Findings

The script provides comprehensive system diagnostics covering:

1. **Network Connectivity**: Both public and private IP addresses confirm proper network configuration
2. **Resource Utilization**: Memory and CPU usage indicate system health
3. **Service Status**: Active services align with expected system configuration
4. **Storage Patterns**: File size analysis reveals usage patterns and potential optimization areas

### Security Considerations

- **MAC Address Privacy**: Partial masking protects against MAC spoofing attacks
- **Information Disclosure**: Output should be carefully managed to prevent sensitive data exposure
- **Access Control**: Script should be run with appropriate permissions

### Performance Insights

The script efficiently combines multiple tools using pipes, minimizing resource overhead while maximizing information gathering. The modular approach allows for easy customization and extension.

## Conclusion

This system diagnostics tool demonstrates proficiency in Linux system administration, network analysis, and security-aware programming. The script provides valuable insights into system health while maintaining privacy and security best practices.

### Key Achievements
- Automated system information gathering
- Privacy-conscious data handling
- User-friendly output formatting
- Comprehensive resource analysis
- Cross-platform compatibility (Linux/macOS)

### Practical Applications
- System health monitoring
- Security auditing
- Performance troubleshooting
- Network configuration verification
- Resource optimization planning

## Data Sanitization Best Practices

### Information Security Standards

This project implements industry-standard data sanitization techniques to protect sensitive information:

#### Network Information Sanitization
- **Public IP Addresses**: Replace with `[REDACTED]` or use RFC 5737 documentation addresses (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24)
- **Private IP Addresses**: Use RFC 1918 private ranges (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) with masked host portions
- **MAC Addresses**: Replace with generic patterns (AA:BB:CC:XX:XX:XX) or vendor-neutral addresses

#### System Information Protection
- **Usernames**: Replace with generic identifiers (user, admin, service_account)
- **Hostnames**: Use generic names (workstation01, server01, localhost)
- **File Paths**: Replace user-specific paths with generic equivalents (/home/user instead of actual usernames)
- **Process Names**: Keep system processes but sanitize custom application names

#### Best Practices Implementation
1. **Consistent Redaction**: Use `[REDACTED]` for completely sensitive data
2. **Partial Masking**: Use 'X' for partial masking (192.168.X.X)
3. **Generic Substitution**: Replace with realistic but non-sensitive alternatives
4. **Pattern Preservation**: Maintain data format while removing sensitive content

#### Sanitization Levels
- **Level 1 - Public Sharing**: Complete removal of all potentially identifying information
- **Level 2 - Internal Sharing**: Partial masking maintaining some context
- **Level 3 - Development/Testing**: Generic but realistic data substitution

## Recommendations

### Security Enhancements
- Implement automated sanitization functions in scripts
- Add configurable sanitization levels based on output destination
- Include pre-commit hooks to check for sensitive data
- Create sanitization validation tools
- Log all diagnostic activities with sanitized outputs

### Performance Optimizations
- Cache frequently accessed data
- Implement parallel processing for faster execution
- Add configurable output verbosity levels
- Include historical data comparison

### Feature Extensions
- Add JSON/XML output formats for automation
- Implement remote system diagnostics capability
- Include graphical output options
- Add automated alerting for anomalies

### Platform Compatibility

#### Linux Systems
- Native support on all major distributions
- No additional configuration required

#### macOS Systems  
- Compatible with minor command variations
- May require homebrew for some tools

#### Windows Systems (WSL)
- Requires Windows Subsystem for Linux installation:
  ```powershell
  wsl --install
  ```
- Choose preferred Linux distribution from Microsoft Store
- Execute script within WSL environment

## References

### Command Documentation
- [curl Documentation](https://developer.ibm.com/articles/what-is-curl-command/)
- [Linux ip Command Guide](https://www.linode.com/docs/guides/how-to-use-the-linux-ip-command/)
- [ps Command Examples](https://www.geeksforgeeks.org/ps-command-in-linux-with-examples/)
- [free Command Usage](https://www.geeksforgeeks.org/free-command-linux-examples/)
- [systemctl Command Guide](https://www.tecmint.com/list-all-running-services-under-systemd-in-linux/)
- [du Command Options](https://www.redhat.com/sysadmin/du-command-options/)
- [find Command Manual](https://man7.org/linux/man-pages/man1/find.1.html)
- [sort Command Reference](https://man7.org/linux/man-pages/man1/sort.1.html)

### Security Resources
- [MAC Address Spoofing](https://wiki.archlinux.org/title/MAC_address_spoofing)
- [Network Security Best Practices](https://en.wikipedia.org/wiki/MAC_spoofing)

### Additional Learning
- [The Art of Command Line](https://github.com/jlevy/the-art-of-command-line)
- [Linux System Administration](https://www.linode.com/docs/guides/)
- [Bash Scripting Guide](https://www.gnu.org/software/bash/manual/)
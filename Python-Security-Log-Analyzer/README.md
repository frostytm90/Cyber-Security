# Python Security Log Analyzer

## Project Overview

A comprehensive Python-based security log analyzer designed to parse and monitor authentication logs for detecting unauthorized access attempts, security breaches, and potential attacks. This project demonstrates proficiency in Python programming, regular expressions, log analysis, and security monitoring techniques.

## Objectives

- Parse and analyze authentication log files (auth.log) from Linux systems
- Detect and categorize security events including failed login attempts, privilege escalations, and brute-force attacks
- Generate detailed security reports with chronological event logging
- Provide statistical analysis of security events for threat assessment
- Implement data sanitization for privacy protection in logs

## Features

### Core Functionality
- **Multi-Pattern Log Parsing**: Utilizes regular expressions to identify various log entry types
- **Security Event Detection**: Identifies failed sudo attempts, unauthorized access, and attack patterns
- **Chronological Sorting**: Orders events by timestamp for timeline analysis
- **Statistical Analysis**: Generates metrics on security events and potential threats
- **Data Sanitization**: Protects sensitive information like IP addresses

### Supported Event Types
1. **Command Execution Monitoring**: Tracks sudo and regular command usage
2. **User Authentication Changes**: Monitors user additions, deletions, and password changes
3. **Failed Authentication Attempts**: Detects failed sudo and login attempts
4. **Brute-Force Attack Detection**: Identifies patterns consistent with Hydra and similar tools
5. **Privilege Escalation Attempts**: Flags suspicious privilege elevation activities

## Skills Demonstrated

### Python Programming
- **Object-Oriented Design**: Modular class-based architecture
- **Regular Expressions**: Complex pattern matching for log parsing
- **File I/O Operations**: Efficient processing of large log files
- **Error Handling**: Robust exception management
- **Command-Line Interface**: argparse for user-friendly CLI

### Security Analysis
- **Log Analysis**: Understanding of Linux authentication logs
- **Attack Pattern Recognition**: Identifying common attack vectors
- **Security Monitoring**: Proactive threat detection capabilities
- **Incident Response**: Chronological event reconstruction
- **Compliance Support**: Audit trail generation

### Software Engineering
- **Code Documentation**: Comprehensive docstrings and comments
- **Modular Design**: Reusable and maintainable code structure
- **Testing Framework**: Includes test data generator
- **Performance Optimization**: Efficient processing of large datasets

## Technical Implementation

### Architecture

```
LogAnalyzer Class
├── __init__(): Initialize analyzer with configuration
├── parse_line(): Parse individual log entries
├── sanitize_ip(): Privacy protection for IP addresses
├── analyze(): Main analysis workflow
└── print_summary(): Generate statistical reports
```

### Regular Expression Patterns

The analyzer uses sophisticated regex patterns to match:

1. **Command Execution**:
```python
r"^(\S+)\s+(\d+)\s+(\d{2}:\d{2}:\d{2})\s+server\s+sudo\[(\d+)\]..."
```

2. **User Management Events**:
```python
r"^(\S+)\s+(\d+)\s+(\d{2}:\d{2}:\d{2})\s+server\s+(useradd|userdel|passwd|su|sudo)..."
```

3. **Failed Authentication**:
```python
r"^(\S+)\s+(\d+)\s+(\d{2}:\d{2}:\d{2})\s+server\s+sudo\[(\d+)\]:.*authentication\s+failure..."
```

4. **Brute-Force Attempts**:
```python
r"^(\S+)\s+(\d+)\s+(\d{2}:\d{2}:\d{2})\s+server\s+sshd\[(\d+)\]:\s+(Failed|Accepted)..."
```

### Data Flow

1. **Input Processing**: Read auth.log file line by line
2. **Pattern Matching**: Apply regex patterns to identify event types
3. **Data Extraction**: Parse timestamps, users, commands, and IPs
4. **Event Categorization**: Classify events by security relevance
5. **Chronological Sorting**: Order events by timestamp
6. **Report Generation**: Create formatted output with statistics

## Installation and Usage

### Prerequisites
- Python 3.7 or higher
- Linux/Unix system (or WSL for Windows)
- Access to auth.log files or test data

### Setup
```bash
# Clone or download the project
cd Python-Security-Log-Analyzer

# Install dependencies (if any)
pip install -r requirements.txt
```

### Running the Analyzer

#### Basic Usage
```bash
python scripts/log_analyzer.py -i data/simulated_auth.log -o output/analysis_report.txt
```

#### Advanced Options
```bash
# Specify year for log entries
python scripts/log_analyzer.py -i /var/log/auth.log -o report.txt -y 2024

# Generate test data
python scripts/generate_test_logs.py -o test_logs.txt -n 10000
```

### Command-Line Arguments
- `-i, --input`: Input log file path (default: simulated_auth.log)
- `-o, --output`: Output report file path (default: parsed_logs.txt)
- `-y, --year`: Year for log entries (default: current year)

## Project Structure

```
Python-Security-Log-Analyzer/
├── README.md                              # This file
├── scripts/
│   ├── log_analyzer.py                   # Main analyzer script
│   ├── generate_test_logs.py             # Test data generator
│   ├── original_create_mock_auth.py      # Original mock data creator
│   └── original_project_script.py        # Original project script
├── docs/
│   ├── Python_Log_Analyzer_Report.pdf    # Detailed project report
│   └── LESSONS_LEARNED.md               # Key takeaways and insights
├── data/
│   └── simulated_auth.log               # Sample log data
├── output/
│   ├── parsed_logs.txt                  # Sample output
│   └── analysis_report.txt              # Analysis results
└── tools/
    └── requirements.txt                  # Python dependencies

```

## Sample Output

### Statistics Summary
```
===========================================================
ANALYSIS SUMMARY
===========================================================
Total Relevant Entries: 6666
Commands Executed: 123
User Account Changes: 456
Sudo Commands: 789
Failed Sudo Attempts: 15
Failed Login Attempts: 234
Successful Logins: 567
Potential Security Threats: 249
===========================================================
```

### Log Entry Examples
```
Command Log - Timestamp: 2024-01-15 14:23:45, User: alice, Command: apt update
ALERT! Failed sudo - Timestamp: 2024-02-20 03:15:22, User: unknown, Command: sudo command failed
Hydra Attack - Failed login attempt - Timestamp: 2024-02-25 18:45:33, User: admin, IP: 192.0.XXX.XXX, Port: 22
```

## Security Insights

### CIA Triad Application

#### Confidentiality
- Monitors unauthorized access attempts to protect sensitive data
- Detects credential compromise through failed login analysis
- Implements IP sanitization for privacy protection

#### Integrity
- Tracks system changes including user modifications
- Monitors privilege escalation attempts
- Maintains audit trail for compliance

#### Availability
- Identifies DoS attack patterns through log analysis
- Enables rapid incident response
- Supports system stability monitoring

## Key Learnings

### Technical Skills Acquired
1. **Regular Expression Mastery**: Complex pattern matching in Python
2. **Log Analysis Techniques**: Understanding system log formats and structures
3. **Security Event Correlation**: Connecting related events for threat detection
4. **Performance Optimization**: Efficient processing of large log files
5. **Data Privacy**: Implementing sanitization while maintaining utility

### Security Concepts
1. **Attack Pattern Recognition**: Identifying brute-force and exploitation attempts
2. **Incident Timeline Reconstruction**: Chronological event analysis
3. **Threat Hunting**: Proactive security monitoring techniques
4. **Compliance Support**: Audit trail generation for regulatory requirements

## Future Enhancements

### Planned Features
1. **Real-time Monitoring**: Integration with system log streams
2. **Machine Learning**: Anomaly detection using ML algorithms
3. **Dashboard Interface**: Web-based visualization of security metrics
4. **Alert System**: Email/SMS notifications for critical events
5. **Extended Log Support**: Parse additional log types (syslog, Apache, etc.)

### Performance Improvements
1. **Parallel Processing**: Multi-threaded log analysis
2. **Database Integration**: Store results for historical analysis
3. **Caching Mechanism**: Improve performance for repeated analyses
4. **Streaming Processing**: Handle continuous log streams

## Best Practices Implemented

### Code Quality
- **PEP 8 Compliance**: Following Python style guidelines
- **Type Hints**: Enhanced code readability and IDE support
- **Comprehensive Documentation**: Docstrings for all functions
- **Error Handling**: Graceful failure with informative messages

### Security Practices
- **Input Validation**: Sanitize user inputs and file paths
- **Data Privacy**: Mask sensitive information in outputs
- **Secure Defaults**: Conservative security settings
- **Audit Logging**: Track analyzer usage and results

## Testing

### Test Data Generation
The project includes a comprehensive test data generator that creates:
- Normal user activities
- Suspicious behavior patterns
- Attack simulations
- Edge cases for parser testing

### Running Tests
```bash
# Generate test data
python scripts/generate_test_logs.py -n 50000

# Run analyzer on test data
python scripts/log_analyzer.py -i simulated_auth.log -o test_results.txt

# Verify results
cat test_results.txt | grep "ALERT"
```

## Recommendations

### For System Administrators
1. Schedule regular log analysis (cron jobs)
2. Integrate with SIEM systems for centralized monitoring
3. Customize regex patterns for environment-specific logs
4. Set up alerting thresholds based on baseline activity

### For Security Teams
1. Correlate findings with other security tools
2. Use for incident response and forensics
3. Create custom patterns for emerging threats
4. Generate compliance reports for audits

## Conclusion

This Python Security Log Analyzer demonstrates comprehensive understanding of:
- Python programming and software engineering principles
- Security monitoring and threat detection techniques
- Log analysis and pattern recognition
- Data privacy and sanitization practices

The tool provides practical value for system administrators and security professionals while showcasing advanced Python development skills and security awareness.

## References

- [Python Regular Expression Documentation](https://docs.python.org/3/library/re.html)
- [Linux Log Files Guide](https://help.ubuntu.com/community/LinuxLogFiles)
- [NIST Guide to Computer Security Log Management](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-92.pdf)
- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

## License

This project is for educational and portfolio purposes. Please ensure compliance with applicable laws and regulations when analyzing system logs.

## Author

Security Analyst - Python Developer
Specializing in Security Automation and Log Analysis
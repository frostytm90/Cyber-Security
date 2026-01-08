#!/bin/bash

# Data Sanitization Script for System Diagnostics Output
# Implements best practices for information security

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to sanitize IP addresses
sanitize_ip() {
    local input="$1"
    local level="$2"
    
    case "$level" in
        "public")
            # Level 1: Complete redaction for public sharing
            echo "[REDACTED]"
            ;;
        "internal")
            # Level 2: Partial masking for internal use
            echo "$input" | sed -E 's/([0-9]{1,3}\.[0-9]{1,3}\.)[0-9]{1,3}\.[0-9]{1,3}/\1X.X/g'
            ;;
        "development")
            # Level 3: Replace with RFC 5737 documentation addresses
            echo "192.0.2.1"
            ;;
        *)
            echo "[SANITIZED]"
            ;;
    esac
}

# Function to sanitize MAC addresses
sanitize_mac() {
    local input="$1"
    local level="$2"
    
    case "$level" in
        "public")
            # Complete masking
            echo "AA:BB:CC:DD:EE:FF"
            ;;
        "internal")
            # Preserve vendor, mask device
            echo "$input" | sed -E 's/([0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}):.*/\1:XX:XX:XX/g'
            ;;
        "development")
            # Generic but valid MAC
            echo "02:00:00:00:00:01"
            ;;
        *)
            echo "XX:XX:XX:XX:XX:XX"
            ;;
    esac
}

# Function to sanitize usernames
sanitize_username() {
    local input="$1"
    
    # Replace common usernames with generic ones
    case "$input" in
        root)
            echo "root"
            ;;
        admin*)
            echo "admin"
            ;;
        *)
            echo "user"
            ;;
    esac
}

# Function to sanitize file paths
sanitize_filepath() {
    local input="$1"
    
    # Replace home directory paths
    echo "$input" | sed -E 's|/home/[^/]+|/home/user|g' | \
                    sed -E 's|/Users/[^/]+|/Users/user|g' | \
                    sed -E 's|C:\\Users\\[^\\]+|C:\\Users\\user|g'
}

# Function to sanitize hostnames
sanitize_hostname() {
    local input="$1"
    
    # Replace with generic hostname
    echo "workstation01"
}

# Main sanitization function
sanitize_output() {
    local input_file="$1"
    local output_file="$2"
    local level="${3:-public}"  # Default to public level
    
    if [ ! -f "$input_file" ]; then
        echo -e "${RED}Error: Input file not found${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}Starting sanitization process...${NC}"
    echo -e "${YELLOW}Sanitization level: $level${NC}"
    
    # Create temporary file
    temp_file=$(mktemp)
    
    # Copy original to temp
    cp "$input_file" "$temp_file"
    
    # Sanitize IP addresses
    echo "Sanitizing IP addresses..."
    # Match common IP patterns
    sed -i -E 's/\b([0-9]{1,3}\.){3}[0-9]{1,3}\b/[IP-REDACTED]/g' "$temp_file"
    
    # Sanitize MAC addresses
    echo "Sanitizing MAC addresses..."
    sed -i -E 's/([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}/AA:BB:CC:XX:XX:XX/g' "$temp_file"
    
    # Sanitize email addresses
    echo "Sanitizing email addresses..."
    sed -i -E 's/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/user@example.com/g' "$temp_file"
    
    # Sanitize common paths
    echo "Sanitizing file paths..."
    sed -i -E 's|/home/[^/[:space:]]+|/home/user|g' "$temp_file"
    sed -i -E 's|/Users/[^/[:space:]]+|/Users/user|g' "$temp_file"
    
    # Sanitize hostnames
    echo "Sanitizing hostnames..."
    sed -i -E 's/@[a-zA-Z0-9.-]+/@hostname/g' "$temp_file"
    
    # Remove potential passwords or keys
    echo "Removing potential secrets..."
    sed -i -E 's/(password|passwd|pwd|secret|token|key|api)[ ]*[=:][ ]*[^ ]+/\1=[REDACTED]/gi' "$temp_file"
    
    # Copy sanitized content to output
    mv "$temp_file" "$output_file"
    
    echo -e "${GREEN}Sanitization complete!${NC}"
    echo -e "Output saved to: $output_file"
    
    # Generate sanitization report
    echo -e "\n${YELLOW}Sanitization Report:${NC}"
    echo "- IP addresses: Replaced with [IP-REDACTED]"
    echo "- MAC addresses: Masked as AA:BB:CC:XX:XX:XX"
    echo "- Email addresses: Replaced with user@example.com"
    echo "- File paths: Genericized to /home/user"
    echo "- Potential secrets: Redacted"
}

# Script usage
usage() {
    echo "Usage: $0 <input_file> <output_file> [sanitization_level]"
    echo ""
    echo "Sanitization levels:"
    echo "  public      - Complete redaction (default)"
    echo "  internal    - Partial masking"
    echo "  development - Generic substitution"
    echo ""
    echo "Example:"
    echo "  $0 raw_output.txt sanitized_output.txt public"
    exit 1
}

# Main execution
if [ $# -lt 2 ]; then
    usage
fi

sanitize_output "$1" "$2" "${3:-public}"
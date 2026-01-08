# Network Research Tools - Setup Instructions

## Prerequisites

- Linux-based operating system (Ubuntu/Debian recommended)
- sudo privileges for package installation
- Internet connection for downloading tools
- Minimum 2GB RAM for smooth operation

## Tool Installation Guide

### 1. System Update
```bash
sudo apt-get update
sudo apt-get upgrade -y
```

### 2. Core Dependencies

#### Basic Tools
```bash
# Network utilities
sudo apt-get install -y curl wget git

# JSON processor
sudo apt-get install -y jq

# SSH automation
sudo apt-get install -y sshpass openssh-client
```

### 3. Nipe Installation

#### Prerequisites for Nipe
```bash
# Install Perl and CPAN
sudo apt-get install -y perl cpanminus

# Install required Perl modules
sudo cpanm Switch JSON LWP::UserAgent
```

#### Download and Install Nipe
```bash
# Clone Nipe repository
git clone https://github.com/htrgouvea/nipe
cd nipe

# Install Nipe
sudo perl nipe.pl install

# Verify installation
perl nipe.pl help
```

### 4. Tor Installation

#### Install Tor Service
```bash
# Add Tor repository
echo "deb https://deb.torproject.org/torproject.org $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/tor.list

# Add GPG key
wget -qO- https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc | \
sudo gpg --dearmor -o /usr/share/keyrings/tor-archive-keyring.gpg

# Update and install
sudo apt-get update
sudo apt-get install -y tor tor-geoipdb

# Start Tor service
sudo systemctl start tor
sudo systemctl enable tor
```

### 5. Nmap Installation

#### Install Latest Nmap
```bash
# Install from repository
sudo apt-get install -y nmap

# Or compile from source for latest version
wget https://nmap.org/dist/nmap-7.94.tar.bz2
bzip2 -cd nmap-7.94.tar.bz2 | tar xvf -
cd nmap-7.94
./configure
make
sudo make install
```

### 6. Traffic Analysis Tools

#### Tcpdump Installation
```bash
sudo apt-get install -y tcpdump

# Set capabilities to run without sudo
sudo setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump
```

#### Wireshark Installation
```bash
# CLI version (tshark)
sudo apt-get install -y tshark

# GUI version (optional)
sudo apt-get install -y wireshark

# Add user to wireshark group
sudo usermod -a -G wireshark $USER
```

### 7. Additional Security Tools

#### Install Supporting Tools
```bash
# Network discovery
sudo apt-get install -y netcat-openbsd

# DNS tools
sudo apt-get install -y dnsutils

# Packet crafting
sudo apt-get install -y hping3

# SSL/TLS analysis
sudo apt-get install -y sslscan testssl.sh
```

## Configuration

### 1. Nipe Configuration

#### Test Nipe Functionality
```bash
# Start Nipe
sudo perl nipe/nipe.pl start

# Check status
sudo perl nipe/nipe.pl status

# Stop Nipe
sudo perl nipe/nipe.pl stop
```

### 2. Environment Variables Setup

Create `.env` file for sensitive data:
```bash
# Create environment file
cat > ~/.network_research.env << EOF
export REMOTE_USER="your_username"
export REMOTE_SERVER="your_server_ip"
export SSH_PASS="your_password"
EOF

# Source in your scripts
source ~/.network_research.env
```

### 3. SSH Key Setup (Recommended)

#### Generate SSH Keys
```bash
# Generate key pair
ssh-keygen -t ed25519 -C "network-research"

# Copy to remote server
ssh-copy-id user@remote_server
```

## Verification

### Check All Tools
```bash
#!/bin/bash
# Tool verification script

echo "Checking installed tools..."

tools=("curl" "jq" "sshpass" "nmap" "tor" "tcpdump" "perl")

for tool in "${tools[@]}"; do
    if command -v $tool &> /dev/null; then
        echo "✓ $tool is installed"
        $tool --version 2>&1 | head -n 1
    else
        echo "✗ $tool is NOT installed"
    fi
done

# Check Nipe
if [ -d "nipe" ]; then
    echo "✓ Nipe directory found"
else
    echo "✗ Nipe not found"
fi

# Check Tor service
if systemctl is-active --quiet tor; then
    echo "✓ Tor service is running"
else
    echo "✗ Tor service is not running"
fi
```

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: Nipe Won't Start
```bash
# Check for conflicting services
sudo systemctl stop tor
sudo perl nipe.pl stop
sudo perl nipe.pl start

# Check iptables rules
sudo iptables -t nat -L
```

#### Issue 2: Perl Module Errors
```bash
# Force reinstall modules
sudo cpanm --force Switch JSON LWP::UserAgent

# Check Perl version
perl -v
```

#### Issue 3: Permission Denied
```bash
# Fix permissions
chmod +x script.sh
sudo chown $USER:$USER /path/to/files
```

#### Issue 4: Connection Refused
```bash
# Check firewall
sudo ufw status
sudo ufw allow 9050/tcp  # Tor SOCKS port
sudo ufw allow 9051/tcp  # Tor control port
```

## Security Considerations

### 1. Secure Installation
- Always verify GPG signatures when downloading tools
- Use official repositories when possible
- Keep tools updated regularly

### 2. Permission Management
- Run tools with minimum required privileges
- Avoid running as root unless necessary
- Use capability-based permissions where possible

### 3. Log Management
```bash
# Create secure log directory
sudo mkdir -p /var/log/network-research
sudo chmod 750 /var/log/network-research
sudo chown $USER:adm /var/log/network-research
```

## Platform-Specific Instructions

### Ubuntu 20.04/22.04
- All commands above work as-is
- May need to enable universe repository:
  ```bash
  sudo add-apt-repository universe
  ```

### Debian 11/12
- Replace `lsb_release -cs` with specific version name
- May need to install `lsb-release` package first

### Kali Linux
- Most tools pre-installed
- Update with: `sudo apt update && sudo apt upgrade`

### macOS (via Homebrew)
```bash
# Install Homebrew first
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install tools
brew install curl jq nmap tor
brew install --cask wireshark
```

### Windows (WSL2)
1. Install WSL2 with Ubuntu
2. Follow Ubuntu instructions above
3. For GUI tools, install X server (VcXsrv or similar)

## Testing Your Setup

### Basic Connectivity Test
```bash
# Test without anonymity
curl -s https://ipinfo.io/ip

# Test with Tor
curl -s --socks5 127.0.0.1:9050 https://ipinfo.io/ip
```

### Nmap Test
```bash
# Test on localhost
nmap -sV localhost

# Test with specific options
nmap -sS -sV -O -p- scanme.nmap.org
```

### Packet Capture Test
```bash
# Capture 10 packets
sudo tcpdump -c 10 -i any

# Capture and save
sudo tcpdump -w test.pcap -c 100
tcpdump -r test.pcap
```

## Maintenance

### Regular Updates
```bash
# Create update script
cat > update_tools.sh << 'EOF'
#!/bin/bash
echo "Updating system packages..."
sudo apt-get update
sudo apt-get upgrade -y

echo "Updating Nipe..."
cd nipe && git pull && cd ..

echo "Updating Perl modules..."
sudo cpan-outdated -p | cpanm

echo "Update complete!"
EOF

chmod +x update_tools.sh
```

### Backup Configuration
```bash
# Backup important configs
tar -czf network-tools-config.tar.gz \
    ~/.bashrc \
    ~/.network_research.env \
    ~/nipe/
```

## Resources

- [Nipe GitHub](https://github.com/htrgouvea/nipe)
- [Tor Project Documentation](https://www.torproject.org/docs/)
- [Nmap Reference Guide](https://nmap.org/book/)
- [Tcpdump Tutorial](https://danielmiessler.com/study/tcpdump/)
- [Wireshark User Guide](https://www.wireshark.org/docs/)
# Vulnerability

## Objective
This project is designed to simulate the mindset and methods of a potential attacker. By scanning the network, identifying vulnerabilities, and attempting to exploit them, Individuals can gain a deeper understanding of the network's weaknesses. This isn't just about finding holes in the system; it's about learning how an attacker might think and act, so we can strengthen our defenses.

### Skills Learned
#### Network Scanning and Mapping:
- Using tools like Nmap for scanning network ports and services.
- Differentiating between basic and full network scans (including NSE scripts).

#### Vulnerability Analysis:

- Automating the identification of vulnerabilities in local networks using tools like Searchsploit.
- Understanding how to use the Nmap Scripting Engine (NSE) for vulnerability assessment.

#### Password Cracking:

- Detecting weak passwords for common login services such as SSH, RDP, FTP, and TELNET.
- Working with tools like Hydra and Medusa to automate brute-force attacks.

#### User Input Handling:

- Creating functions to validate user inputs and make the process more user-friendly.
- Collecting user-defined parameters for network scans and password lists.

#### Logging and Reporting:

- Logging scan results and providing an option to search and save the results in a structured manner.
- Generating reports, including the ability to save results in a ZIP file for easy sharing.

#### Automation Scripting:

- Writing automated scripts using tools mentioned to minimize manual intervention.
- Leveraging functions to modularize the code and improve reusability.

#### Security Tools Familiarity:

- Gaining hands-on experience with popular penetration testing tools like Nmap, Hydra, Medusa, and Searchsploit.

#### Shell Scripting:

- Developing skills in Bash scripting to automate tasks.
- Using comments in code for documentation and attributing borrowed code.

#### Penetration Testing Workflow:

- Understanding and following a structured penetration testing workflow, including scanning, password cracking, vulnerability mapping, and result logging.

#### Credential Analysis:

- Evaluating credential strength in the network by using pre-defined or user-supplied password lists.

#### User Experience and Interface Design:

- Designing user interactions to select between basic or full scans, and enabling effective user feedback during each stage of the process.

#### Security Protocols Knowledge:

- Gaining knowledge of common network protocols such as SSH, RDP, FTP, and Telnet, and understanding their security implications.

#### Documentation:

- Documenting code with comments for better readability and understanding, especially when working in collaborative environments or for academic purposes.
- Preparing submission materials, including screenshots to demonstrate project functionality.

#### Data Management:

- Managing output data, including saving results in ZIP format for easy archival and transfer.
- Allowing search functionality within log results for efficient data retrieval.

#### Risk Identification and Mitigation:

- Learning how to identify security risks related to network vulnerabilities and weak passwords.
- Applying measures to understand potential mitigation strategies.

#### Operational Security Order:

- Familiarizing with the concept of an operation order and how it applies to structuring penetration testing projects for ongoing monitoring and asset protection.

#### Project Structuring and Modularity:

- Structuring a project into distinct modules (e.g., user input handling, weak credential detection, vulnerability mapping) to enhance maintainability and clarity of the code.

#### Use of Pre-built Tools and Custom Scripts:

- Learning how to effectively combine pre-built security tools and custom scripts to create an integrated penetration testing system.

#### Cybersecurity Automation Techniques:

- Building foundational knowledge in cybersecurity automation, especially focusing on tasks that benefit from reduced manual intervention to enhance security coverage and efficiency.

#### Report Generation and Presentation:

- Understanding the importance of presenting findings in a way that is useful to stakeholders, including providing clear visual representations and structured reports of detected vulnerabilities.

### Tools Used

1. Nmap - For network scanning and identifying open ports and services.
2. Hydra - For performing brute-force attacks on services like SSH, FTP, RDP, and Telnet.
3. Searchsploit - For identifying known vulnerabilities related to the services detected.
4. Nipe - For anonymizing the connection.
5. curl - Used for verifying anonymous connection.
    * jq - Used alongside curl for data manipulation in JSON format.
6. Grep - For searching within result files.
7. Zip Utility - For compressing result files into a ZIP archive.
8. apt-get - Linux package manager for installing and updating system tools.
9. pip - Python package installer for managing Python packages.
10. Geany - Text editor for manually viewing the results.

## Methodologies

The methodologies used in this project are focused on systematically identifying and evaluating the security posture of the network. The approach is divided into several stages, each utilizing specific tools and techniques to gather information, assess vulnerabilities, and attempt exploitation. The following sections detail the steps taken during the assessment.

### Network Scanning
* Method:
    * The script scans the network for open TCP ports and identifies the services running on them using Nmap. The scan aims to provide essential details about active services within the specified network range.

* Tools Used:
    * Nmap: Utilized for discovering open ports and identifying the services running on those ports. The script does not use NSE
    scripts.

* Command Example:
    * `Basic Scan: nmap -sS -sV {network_range}`

### Vulnerability Assessment

* Method:
    * The script identifies potential vulnerabilities by using service versions discovered in the network scan and cross-referencing them with known exploits.

* Tools Used:
    * Searchsploit: A command-line interface for the Exploit-DB database, allowing the script to find known exploits for the detected service versions.

* Command Example:
    * `searchsploit {service_version}`

### Brute-force Attacks

* Method:
    * This method tests for weak or default credentials on selected services by attempting multiple username and password combinations.

* Tools Used:
    * Hydra: A versatile tool for performing brute-force attacks on services such as SSH, FTP, RDP, and Telnet.

* Command Example:
    * `hydra -L {username_list} -P {password_list} {ip} {service} -s {port}`

#### Logging and Reporting

* Method:
    * All results from network scans, vulnerability assessments, and brute-force attacks are logged in a structured format. The script also offers options to search through these logs or compress them for further use.

* Tools Used:
    * Text Files: For storing results.
    * Grep: A command-line utility for searching within the results.
    * Zip Utility: For compressing all results into a single file.

* Command Example:
    * Search: `grep {search_term} {output_file}`
    * Zip: `zip -r scan_results.zip {output_directory}`

### Tool Management

* Method:
    * Ensures that all necessary tools are installed and up-to-date. This method checks for missing tools and installs them if necessary.

* Tools Used:
    * Apt-get (Linux Package Manager): Used for installing and updating system tools.
    * Pip (Python Package Installer): For managing Python packages.

* Command Example:
    * System Tools: `sudo apt-get install {missing_tools}`
    * Python Packages: `pip install {missing_packages}`

## Discussion

### Tools Check and Installation

### Overview

In the initial phase of the script, the goal is to ensure that all the necessary tools and Python packages are installed and up to date. This is crucial for the rest of the script to function correctly, as missing tools would cause errors later in the process.

### Code Section

Here’s the code snippet that handles tool checking, installation, and updating:

![Code Snippet](/images/code_snippet.png "Code Snippet")

### Detailed Explanation

#### Tools List:
* required_tools: This dictionary holds the names of the tools that are necessary for the script to function. 
    
    For example:
    > * nmap for network scanning,
    > * searchsploit for vulnerability assessment,
    > * hydra for brute-force attacks,
    > * pip for Python package management.
    
    This ensures that the script covers different aspects of penetration testing, from scanning to exploitation.

* Tool Check Function (`is_tool_installed`):
    * This function tries to run each tool with the --version flag to check if it’s installed. If the tool isn’t found (FileNotFoundError), it returns False, indicating that the tool needs to be installed.
    * This approach is efficient because it doesn’t require complex checks and leverages existing command-line utilities to determine the presence of the tool.

* Installation and Update Function (`install_and_update_tools`):
    * Missing Tools Identification:
        * The script loops through the required tools and identifies any that aren’t installed. These tools are added to a missing_tools list, which will be installed later.
    * System Tools Installation:
        * If there are any missing tools, the script uses apt-get to update the package list (sudo apt-get update) and then installs the missing tools (`sudo apt-get install -y`). The ==-y== flag automatically answers "yes" to prompts during installation, ensuring the process is non-interactive.
        * If the installation fails, the script exits (sys.exit(1)), preventing further execution without the required tools.
        * Python Package Check and Installation:
            * Similar to system tools, the script checks if the required Python packages (like colorama) are installed. If they’re missing, the script uses pip to install them. This ensures that the script can handle colored output for better user experience.
* Error Handling:
    * The script handles errors gracefully by checking for issues during tool installation. If something goes wrong, it prevents further execution, ensuring that the user is aware of the problem and can resolve it before continuing.

#### Why This is Important 
Ensuring that the environment is correctly set up is a crucial first step in any script. By automating the process of checking for and installing necessary tools, this script reduces the likelihood of encountering errors later on due to missing dependencies. It also makes the script more user-friendly, as it handles the setup process automatically.
    
This part of the script essentially acts as a "gatekeeper," ensuring that all the necessary components are in place before the main functionality of the script begins.

### User Input Handling

### Overview

The script gathers various inputs from the user, such as the network range to scan, the output
directory, and the type of scan to perform. This section is essential because it sets up the
parameters for the entire operation, allowing for a tailored experience based on user needs.

### Code Section

Below is the code snippet that handles user input:

![Code Snippet](/images/userinput_handling.png "User Handling")

### Detailed Explanation

* Getting Network Range (`get_network_input`):
    * The script first prompts the user to input a network range in the format 192.168.x.x/24.
        * If the input doesn’t match the expected format, the script prints an error message and recursively calls the function to prompt the user again. This ensures that only valid input is accepted.    
    * **Regex Validation**: The input is validated using a regular expression that checks for proper IP address formatting (e.g., four octets separated by periods) and the subnet mask length (e.g., /24).
* Regex Breakdown:
    * ^\d{1,3}: This part checks for the first octet of the IP address, which should be a number between 1 and 3 digits long.
    * (\.\d{1,3}){3}: This checks for the next three octets, each separated by a dot, again ensuring they are between 1 and 3 digits.
    * /\d{1,2}$: This checks for the subnet mask, which is typically between 1 and 2 digits (e.g., /24).

    > Example Input:
    > Valid: 192.168.1.0/24
    > Invalid: 192.168.256.0/33

* Getting Output Directory (`get_output_directory`):
    * The user is asked whether they want to save the output in the current directory or specify a custom directory.
    * **Directory Handling**:
        * If the user chooses to save in the current directory (yes), the script uses os.getcwd() to get the current working directory and logs a status message indicating where the output will be saved.
        * If the user chooses a custom directory (no), the script prompts the user to input a directory path. If the directory doesn’t exist, it’s created using os.makedirs() to ensure that the output can be saved there.
        * If the user provides an invalid choice (not yes or no), the script recursively calls the function to prompt for valid input.

    > Example Input:
    > Choosing yes: The output will be saved in the current directory, such as /home/user/.
    > Choosing no: The user might input /home/user/custom_dir, and the script will create this directory if it doesn’t exist.
* Choosing Scan Type (get_scan_type):
    * The user is prompted to select either a "Basic" or "Full" scan.
    * **Input Validation**: The input is converted to lowercase and validated against the allowed choices (basic or full). If the input is invalid, the script prints an error message and prompts the user again.

    > Example Input:
    > Valid: basic, full
    > Invalid: medium (would trigger an error and prompt the user again)

#### Why This is Important

User input is a critical aspect of the script, as it defines how the subsequent processes will be executed. By validating inputs and providing feedback, the script ensures that only valid data is processed, minimizing the risk of errors during execution.

This part of the script adds flexibility, allowing users to customize the scanning process according to their needs. For example, they can specify which network range to scan and where to save the results, ensuring that the script fits seamlessly into their workflow.

    > Example in Practice
    > Network Input: When the script asks for the network range, the user might input 192.168.1.0/24.
      The script will validate this input and proceed only if it’s in the correct format.
    > Output Directory: If the user chooses to save the results in a custom directory,
      they might input /home/user/scans, and the script will create this directory if it doesn’t already exist.

By handling user inputs effectively, the script ensures that the entire process is configured correctly from the start, leading to more accurate and reliable outcomes. With these inputs set, the script can then move forward to the actual scanning and analysis
phases. This user-centric approach makes the tool both powerful and accessible to users of varying expertise levels.

### Perform the TCP Scan

### Overview

This part of the script is responsible for conducting the TCP scan using Nmap, which is essential for identifying open ports and services on the target network. The scan results are saved to a specified output file, allowing for further analysis in subsequent steps.

### Code Section

Below is the code snippet that handles the TCP scan:

![Code Snippet](/images/tcpscan.png "tcp_scan")

### Detailed Explanation

* Nmap Command Breakdown:
    * `nmap -sS`: This flag tells Nmap to perform a TCP SYN scan, also known as a stealth scan. This type of scan sends SYN packets to the target ports and listens for responses, allowing it to detect open ports without completing the TCP handshake. It’s a widely used method because it’s faster and less detectable than a full TCP connection scan.
    * `-sV`: This flag enables version detection, which allows Nmap to probe open ports and determine the services running on them along with their version numbers. This is crucial for vulnerability assessment and further analysis.
    * -oN {output_file}: This flag specifies the output format (normal format) and the file where the results will be saved. By saving the scan results to a file, the script ensures that the data can be accessed and used later in the process.
* File Handling:
    * Output File Creation: The scan results are saved in a file named tcp_scan_results.txt in the specified output directory. This file will contain all the information gathered during the TCP scan, including open ports and detected services.
    * Directory Management: The script checks whether the specified output directory exists and creates it if necessary. This ensures that the scan results are saved in the correct location.
* Logging:
    * Status Updates: The script logs status messages to keep the user informed about the progress of the scan. For example, it informs the user when the scan is starting and when it has completed. This is helpful for managing expectations, especially since network scans can take some time depending on the network size and the number of hosts.

    > Example in Practice:
        > Suppose the user inputs a network range of 192.168.1.0/24. The generated Nmap command would be:
        > *  `nmap -sS -sV 192.168.1.0/24 -oN /path/to/output_directory/tcp_scan_results.txt`
* Output Format:
    * Normal Format Output: The -oN flag ensures that the results are saved in a human-readable format. This is important because the next steps in the script will parse this file to extract relevant information such as service names, versions, and ports.
* Importance of the TCP Scan:
    * The TCP scan is a foundational step in the network assessment process. It identifies the open ports and running services, which are key targets for further analysis, such as vulnerability mapping and brute-force attacks. By understanding the network’s attack surface, security practitioners can prioritize areas for deeper investigation.

#### Why This is Important

The TCP scan serves as the foundation for identifying potential entry points into the network. By discovering open ports and services, the script sets the stage for subsequent vulnerability assessments and brute-force attacks. This step is critical for understanding the network's exposure and identifying weak points that could be exploited by attackers.

By automating this process, the script ensures that all potential attack vectors are identified quickly and efficiently. This information is then used to guide further analysis, making it a crucial part of any cybersecurity assessment.

> Example in Practice
> After running the scan, the user might review the tcp_scan_results.txt file and see output like this:
> ![Code Snippet](/images/tcpscan_example.png "tcpscan_example")
> This output reveals that FTP, SSH, and HTTP services are running on the target machine, with specific versions identified. These
> services become targets for further testing and exploitation. 
>
> * In summary, this part of the script efficiently identifies open 
>   ports and running services, setting the stage for the vulnerability assessments and brute-force attacks that follow. The use of
>   Nmap’s powerful scanning capabilities ensures comprehensive coverage of the network, while the output file provides a structured
>   format for analysis

### Extracting Service Ports

### Overview

This section of the script is responsible for parsing the results of the TCP scan and extracting
the open ports and corresponding services. The extracted data is stored in a dictionary for easy
access during the vulnerability assessment and brute-force attack stages.

### Code Section

Here is the code snippet that handles the extraction of service ports:

![Code Snippet](/images/extractionSP.png "ESP")

### Detailed Explanation

* Reading the Output File:
    * The script opens the Nmap scan results file (`tcp_scan_results.txt`) and reads its contents line by line. This allows the script to parse the results and identify relevant information about open ports and services.
* Regex Pattern for Extraction:
    * The script uses a regular expression (regex) to search for lines that match the pattern of an open TCP port followed by the service name. 
    
    > Specifically, it looks for:
    > `\d{1,5}/tcp`: This matches the port number (which can be between1 and 5 digits) followed by /tcp.
    > `\s+open\s+`: This matches the word "open" with any amount of whitespace before and after it.
    > `\S+`: This captures the service name, which consists of one or more non-whitespace characters.
    > * The regex effectively identifies lines that indicate an open TCP port and the associated service.
* Extracting Port and Service Name:
    * Once the regex finds a match, the script extracts the port number and service name from the matched string.
    * port = `match.group(1).split('/')[0]`: This extracts the port number from the match and removes the /tcp suffix, leaving just the numeric value.
    * service_name = `match.group(2).lower()`: This extracts the service name and converts it to lowercase for consistency.
    * The extracted port and service name are stored in a dictionary (service_ports), where the service name is the key, and the port number isthe value.
* Storing the Data:
    * The dictionary service_ports stores the mapping of service names to their corresponding ports. This dictionary is returned at the end of the function and is used later in the script to identify which ports to target during brute-force attacks.

    > Example Output:
    > If the TCP scan detects the following services, the service_ports dictionary might look like this:
    > ![Code Snippet](/images/ESP_example.png "Code Snippet")

#### Why This is Important

This step is crucial because it provides a structured way to access the services detected during the scan. By storing the service-port mappings in a dictionary, the script can efficiently identify and target specific services during the vulnerability assessment and brute-force attack stages.
The regex pattern matches this line, extracts the port number (22) and service name (ssh), and adds them to the service_ports dictionary. This allows the script to later reference the SSH service and its associated port number when performing brute-force attacks or vulnerability assessments.

By breaking down the scan results in this way, the script ensures that it can easily access and utilize the information gathered during the TCP scan. This structured approach is essential for the subsequent stages of the script, where precise targeting of services is required.

#### Use Case:
For example, if the user chooses to perform a brute-force attack on the FTP service, the script will reference the service_ports dictionary to find that FTP is running on port 21. This makes the script both flexible and scalable, as it can handle different network configurations and
service setups without hardcoding port numbers.

### Vulnerability Mapping

### Overview

In this section, the script performs vulnerability mapping by searching for known vulnerabilities associated with the services detected during the TCP scan. This is done using the Searchsploit tool, which provides a database of exploits and vulnerabilities based on service versions. The results of the vulnerability mapping are appended to the TCP scan results file.

### Code Section

Here is the code snippet that handles vulnerability mapping:

![Code Snippet](/images/Vulner_map.png "Vulnerability Mapping")

### Detailed Explanation

* Starting the Vulnerability Mapping:
    * The script begins by informing the user that vulnerability mapping is starting. This sets the stage for the next phase, where the script will attempt to identify known vulnerabilities associated with the detected services.
    * Searchsploit:
        * Searchsploit: This tool provides access to a vast database of known exploits and vulnerabilities. By querying Searchsploit with the service version identified during the TCP scan, the script can find relevant vulnerabilities that might be exploited.
    * Command Execution: The script constructs a command using the searchsploit tool and executes it in the shell. The command is designed to search for vulnerabilities related to the service version detected in the previous scan. For example, if the service version is "Apache 2.4.29," the command would be
        * `searchsploit Apache 2.4.29`
    * Capturing Output: The script captures the output of the searchsploit command and writes it to the TCP scan results file. If vulnerabilities are found, the details are appended to the file under a "Vulnerability Assessment Results" section.

* Regex Matching and Data Extraction:
    * The script uses regular expressions (regex) to extract the service name, port number, and version from the Nmap scan results. This information is crucial for querying Searchsploit with the correct service version.
* Regex Breakdown:
    * `\d{1,5}/tcp`: Matches the port number followed by /tcp.
    * `\s+open\s+`: Matches the word "open" surrounded by whitespace.
    * `\S+`: Captures the service name.
    * `.*`: Captures the service version.
    * The script then checks if the service/port pair has already been processed. If not, it adds the pair to the vulnerable_services set and performs the vulnerability check.

* Appending Results:
    * File Handling: The script opens the TCP scan results file in append mode, ensuring that the vulnerability assessment results are added to the end of the file without overwriting existing data.
    * Unique Vulnerable Services: By using a set (vulnerable_services) to track unique service/port pairs, the script avoids duplicating vulnerability checks for the same service running on different ports.

* Example Output:
    > After the vulnerability mapping is complete, the tcp_scan_results.txt file might include entries like this:
    > ![Code Snippet](/images/Vulner_result.png "Vulnerability Mapping Result")
    > * This output provides valuable information about potential vulnerabilities that can be further exploited during penetration
    > testing.

#### Why This is Important

Vulnerability mapping is a critical step in identifying potential weaknesses in the network. By leveraging known exploits, security practitioners can prioritize areas for further testing and remediation. The results of this phase guide the brute-force attacks and other penetration testing efforts that follow.

Example in Practice

If the Nmap scan detects Apache 2.4.29 running on port 80, the script uses Searchsploit to find any known vulnerabilities associated with that version. If an exploit is found, the details are written to the results file, providing actionable intelligence for further testing. 
By automating this process, the script ensures comprehensive coverage of all detected services, making it a valuable tool for vulnerability assessments.

### Getting Credentials Lists

### Overview

This section of the script prompts the user to choose whether they want to use the default username and password lists for brute-force attacks or specify custom ones. The script ensures that the provided file paths exist and are valid before proceeding.

### Code Section

Here is the code snippet that handles getting the username and password lists:

![Code Snippet](/images/getcredlist.png "Code Snippet")

### Detailed Explanation

* User Choice for Default or Custom Lists:
    * The script first prompts the user with a choice: whether to use the default username and password lists or specify custom ones. This gives the user flexibility in how they approach the brute-force attacks.
    * The `input()` function captures the user's response, and the `.lower()` method ensures that the input is normalized to lowercase for comparison.

* Default Lists:
    * If the user selects the default option ('yes'), the script automatically uses the predefined paths for the username and password lists:
    `default_username_list = "/home/kali/PenTesting/PenTestingProject/top-usernames -shortlist.txt"`
    `default_password_list = "/home/kali/PenTesting/PenTestingProject/default-basic -14-passwords.txt"`
    * These paths point to files containing common usernames and passwords that will be used for the brute-force attacks.
* Custom Lists:
    * If the user opts to use custom lists ('no'), the script prompts them to provide thefile paths for both the username and password lists.
    * The `os.path.exists()` function checks whether the provided file paths are valid. If either path is invalid, the script informs the user and prompts them to enter valid paths.
* Error Handling:
    * If the user enters an invalid choice (neither '==yes==' nor '==no=='), the script displays an error message and prompts the user again until a valid choice is made. 
    * This ensures that the script always proceeds with valid input, reducing the likelihood of runtime errors due to missing or incorrect file paths.
*  Flexibility and Customization:
    * This approach allows the script to be flexible and adaptable to different scenarios. If the user has specific username and password lists tailored to a particular target, they can easily integrate those into the brute-force process
    * By default, the script provides a basic set of commonly used usernames and passwords, making it useful for general testing scenarios.

    Example Usage:
    > * Default Option:
        > * ![Code Snippet](/images/gcl_default.png "default selection")
        > * The script will proceed with the predefined lists for brute-force attacks.
    > * Custom Option:
    > * ![Code Snippet](/images/gcl_custom.png "custom selection")
    > * The script will validate the provided paths and use the custom lists for brute-force attacks.

#### Why This is Important

The ability to choose between default and custom lists enhances the usability of the script. Users can quickly proceed with default options or fine-tune the brute-force process by supplying their own lists. This flexibility is essential in penetration testing, where different environments may require different approaches.

Example in Practice

In a real-world scenario, a penetration tester might have a custom password list that is specific to a particular organization or target. By allowing the user to input custom lists, the script can adapt to various testing needs, making it a more powerful and versatile tool. This part of the script lays the groundwork for the brute-force attacks that follow, ensuring that the right credentials are used to maximize the chances of success.

### Service Selection for Brute-Force Attacks

### Overview

This section of the script allows the user to select which services (FTP, SSH, RDP, Telnet) they want to target for brute-force attacks. The user can also choose to attack all services, making the script versatile and adaptable to different penetration testing scenarios.

### Code Section

Here is the code snippet that handles service selection:

![Code Snippet](/images/bruteforce_selection.png "Code Snippet")

### Detailed Explanation

* User Choice for Services:
    * The script prompts the user to select which services they want to attack. The user can choose specific services like FTP, SSH, RDP, or Telnet, or they can select "all" to target all supported services.
    * This flexibility allows the user to focus on specific services that are of interest or to perform a comprehensive brute-force attack across multiple services.
* Allowed Services:
* The script defines a list of allowed services: `['ftp', 'ssh', 'rdp', 'telnet']`. These are the services that the script is designed to target for brute-force attacks.
    * If the user selects "all," the script returns this list, indicating that all services should be targeted.
* Service Selection Validation:
* If the user selects specific services (e.g., `ftp, ssh`), the script splits the input into a list and checks each service against the allowed services.
* If the user enters an invalid service (e.g., `http`), the script displays an error message and prompts the user to select valid services.
* This validation ensures that the script only targets services that it is capable of brute-forcing.
* Error Handling:
    * If the user selects invalid services, the script prompts them again until a valid selection is made. This prevents the script from attempting to brute-force unsupported services, reducing the risk of errors during execution.

Example Usage:
* Specific Services:
    ![Code Snippet](/images/bruteforce_specific.jpg "Specific Services")
    * The script will target FTP and SSH for brute-force attacks.
* All Services:
    ![Code Snippet](/images/bruteforce_all.png "All Services")
    * The script will target all supported services (FTP, SSH, RDP, Telnet) for brute-force attacks.

* Flexibility and Focus:
    * This approach allows the user to focus their brute-force efforts on specific services that are of interest. For example, if the user knows that the target environment heavily relies on SSH for remote access, they can choose to focus only on SSH.
    * Conversely, the option to target all services makes the script a powerful tool for comprehensive penetration testing, covering a wide range of potential entry points.

#### Why This is Important

Service selection is a critical aspect of penetration testing. By allowing the user to choose which services to target, the script provides flexibility and adaptability to different testing scenarios. This ensures that the user can tailor their attacks to the specific services that are most likely to yield results, making the testing process more efficient and effective.

Example in Practice

In a real-world penetration test, the user might encounter an environment where SSH is known to be vulnerable due to weak credentials. By selecting only SSH for brute-force attacks, the user can focus their efforts on this service, increasing the likelihood of a successful attack. This part of the script enhances its usability, allowing the user to adapt the testing process to
their specific needs and goals. By providing options for both targeted and comprehensive attacks, the script becomes a versatile tool in the penetration tester's toolkit.

### Brute-Force Attacks on Vulnerable Services

### Overview

This section of the script handles the brute-force attacks on the vulnerable services identified in
the previous stages. The user-selected services (FTP, SSH, RDP, Telnet) are targeted using
Hydra, with the username and password lists provided earlier in the script.

### Code Section

Here is the code snippet that handles brute-force attacks:

![Code Snippet](/images/bruteforce_vul_service.png "Code Snippet")

### Detailed Explanation

* Checking for Vulnerable Services:
    * Before launching brute-force attacks, the script checks if any vulnerable services were identified during the vulnerability assessment. If no vulnerabilities are found, the brute-force attacks are skipped.
* Tracking Attempted Services:
    * The script uses a set (attempted_services) to track the service/port combinations that have already been targeted. This ensures that the same service is not brute-forced multiple times, avoiding redundant attacks.
* Iterating Through Vulnerable Services:
    * The script iterates through the list of vulnerable services and ports that were identified earlier. For each service, it checks if the service is part of the user-selected services for brute-forcing.
* Executing Hydra for Brute-Force Attacks:
    * If a service is selected for brute-forcing and has not been attempted yet, the script constructs a Hydra command to perform the attack. Hydra is a powerful tool that can perform dictionary-based attacks against various services, using the username and password lists provided by the user.

    Example Hydra command:
    > `hydra -vV -L /path/to/usernames.txt -P /path/to/passwords.txt 192.168.232.136 ssh -s 22`
    > * Flags Explanation:
    > * -vV: Enables verbose output, providing detailed logs of the attack progress.
    > * -L: Specifies the path to the username list.
    > * -P: Specifies the path to the password list.
    > * The service (e.g., ssh) and the port (-s 22) are specified based on the service being targeted.

* Handling Command Output:
    * The script captures the output of the Hydra command and checks for success indicators like "login:" or "password:" in the output. If a successful login is found, the details are written to the output file, and the user is notified.
    * If no successful attempts are found, the script logs the failure and moves on to the next service.
* Error Handling:
* The script checks the return code of the Hydra process to detect any errors during the attack. If the command fails, the user is informed, and the script continues with the next service.
* Avoiding Duplicate Attempts:
    * After a service/port combination has been attempted, it is added to the attempted_services set. This ensures that the same service is not brute-forced again, optimizing the script's performance and avoiding redundant attacks.
* Example Usage:
    * Suppose the user selected FTP and SSH for brute-forcing. If the vulnerability assessment identified these services as vulnerable, the script would attempt brute-force attacks on the relevant ports (e.g., 21 for FTP, 22 for SSH).
    * The results of the brute-force attacks, whether successful or not, would be logged in the output file, providing a clear record of the attack outcomes.

#### Why This is Important

Brute-force attacks are a fundamental technique in penetration testing, particularly when weak
credentials are suspected. This section of the script automates the process, allowing the user to
efficiently target vulnerable services and identify weak login credentials. By integrating Hydra,
the script leverages a powerful tool for brute-forcing, increasing the chances of successfully
compromising the target.

Example in Practice

In a real-world penetration test, the script might identify a vulnerable SSH service on a specific
port. By using Hydra to brute-force this service, the tester can potentially gain unauthorized
access to the system, highlighting a critical security flaw that needs to be addressed.
This part of the script is crucial for testing the resilience of services against brute-force attacks,
making it a valuable asset in any penetration tester's toolkit.

### Searching and Viewing the Results

### Overview

This section of the script allows the user to search through the results of the scan and
brute-force attempts. It provides two options: using grep for command-line searching and
opening the results in a code editor for manual inspection.

### Code Section

Here is the code snippet that handles searching and viewing results:

![Code Snippet](/images/Search_view.png "Search Code Snippet")

### Detailed Explanation

* Search with grep:
    * The script provides a command-line search option using grep. The user is prompted to enter a search term, which is then used to search through the results file.
    * The grep command is case-insensitive (`-i flag`) to ensure that matches are found regardless of the case of the search term.
    * This is useful for quickly locating specific information within a large results file, such as finding occurrences of a particular service, port number, or vulnerability.

        > Example:
        > ![Code Snippet](/images/search_ftp.png "Term to Search")
        > The script will execute:
        > ![Code Snippet](/images/search_script_ftp.jpg "Code Snippet")
        > 
        > This command searches for all instances of "ftp" (case-insensitive) in the results file and displays the matching lines.
* Open Results in Geany:
    * As an alternative to command-line searching, the script offers the option to open the results file in Geany, a graphical text editor.
    * If the user chooses to open the file in Geany, the script executes a command to launch the editor with the results file. This allows the user to manually browse through the file, use search features in Geany, and analyze the data more comfortably.

        > Example:
        > The script will prompt:
        > ![Code Snippet](/images/search_geany.png "Code Snippet")
        > * If the user selects "yes," the script runs:
        > * > ![Code Snippet](/images/search_geany_results.jpg "Code Snippet")
        > This command opens the results file in the Geany editor, where the user can use the editor's features to navigate through the data.
* User-Friendly Options:
    * By providing both grep and Geany as options, the script caters to different user preferences. Users who are comfortable with the command line can quickly search with grep, while those who prefer a graphical interface can use Geany.
    * This flexibility makes the script accessible to a wider range of users, ensuring that the results can be efficiently analyzed regardless of the user's skill level or preferred working environment.
* Error Handling:
    * The script includes basic error handling for the Geany option. If the user enters an invalid choice (other than "yes" or "no"), they are prompted again until a valid selection is made. This prevents the script from proceeding with incorrect input.

#### Why This is Important

The ability to search and view results efficiently is crucial in penetration testing. Large scan results can be overwhelming, and finding specific information quickly can make the difference between identifying a vulnerability or missing it entirely. By offering both command-line and graphical options, the script ensures that users can analyze the data in the way that best suits
their workflow.

Example in Practice

In a real-world scenario, after performing a full scan and vulnerability assessment, a penetration tester might want to quickly locate all instances of a particular service (e.g., SSH) in the results. Using the grep function, they can instantly filter the results, saving time and allowing them to focus on the relevant data. This part of the script enhances its usability by making the data accessible and easy to navigate, which is essential for effective penetration testing.

### Zipping everything into a ZIP file

### Overview

The final part of the script allows users to compress all the generated result files into a single ZIP file. This feature is useful for organizing the output, making it easier to store, transfer, or submit the results for further analysis.

### Code Section

Here is the code snippet that handles zipping the results:

![Code Snippet](/images/zip_code.png "Code Snippet")

### Detailed Explanation

* Prompting the User:
    * The script first prompts the user to decide whether they want to compress all result files into a single ZIP file. This prompt is presented after all the scanning, vulnerability assessment, and brute-force attempts are completed.
    * The user can respond with "yes" to proceed with zipping the files or "no" to skip this step.

* Creating the ZIP Archive:
    * If the user chooses to zip the files, the script creates a new ZIP file named scan_results.zip in the specified output directory.
    * The script uses Python’s built-in zipfile module to handle the compression. The zipfile.ZipFile class is used to create a new ZIP file, and the write() method adds files to it.
* Filtering Files to Include:
    * The script recursively walks through the output directory using os.walk() to identify all the files that should be added to the ZIP archive.
    * Only files with a .txt extension are included in the ZIP file. This ensures that only relevant result files (like scan outputs and logs) are compressed, avoiding unnecessary files.
* Error Handling and Re-prompting:
    * If the user enters an invalid choice (anything other than "yes" or "no"), the script will prompt them again until a valid response is provided. This ensures that the script behaves as expected and doesn't proceed with incorrect input.
* Feedback to the User:
    * Once the zipping process is complete, the script provides feedback to the user, confirming that all results have been successfully compressed into the specified ZIP file. This message is color-coded in green to indicate success.

#### Why This is Important

The ability to zip all the results into a single file is important for several reasons:
* Organization: Compressing all results into a single file helps in keeping the output organized and prevents clutter in the working directory.
* Portability: A ZIP file is easier to transfer between systems, whether for backup purposes, sharing with team members, or submitting for grading in an educational setting.
* Space Saving: By compressing the files, the script helps save disk space, especially if the scan results are large.

Example in Practice

In a penetration testing scenario, after completing all scans and assessments, a tester may need to submit the results to their client or store them for future reference. Having all results compressed into a single ZIP file makes this process straightforward and ensures that no files are accidentally omitted.

By including this feature, the script ensures that users can easily manage the outputs of their scanning and brute-force activities, making the overall process more efficient and user-friendly. The final part of the script ties everything together by providing a clean and organized way to handle the outputs. The option to compress the results into a ZIP file adds a layer of
professionalism and practicality to the tool, making it a complete package for network scanning, vulnerability assessment, and brute-force testing.

## Conclusion

The script developed for network scanning, vulnerability assessment, and brute-force attacks represents a comprehensive tool tailored for cybersecurity practitioners. It automates critical aspects of penetration testing, including identifying open ports, determining service versions, assessing potential vulnerabilities, and attempting to exploit weak credentials through brute-force
attacks.

From the perspective of a cybersecurity practitioner, this script offers several key advantages:

* Automation of Tedious Tasks: Manual scanning and vulnerability assessment can be time-consuming. By automating these processes, the script allows practitioners to focus on more critical aspects of their assessments, such as analyzing the results and planning further penetration tests.
* Customizability: The script allows users to choose between basic and full scans, select specific services for brute-force attacks, and use custom password lists. This flexibility makes it suitable for various scenarios, from quick assessments to in-depth penetration tests. 
* Efficiency: With built-in tools like nmap, searchsploit, and hydra, the script efficiently handles the most crucial tasks in penetration testing. It also offers features like result compression and searching, making it easier to manage and analyze the outputs.
* Learning Tool: For those new to penetration testing, this script serves as an excellent learning tool. By interacting with the script and reviewing the outputs, users can gain hands-on experience with core penetration testing techniques and understand how different tools work together.

### Crucial Discoveries:

* Automation Enhances Efficiency: The automation of network scanning, vulnerability assessment, and brute-force attacks significantly reduces the time required for penetration testing. Tasks that would typically be done manually are streamlined, allowing for more focus on analysis and mitigation.
* Dynamic Service Detection: By dynamically extracting service ports from the scan results, the script ensures that no service is overlooked. This flexibility is crucial when dealing with environments where services may not run on their default ports.
* Importance of Customization: The ability to customize password lists and choose specific services for brute-force attacks emphasizes the need for tailored testing approaches. Not every environment is the same, and the script's adaptability makes it versatile in different testing scenarios. 
* Integrated Toolchain: Leveraging tools like nmap, searchsploit, and hydra within a single script demonstrates the power of integrating different security tools. Each tool plays a specific role, from discovery to exploitation, highlighting the importance of a well-rounded approach in cybersecurity assessments.

### Lessons Learned:
* Thoroughness is Key: The script teaches that thoroughness in scanning and vulnerability assessment is vital. Even with automation, it's essential to review the results carefully to ensure no critical vulnerabilities are missed. 
* Practical Understanding of Tools: By using this script, users gain a deeper understanding of how various tools work together. This hands-on experience is invaluable in building practical knowledge, which is often more effective than theoretical learning alone.
* Real-World Application: The script's design mirrors real-world penetration testing workflows, making it an excellent training tool. Users learn how to structure their assessments, interpret results, and decide on the next
steps, all within the context of a controlled environment.
* Security Beyond Tools: While the script automates many tasks, it also emphasizes that tools alone are not enough. A cybersecurity practitioner must know how to analyze the outputs, understand the implications of the findings, and take appropriate actions based on the results.

## Recommendations:
* Proactive Patch Management:
    * Rationale: As cybersecurity threats evolve rapidly, keeping systems and software up-to-date is crucial. Implement an automated patch management solution to ensure that all critical systems receive security patches promptly. This reduces the window of exposure to known vulnerabilities, such as the `vsftpd 2.3.4 backdoor`.
* Service Hardening and Minimization:
    * Rationale: Attackers often exploit unnecessary or poorly configured services. Conduct regular audits of running services and disable or remove any that are not essential. For services that must remain operational, implement best practices for securing them, such as using SSH keys instead of passwords and disabling root login.
* Brute-force Mitigation:
    * Rationale: Brute-force attacks are common against services like SSH and FTP. Implement strong password policies and deploy tools like fail2ban to block IP addresses after repeated failed login attempts. Additionally, consider multi-factor authentication (MFA) where possible to further reduce the risk.
* Comprehensive Vulnerability Management:
    * Rationale: Conduct regular vulnerability assessments to identify and remediate security gaps. Use a combination of tools like Nmap for service detection, Searchsploit for vulnerability assessment, and manual checks for high-risk areas. While automated tools are valuable, supplement them with expert analysis to avoid false positives and missed risks.
* Network Segmentation and Isolation:
    * Rationale: By segmenting your network, you limit the lateral movement of attackers who may breach one part of your infrastructure. Use VLANs, firewalls, and access control lists (ACLs) to isolate critical systems from less secure areas, such as guest networks or publicly accessible services.
* Enhanced Monitoring and Incident Response:
    * Rationale: Deploy Security Information and Event Management (SIEM) solutions to collect and analyze log data in real-time. Proactively monitor for indicators of compromise, such as unusual login attempts or unexpected network traffic. Establish clear incident response protocols to react quickly to detected threats.
* Employee Security Training:
    * Rationale: Human error remains a significant factor in security breaches. Regularly train employees on cybersecurity best practices, including phishing awareness, password management, and how to report suspicious activities. Tailor training to specific roles to ensure relevance and impact.
* Data Backup and Recovery Strategies:
    * Rationale: In the event of a ransomware attack or system compromise, having reliable backups is essential. Implement a robust backup strategy that includes regular testing of recovery procedures. Ensure backups are stored securely, both on-site and off-site, to mitigate the risk of data loss.
* Enforce the Principle of Least Privilege:
    * Rationale: Restrict user access to only the resources necessary for their roles. Regularly review and adjust permissions to minimize the potential impact of compromised accounts. Implement role-based access control (RBAC) to enforce these policies across the organization.
* Regular Penetration Testing:
    * Rationale: Conducting periodic penetration tests simulates real-world attack scenarios, providing valuable insights into your security posture. Use the results to refine your defenses, patch vulnerabilities, and ensure that your security measures are effective against emerging threats.

These recommendations focus on reducing risk and enhancing security resilience through a combination of technical controls, regular assessments, and fostering a security-aware culture. Implementing these measures will strengthen your organization's ability to defend against a wide range of cybersecurity threats.

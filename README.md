# penetration-testing
Assigment course penetration testing A.A 2024/2025.

The main goals of this analysis was to identify and document as many vulnerabilities as possible in the system under investigation.

**USED TOOLS
- Nmap[4]: Used to search the ports exposed by the system.
- curl[10]: Used to interact with the web pages in command-line style. Also was used to identify the
responses produced
- Wfuzz[11]: Used to identify XSS payloads
- FFuf[3]: Used to find all pages exposed by the server
- Exploit DB[7]: Used to identify CVEs based on the results found in scanning time
- sqlmap[1]: Used to do SQL injection
- netcat[9]: Used to create connections to and from the container
- Custom Script: Used for brute-force attacks to search the system root password (Sez. 4)

**FINDINGS
- XSS Injection
- SQL Injection
- Remote Command Exectuion

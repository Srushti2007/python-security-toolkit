# Python Security Toolkit

## Overview

Python Security Toolkit is an integrated Python-based cybersecurity framework developed to organize multiple security-testing and defensive demonstration modules under a single command-line interface.

The toolkit provides a structured way to select security modules, collect required inputs, validate user-provided values, execute the selected functionality, and display clear results or error messages.

The project focuses on modular design, reusable utilities, input validation, exception handling, testing, documentation, and responsible use within authorized cybersecurity laboratory environments.
## Features

The toolkit currently includes:

1. MAC Address Changer
2. Network Scanner
3. ARP Spoofing Demo
4. Packet Sniffer
5. Network Queue Demo
6. DNS Spoofing Demo
7. ARP Spoof Detector

## Project Structure

```text
Python-Security-Toolkit/
│
├── main.py
├── requirements.txt
│
├── modules/
│   ├── mac_changer.py
│   ├── network_scanner.py
│   ├── arp_spoofer.py
│   ├── packet_sniffer.py
│   ├── network_jammer.py
│   ├── dns_spoofer.py
│   └── arp_spoof_detector.py
│
├── utils/
│   ├── network_utils.py
│   ├── validators.py
│   └── logger.py
│
├── tests/
├── screenshots/
└── reports/
```
## Usage

After starting the toolkit, a central menu is displayed.

The user selects a module by entering its corresponding number and provides the required inputs.

The toolkit validates user input and displays the result or an appropriate error message.

## Lab Environment

Testing should be performed only in an isolated and authorized cybersecurity laboratory environment.

Recommended environments include:

- Virtual machines
- Controlled test systems
- Authorized private networks

## Limitations

Some potentially disruptive or traffic-interception features are implemented as safe demonstrations in this version.

Live packet manipulation, DNS interception, network jamming, and ARP spoofing operations are disabled in the demonstration modules.

The toolkit is intended for educational and authorized security-testing purposes.

## Responsible Use

This toolkit must only be used on systems, networks, and virtual machines for which explicit permission has been obtained.

Do not use the toolkit against public networks, production systems, or devices belonging to other users.

Users should restore any network configuration changes after authorized testing.

## Credits

This project was developed as an educational cybersecurity integration project based on the security-testing exercises provided during the bootcamp.
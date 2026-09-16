import ipaddress


def validate_ip(ip_address):
    """Validate an IPv4 address."""
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False


def start_dns_demo(target_ip, spoof_ip, interface):
    """
    Start a safe DNS spoofing demonstration.

    No live DNS packets are intercepted or modified.
    """

    if not validate_ip(target_ip):
        raise ValueError("Invalid target IP address.")

    if not validate_ip(spoof_ip):
        raise ValueError("Invalid spoof IP address.")

    if not interface:
        raise ValueError("Network interface cannot be empty.")

    print("\n[*] DNS Spoofing Demo")
    print(f"[*] Target IP : {target_ip}")
    print(f"[*] Spoof IP  : {spoof_ip}")
    print(f"[*] Interface : {interface}")

    print("[*] Input validation successful.")
    print("[!] Live DNS interception/modification is disabled in this demo.")
    print("[+] Safe demonstration completed.")

    return True
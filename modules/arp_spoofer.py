def validate_inputs(target_ip, gateway_ip, interface):
    """Validate the required ARP spoofing demonstration inputs."""

    if not target_ip:
        raise ValueError("Target IP cannot be empty.")

    if not gateway_ip:
        raise ValueError("Gateway IP cannot be empty.")

    if not interface:
        raise ValueError("Network interface cannot be empty.")

    return True


def start_demo(target_ip, gateway_ip, interface):
    """
    Start a safe ARP spoofing demonstration.

    This version does not transmit ARP spoofing packets.
    """

    validate_inputs(target_ip, gateway_ip, interface)

    print("\n[*] ARP Spoofing Demo")
    print(f"[*] Target IP : {target_ip}")
    print(f"[*] Gateway IP: {gateway_ip}")
    print(f"[*] Interface : {interface}")

    print("[*] Input validation successful.")
    print("[!] Live ARP spoofing is disabled in this demo.")
    print("[+] Safe demonstration completed.")

    return True
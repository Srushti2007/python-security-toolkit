def start_jammer_demo(interface, packet_limit=5):
    """
    Start a safe Network Queue demonstration.

    No packets are blocked, dropped, or modified.
    """

    if not interface:
        raise ValueError("Network interface cannot be empty.")

    if packet_limit <= 0:
        raise ValueError("Packet limit must be greater than zero.")

    print("\n[*] Network Queue Demo")
    print(f"[*] Interface: {interface}")
    print(f"[*] Packet limit: {packet_limit}")

    print("[*] Input validation successful.")
    print("[!] Live packet blocking/jamming is disabled in this demo.")
    print("[+] Safe demonstration completed.")

    return True
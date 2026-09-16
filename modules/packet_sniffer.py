def start_sniffer(interface, packet_count=5):
    """
    Start a safe packet-sniffer demonstration.

    No live packet capture is performed in this demo.
    """

    if not interface:
        raise ValueError("Network interface cannot be empty.")

    if packet_count <= 0:
        raise ValueError("Packet count must be greater than zero.")

    print("\n[*] Packet Sniffer Demo")
    print(f"[*] Interface: {interface}")
    print(f"[*] Packet limit: {packet_count}")

    print("[*] Input validation successful.")
    print("[!] Live packet capture is disabled in this demo.")
    print("[+] Safe demonstration completed.")

    return True
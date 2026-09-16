def detect_arp_anomaly(observations):
    """
    Detect conflicting MAC addresses for the same IP address.

    observations should be a list of dictionaries:
    [
        {"ip": "192.168.1.1", "mac": "AA:BB:CC:DD:EE:FF"},
        ...
    ]
    """

    if not isinstance(observations, list):
        raise ValueError("Observations must be provided as a list.")

    ip_to_mac = {}
    alerts = []

    for observation in observations:
        if not isinstance(observation, dict):
            continue

        ip_address = observation.get("ip")
        mac_address = observation.get("mac")

        if not ip_address or not mac_address:
            continue

        if ip_address in ip_to_mac:
            if ip_to_mac[ip_address] != mac_address:
                alerts.append({
                    "ip": ip_address,
                    "previous_mac": ip_to_mac[ip_address],
                    "new_mac": mac_address
                })
        else:
            ip_to_mac[ip_address] = mac_address

    return alerts


def display_alerts(alerts):
    """Display detected ARP anomalies."""

    if not alerts:
        print("[+] No conflicting ARP entries detected.")
        return

    print("\n[!] Possible ARP spoofing indicators:")
    print("-" * 55)

    for alert in alerts:
        print(f"IP Address : {alert['ip']}")
        print(f"Previous MAC: {alert['previous_mac']}")
        print(f"New MAC     : {alert['new_mac']}")
        print("-" * 55)

    print(f"[!] {len(alerts)} anomaly/anomalies detected.")
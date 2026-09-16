import ipaddress
import scapy.all as scapy

from utils.network_utils import print_status

def validate_target(target):
    """Validate an IP address or network range."""
    try:
        ipaddress.ip_network(target, strict=False)
        return True
    except ValueError:
        return False


def scan(target):
    """Scan an authorized local network using ARP."""

    if not validate_target(target):
        raise ValueError("Invalid IP address or network range.")

    print_status(f"Scanning target: {target}")
    print_status("Sending ARP requests...")

    try:
        arp_request = scapy.ARP(pdst=target)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request

        answered = scapy.srp(
            arp_request_broadcast,
            timeout=2,
            verbose=False
        )[0]

        results = []

        for _, received in answered:
            results.append({
                "ip": received.psrc,
                "mac": received.hwsrc
            })

        return results

    except PermissionError:
        raise PermissionError(
            "Permission denied. Run the toolkit with the required privileges."
        )

    except Exception as error:
        raise RuntimeError(f"Network scan failed: {error}")


def display_results(results):
    """Display scan results in a readable format."""

    if not results:
        print("[!] No devices were discovered.")
        return

    print(f"{'IP Address':<20}{'MAC Address'}")
    print("-" * 40)

    for device in results:
        print(f"{device['ip']:<20}{device['mac']}")

    print(f"\n[+] Scan completed. {len(results)} device(s) discovered.")
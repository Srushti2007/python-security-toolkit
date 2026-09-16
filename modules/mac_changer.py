from utils.validators import is_valid_mac


def change_mac(interface, new_mac):
    """
    Validate MAC address and prepare a MAC-change request.

    Actual adapter modification is intentionally not performed here.
    """
    if not interface:
        raise ValueError("Interface name cannot be empty.")

    if not is_valid_mac(new_mac):
        raise ValueError("Invalid MAC address format.")

    print(f"\n[*] Interface: {interface}")
    print(f"[*] Requested MAC address: {new_mac}")
    print("[*] MAC change request validated.")
    print("[!] Actual adapter modification is disabled in this demo.")

    return True
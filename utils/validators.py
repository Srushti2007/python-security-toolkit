import re


def is_valid_mac(mac):
    """Return True if the supplied value is a valid MAC address."""
    pattern = r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"
    return re.match(pattern, mac) is not None
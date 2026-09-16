from utils.logger import log
from modules.arp_spoof_detector import detect_arp_anomaly, display_alerts
from modules.dns_spoofer import start_dns_demo
from modules.network_jammer import start_jammer_demo
from modules.packet_sniffer import start_sniffer
from modules.arp_spoofer import start_demo
from modules.mac_changer import change_mac
from modules.network_scanner import scan, display_results

def display_banner():
    print("\n" + "=" * 55)
    print("          PYTHON SECURITY TOOLKIT")
    print("       Integrated Ethical Hacking Framework")
    print("=" * 55)


def display_menu():
    print("\n" + "=" * 60)
    print("                    MODULE MENU")
    print("=" * 60)

    print("[1]  MAC Address Changer")
    print("[2]  Network Scanner")
    print("[3]  ARP Spoofing Demo")
    print("[4]  Packet Sniffer")
    print("[5]  Network Queue Demo")
    print("[6]  DNS Spoofing Demo")
    print("[7]  ARP Spoof Detector")
    print("[8]  Exit")

    print("=" * 60)


def main():
    display_banner()
    log("Python Security Toolkit started")

    while True:
        display_menu()

        choice = input("Select an option: ").strip()

        if choice == "1":
            print("\n[INFO] MAC Address Changer selected.")

            interface = input("Enter network interface name: ").strip()
            new_mac = input("Enter new MAC address: ").strip()

            try:
                change_mac(interface, new_mac)

            except ValueError as error:
                print(f"\n[ERROR] {error}")


        elif choice == "2":

            print("\n[INFO] Network Scanner selected.")

            target = input(

                "Enter the authorized target IP or network range: "

            ).strip()

            try:

                results = scan(target)

                display_results(results)


            except ValueError as error:

                print(f"\n[ERROR] {error}")


            except PermissionError as error:

                print(f"\n[ERROR] {error}")


            except RuntimeError as error:

                print(f"\n[ERROR] {error}")


        elif choice == "3":

            print("\n[INFO] ARP Spoofing Demo selected.")

            target_ip = input("Enter authorized target IP: ").strip()

            gateway_ip = input("Enter gateway IP: ").strip()

            interface = input("Enter network interface name: ").strip()

            try:

                start_demo(target_ip, gateway_ip, interface)


            except ValueError as error:

                print(f"\n[ERROR] {error}")


        elif choice == "4":

            print("\n[INFO] Packet Sniffer selected.")

            interface = input("Enter network interface name: ").strip()

            packet_count_input = input(

                "Enter packet count for the demo: "

            ).strip()

            try:

                packet_count = int(packet_count_input)

                start_sniffer(

                    interface,

                    packet_count

                )


            except ValueError as error:

                print(f"\n[ERROR] {error}")

        elif choice == "5":
                print("\n[INFO] Network Queue Demo selected.")

                interface = input("Enter network interface name: ").strip()

                packet_limit_input = input(
                    "Enter packet limit for the demo: "
                ).strip()

                try:
                    packet_limit = int(packet_limit_input)

                    start_jammer_demo(
                        interface,
                        packet_limit
                    )

                except ValueError as error:
                    print(f"\n[ERROR] {error}")


        elif choice == "6":

            print("\n[INFO] DNS Spoofing Demo selected.")

            target_ip = input("Enter authorized target IP: ").strip()

            spoof_ip = input("Enter demonstration spoof IP: ").strip()

            interface = input("Enter network interface name: ").strip()

            try:

                start_dns_demo(

                    target_ip,

                    spoof_ip,

                    interface

                )


            except ValueError as error:

                print(f"\n[ERROR] {error}")


        elif choice == "7":

            print("\n[INFO] ARP Spoof Detector selected.")

            observations = [

                {

                    "ip": "192.168.1.1",

                    "mac": "AA:BB:CC:DD:EE:FF"

                },

                {

                    "ip": "192.168.1.10",

                    "mac": "11:22:33:44:55:66"

                },

                {

                    "ip": "192.168.1.1",

                    "mac": "11:AA:22:BB:33:CC"

                }

            ]

            try:

                alerts = detect_arp_anomaly(observations)

                display_alerts(alerts)


            except ValueError as error:

                print(f"\n[ERROR] {error}")

        elif choice == "8":
            print("\n[+] Exiting Python Security Toolkit.")
            break

        else:
            print("\n[ERROR] Invalid option. Please select 1-8.")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\n\n[!] Toolkit interrupted by user.")

    except Exception as error:
        print(f"\n[ERROR] Unexpected error: {error}")
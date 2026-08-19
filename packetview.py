#!/usr/bin/env python3
"""PacketView - local network and system information tool."""

import datetime
import os
import platform
import socket
import subprocess


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def local_info():
    hostname = socket.gethostname()
    try:
        ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip = "Unavailable"

    print("\n=== LOCAL NETWORK ===")
    print(f"Hostname : {hostname}")
    print(f"Local IP : {ip}")
    print(f"Platform : {platform.system()} {platform.release()}")
    print(f"Python   : {platform.python_version()}")


def interfaces():
    print("\n=== NETWORK INTERFACES ===")
    try:
        result = subprocess.run(
            ["ip", "-brief", "address"],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.stdout.strip():
            print(result.stdout)
        else:
            print("No interface information available.")
    except FileNotFoundError:
        print("The 'ip' command is not available on this system.")


def stats():
    print("\n=== CONNECTION ===")
    print(f"Checked: {datetime.datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S %Z')}")
    try:
        socket.create_connection(("1.1.1.1", 53), timeout=2).close()
        print("Internet connectivity: reachable")
    except OSError:
        print("Internet connectivity: unavailable")


def menu():
    while True:
        clear()
        print("╔══════════════════════════════════╗")
        print("║          PACKETVIEW v0.1         ║")
        print("╠══════════════════════════════════╣")
        print("║ [1] My Network                   ║")
        print("║ [2] Network Interfaces           ║")
        print("║ [3] Connection Statistics        ║")
        print("║ [0] Exit                         ║")
        print("╚══════════════════════════════════╝")

        choice = input("\nPacketView > ").strip()

        if choice == "1":
            local_info()
        elif choice == "2":
            interfaces()
        elif choice == "3":
            stats()
        elif choice == "0":
            print("Shutting down PacketView.")
            break
        else:
            print("Unknown option.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    menu()

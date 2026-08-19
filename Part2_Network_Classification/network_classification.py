# Network Device and Transmission Media Classification

devices = {
    "switch": {
        "layer": "Layer 2 - Data Link",
        "function": "Connects devices within a LAN and forwards data using MAC addresses."
    },
    "router": {
        "layer": "Layer 3 - Network",
        "function": "Connects different networks and forwards packets using IP addresses."
    },
    "bridge": {
        "layer": "Layer 2 - Data Link",
        "function": "Connects and filters traffic between two LAN segments."
    },
    "access point": {
        "layer": "Layer 2 - Data Link",
        "function": "Provides wireless connectivity between Wi-Fi devices and a wired network."
    }
}

media = {
    "twisted pair": {
        "type": "Wired",
        "function": "Used for Ethernet and LAN connections."
    },
    "coaxial cable": {
        "type": "Wired",
        "function": "Used for cable television, broadband and data transmission."
    },
    "fiber optic": {
        "type": "Wired",
        "function": "Provides high-speed data transmission over long distances using light."
    },
    "wireless/radio": {
        "type": "Wireless",
        "function": "Uses radio waves for wireless communication such as Wi-Fi."
    }
}

print("=" * 70)
print("       NETWORK DEVICE CLASSIFICATION REPORT")
print("=" * 70)

print("\nNETWORK DEVICES")
print("-" * 70)

for device, details in devices.items():
    print(f"\nDevice: {device.title()}")
    print(f"OSI Layer: {details['layer']}")
    print(f"Primary Function: {details['function']}")

print("\n" + "=" * 70)
print("       TRANSMISSION MEDIA CLASSIFICATION")
print("=" * 70)

for medium, details in media.items():
    print(f"\nMedia: {medium.title()}")
    print(f"Type: {details['type']}")
    print(f"Primary Function: {details['function']}")

print("\n" + "=" * 70)
print("Classification report generated successfully.")
print("=" * 70)
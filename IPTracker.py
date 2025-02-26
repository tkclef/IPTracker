import socket

#Command to Identify an IP Address.

def get_my_ip():
    """ Function to retrieve the local IP address of the system """
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_ip
    except:
        return None


def track_ip(ip_address):
    """ Function to track and display information about an IP address """
    try:
        host_name = socket.gethostbyaddr(ip_address)
        print(f"Hostname: {host_name[0]}")
        print(f"IP Address: {ip_address}")
        # Additional information retrieval can be added here, like geolocation, ISP, etc.
    except socket.herror:
        print("Hostname could not be found.")
    except socket.gaierror:
        print("Invalid IP address format.")


if __name__ == "__main__":
    print("IP Tracker")
    print("1. Track your own IP")
    print("2. Track a specific IP")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        my_ip = get_my_ip()
        if my_ip:
            print(f"Your IP address: {my_ip}")
            track_ip(my_ip)
        else:
            print("Failed to retrieve your IP address.")
    elif choice == "2":
        ip_to_track = input("Enter the IP address to track: ")
        track_ip(ip_to_track)
    else:
        print("Invalid choice. Please enter '1' or '2'.")

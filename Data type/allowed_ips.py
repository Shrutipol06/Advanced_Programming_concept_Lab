# Server configuration

server_ip = ("192.168.1.10", 8080)

allowed_ips = ["192.168.1.1", "192.168.1.2"]


# Function to update allowed IPs
def update_allowed_ips():
    ip = input("Enter new IP address to allow: ")

    allowed_ips.append(ip)

    print("IP address added successfully.")


# Function to display configuration
def display_configuration():
    print("\n--- Server Configuration ---")
    print("Server IP:", server_ip)
    print("Allowed IPs:", allowed_ips)


# Display original configuration
display_configuration()

# Update allowed IPs
update_allowed_ips()

# Display updated configuration
display_configuration()

# Trying to change server_ip
print("\nServer IP is stored as a tuple and cannot be changed.")
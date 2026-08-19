import socket

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server IP address and port number
HOST = "127.0.0.1"
PORT = 5000

# Connect to the server
client_socket.connect((HOST, PORT))

print("Connected to server.")

# Take a message from the user
message = input("Enter message: ")

# Send message to server
client_socket.send(message.encode())

print("Message sent successfully.")

# Receive response from server
response = client_socket.recv(1024).decode()

print("Server response:", response)

# Close connection
client_socket.close()

print("Client closed.")
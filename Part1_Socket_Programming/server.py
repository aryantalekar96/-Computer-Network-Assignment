import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP address and port number
HOST = "127.0.0.1"
PORT = 5000

# Bind the socket to the IP address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

print("Server started...")
print("Waiting for client connection...")

# Accept a client connection
client_socket, client_address = server_socket.accept()

print("Client connected.")

# Receive message from client
message = client_socket.recv(1024).decode()

print("Message received from client:", message)

# Send response to client
response = "Message received successfully!"
client_socket.send(response.encode())

print("Response sent to client.")

# Close connections
client_socket.close()
server_socket.close()

print("Server closed.")
import socket

# Server address and port
serverName = 'localhost'  # Change this to the server's IP if not running locally
serverPort = 7777

# Create a UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Sending a message to the server
message = input('Enter a message to send to the server: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))

# Receiving a response from the server
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print('From Server:', modifiedMessage.decode())

# Closing the socket
clientSocket.close()

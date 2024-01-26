import socket
import sys

# Server settings
serverPort = 7777
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Binding the server socket to the specified port
try:
    serverSocket.bind(('', serverPort))
    print(f"Server is listening on port {serverPort}")
except OSError as e:
    print(f"Error: Unable to bind to port {serverPort}: {e}")
    sys.exit(1)

# Server main loop
try:
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        modifiedMessage = message.decode().upper()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
except KeyboardInterrupt:
    print("\nServer is shutting down.")
finally:
    serverSocket.close()

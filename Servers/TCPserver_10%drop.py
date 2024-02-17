from socket import *
import sys
import random

serverName = '127.0.0.1'
serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)

try:
    serverSocket.bind((serverName, serverPort))
except OSError as e:
    print(f"Server failed to bind on port {serverPort}: {e}")
    sys.exit(1)

serverSocket.listen(1)
print('The server is listening')

try:
    while True:
        connectionSocket, addr = serverSocket.accept()
        print(f"Connection from {addr}")
        connectionOpen = True

        while connectionOpen:
            try:
                sentence = connectionSocket.recv(1024).decode()
                if not sentence or sentence.lower() == 'quit':
                    connectionOpen = False
                    break

                if random.randint(1, 10) <= 1:  # 10% chance of drop
                    print("A message was dropped")
                    continue

                capitalizedSentence = sentence.upper()
                connectionSocket.send(capitalizedSentence.encode())
            except IOError as e:
                print(f"IOError: {e}")
                connectionOpen = False

finally:
    serverSocket.close()

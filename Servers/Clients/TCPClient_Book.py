from socket import *

serverName = 'localhost'  # Change this to the server's IP if not running locally
serverPort = 12000

try:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    sentence = input('Input lowercase sentence:')
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)

    print('From Server: ', modifiedSentence.decode())
except ConnectionRefusedError:
    print(f"Could not connect to server {serverName} on port {serverPort}")
finally:
    clientSocket.close()

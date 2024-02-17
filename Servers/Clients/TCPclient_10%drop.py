from socket import *

serverName = '127.0.0.1'
serverPort = 5000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(5)  # Set to 5 seconds

try:
    clientSocket.connect((serverName, serverPort))

    while True:
        sentence = input('Input lowercase sentence or "quit" to exit: ')
        clientSocket.send(sentence.encode())

        if sentence.lower() == 'quit':
            break

        try:
            modifiedSentence = clientSocket.recv(1024)
            print('From Server:', modifiedSentence.decode())
        except timeout:
            print(f"Message dropped or server did not respond: {sentence}")

except ConnectionRefusedError:
    print(f"Could not connect to server {serverName} on port {serverPort}")
finally:
    clientSocket.close()

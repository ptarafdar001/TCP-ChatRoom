import socket
import threading

host = socket.gethostbyname(socket.gethostname())
port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
fullNames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = fullNames[index]
            broadcast(f'{name} left the chat!'.encode('ascii'))
            fullNames.remove(name)
            break


def receive():
    while True:
        client, addr = server.accept()
        print(f"connected with--{str(addr)}")

        client.send('NICK'.encode('ascii'))
        name = client.recv(1024).decode('ascii')
        fullNames.append(name)
        clients.append(client)

        print(f" Name of the client is: {name}")
        broadcast(f"{name} jioned the chat!".encode('ascii'))
        client.send('You are connected.Start chating '.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server is running...")
receive()

import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.0.6', 5000))

name = input("Enter your name: ")


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(name.encode('ascii'))
            else:
                print(message)
        except:
            print("[Error] Our team is working to fix it")
            client.close()
            break


def write():
    while True:
        message = f"{name}: {input()}"
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

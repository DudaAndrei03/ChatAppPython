import socket

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPV4, TCP
    client.connect(("localhost", 12345))

    print(client.recv(1024))
    client.sendall(b'Sunt aici!')

    client.close()



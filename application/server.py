import socket
import threading
import signal
import sys

def handle_client(client_socket, client_address):
    client_socket.sendall(b'Te-ai conectat cu succes!')

    data = client_socket.recv(1024)
    print(f"{client_address}: {data}")

    client_socket.close()


def signal_handler(sig, frame):
    print("\n Server oprit manual.")
    server.close()
    sys.exit(0)


if __name__ == "__main__":
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPV4, TCP
        print("Socket-ul s-a creat cu succes.")
    except socket.error as err:
        print("Socket-ul nu a fost creat corespunzator %s" %(err))

    server.bind(("localhost", 12345))
    server.listen(5)

    signal.signal(signal.SIGINT, signal_handler)


    while True:
        try:
            client_socket, client_address = server.accept()
            print(f"Conectiune de la :{client_address}")

            client_thread = threading.Thread(target=handle_client, args = (client_socket,client_address))
            client_thread.daemon = True
            client_thread.start()

        except KeyboardInterrupt:
            print("\nServer oprit manual.")
            server.close()
            break
        except socket.error as e:
            print(f"Eroare la acceptarea clientului: {e}")


import socket
import threading

SERVER = "127.0.0.1"
PORT = 5050


def receive_messages(sock):

    while True:
        try:
            msg = sock.recv(1024).decode()

            if not msg:
                break

            print(msg)

        except:
            break


def send_messages(sock):

    while True:

        text = input()

        if text == "/exit":
            sock.send("/exit".encode())
            sock.close()
            break

        try:
            sock.send(text.encode())
        except:
            break


def start_client():

    username = input("Choose username: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((SERVER, PORT))

    client.send(username.encode())

    print("Connected to chat server")
    print("Commands: /list , /exit")

    receive_thread = threading.Thread(
        target=receive_messages,
        args=(client,)
    )

    send_thread = threading.Thread(
        target=send_messages,
        args=(client,)
    )

    receive_thread.start()
    send_thread.start()


if __name__ == "__main__":
    start_client()
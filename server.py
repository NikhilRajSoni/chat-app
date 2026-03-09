import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5050

LOG_FILE = "server_log.txt"

clients = []
usernames = {}

lock = threading.Lock()


def get_time():
    return datetime.now().strftime("%H:%M")


def log_message(text):
    with open(LOG_FILE, "a") as f:
        f.write(text + "\n")


def broadcast_message(message, sender=None):
    with lock:
        for client in clients:
            if client != sender:
                try:
                    client.send(message.encode())
                except:
                    remove_client(client)


def remove_client(client):
    with lock:
        name = usernames.get(client, "Unknown")

        if client in clients:
            clients.remove(client)

        if client in usernames:
            del usernames[client]

    client.close()

    leave_msg = f"{name} disconnected"
    broadcast_message(leave_msg)
    log_message(leave_msg)


def list_users(client):
    with lock:
        users = ", ".join(usernames.values())

    client.send(f"Active users: {users}".encode())


def handle_client(client):

    try:
        name = client.recv(1024).decode().strip()

        with lock:
            clients.append(client)
            usernames[client] = name

        join_msg = f"{name} entered the chat"
        print(join_msg)

        broadcast_message(join_msg)
        log_message(join_msg)

        while True:
            data = client.recv(1024)

            if not data:
                break

            text = data.decode().strip()

            if text == "/exit":
                break

            if text == "/list":
                list_users(client)
                continue

            formatted = f"({name}) -> {text}"

            print(formatted)

            broadcast_message(formatted, sender=client)
            log_message(formatted)

    except:
        pass

    finally:
        remove_client(client)


def start_chat_server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen()

    print(f"Chat server running on {HOST}:{PORT}")

    while True:
        client, addr = server.accept()

        thread = threading.Thread(
            target=handle_client,
            args=(client,)
        )

        thread.start()


if __name__ == "__main__":
    start_chat_server()
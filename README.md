# Socket Based Chat Program

## Overview

This project implements a simple **terminal-based group chat system** using Python and TCP sockets.
A single server manages multiple clients and allows them to share messages over a network connection.

Each connected client chooses a username and can send messages that are delivered to all other active users.

The goal of the project is to demonstrate key networking concepts including:

* TCP socket communication
* multi-client server design
* thread-based concurrency
* command-based interaction between clients and server

---

## How the System Works

The system follows a **centralized server model**.

1. A server process listens for incoming TCP connections.
2. When a new user connects, the server creates a **separate thread** to manage that user.
3. Messages received from a client are distributed to all other connected clients.

## Message Format

When a client sends a message, the server formats it before sending it to others.

Example:

```
(pankaj) -> hi
(nikhil raj) -> hlo pankaj
```

This indicates the sender's username followed by the message content.

---

## Supported Commands

The chat client supports a few simple commands.

| Command | Purpose                           |
| ------- | --------------------------------- |
| `/list` | Display currently connected users |
| `/exit` | Leave the chat session            |

Example usage:

```
/list
Active users: nikhil raj, pankaj
```

---

## Files in the Project

```
chat-app/
│
├── server.py
├── client.py
├── server_log.txt   # Log file storing chat activities, etc.
└── README.md
```

---

## Running the Chat System

### 1. Start the Server

Run the following command in a terminal:

```
python3 server.py
```

We will see a message indicating that the server is running.

---

### 2. Start a Client

Open another terminal and run:

```
python3 client.py
```

Enter a username when prompted.

Example:

```
Choose username: Pankaj (for example)
```

---

### 3. Chat With Other Users

After connecting, users can type messages which will be visible to all other participants.

Example session:

```
(pankaj) -> Hi
(nikhil raj) -> Hello
```

Commands such as `/list` and `/exit` can be used during the chat.

---

## Server Logging

The server keeps a record of chat activity in:

```
server_log.txt
```

The log may include:

* user join messages
* chat messages
* user disconnection events

This file helps track server activity and debugging.

---

## Conclusion

This project explains how a basic multi-user chat application can be implemented using TCP sockets and threads. The server coordinates communication between clients and ensures messages are distributed efficiently among participants.

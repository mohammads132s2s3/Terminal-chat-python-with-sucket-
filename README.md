 #💬 Terminal Chat App (Python Socket Programming)

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)



A simple terminal-based chat app using sockets in Python.  
Real-time messaging between multiple clients and a central server — all via your terminal.

---


## ⚙️ Requirements

- Python 3.6 or higher
- Works on Windows, Linux, or macOS

---

## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/your-username/terminal-chat.git
cd terminal-chat

2. Start the Server

python server.py

This will start the chat server on 0.0.0.0:50505.

3. Start a Client

In a separate terminal window:

python client.py

You can start multiple clients this way.

> 💡 If the server is on a different computer, replace 127.0.0.1 in client.py with the server’s IP address.




---

🧠 How It Works

The server listens for incoming connections using Python sockets.

Each client that connects is handled in a separate thread.

Messages from one client are broadcast to all other connected clients.

Each client runs two threads:

One for receiving messages

One for sending messages




---


🛠 Features

✅ Real-time messaging

✅ Support for multiple clients

✅ Broadcasting messages

✅ Threaded server and client

✅ Terminal interface (no GUI)



---

🧪 Troubleshooting

❗ Port Already in Use (WinError 10048)

Another process is using port 50505. Use the following commands to free it:

netstat -ano | findstr :50505
taskkill /PID <PID> /F

Or simply change the port number in both server.py and client.py.

❗ Connection Refused (WinError 10061)

Make sure the server is running before starting the client, and IP/port is correct.


---

🔧 Customization

Change Port or IP

Edit these lines:

In server.py:

s.bind(("0.0.0.0", 50505))

In client.py:

client.connect(("127.0.0.1", 50505))

Change 50505 to any available port number.


---

✍️ Author

Made with ❤️ by [Your Name]
GitHub: https://github.com/mohammads132s2s3

---

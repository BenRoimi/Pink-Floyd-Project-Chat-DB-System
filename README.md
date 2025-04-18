# 🎵 Pink Floyd Server

This project is a client-server application in Python that lets users explore albums, songs, lyrics, and trivia related to the legendary rock band **Pink Floyd**. It uses TCP sockets for communication and includes authentication, a structured query system, and file-based data storage.

---

## 🧩 Features

- 🔒 **Password authentication** with SHA-256 hash
- 🎧 **Query options** for albums, songs, lyrics, and keyword-based search
- 🗂️ **Structured song data** stored in a custom `.txt` database
- 🔌 **Client-server communication** over TCP with a custom mini-protocol
- 💬 Interactive terminal UI

---

## 🛠 Technologies

- Python 3.x
- `socket` – low-level network communication
- `hashlib` – for secure password hashing
- File I/O for database simulation

---

## 📁 Project Structure

```bash
PinkFloydTrivia/
├── client.py         # Client-side app, handles input/output and communication
├── server.py         # Server-side app, handles logic, queries, and communication
├── data.py           # Data processing module (loading, searching, responding)
├── Pink_Floyd_DB.txt # Text-based storage file (not uploaded here)
└── README.md

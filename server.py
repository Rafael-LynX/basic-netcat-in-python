# Server
import socket
import json

### Specify Host and Port
HOST = "127.0.0.1"
PORT = 5789

### Creation socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    ### Binding
    server.bind((HOST, PORT))
    server.listen(1)

    print(f"Waiting for connection to the client {HOST}:{PORT}...")
    ### Accept
    conn, addr = server.accept()

    with conn:
        print(f"Connecting: {addr}")

        ### Makefile
        with conn.makefile("r", encoding="utf-8") as entry:
            while True:
                ### Command
                command = input("lab> ").strip()

                if not command:
                    continue

                ## Order
                order = json.dumps({"command": command}) + "\n"
                conn.sendall(order.encode("utf-8"))

                line = entry.readline()

                if line == "":
                    print("The client closed the connection.")
                    break

                response = json.loads(line)

                if response["exit"]:
                    print(response["exit"], end="")
                    if not response["exit"].endswith("\n"):
                        print()

                print(f"[code de saída: {response['code']}]")

                if command == "exit":
                    break

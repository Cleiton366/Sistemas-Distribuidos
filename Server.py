import socket
import threading

HEADER = 64
PORT = 3000
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!Disconnect"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)


def handle_client(connection, address):
    print(f"[NEW CONNECTION] {address} connected.")

    connected = True
    while connected:
        operation_type = connection.recv(HEADER).decode(FORMAT)
        n1 = connection.recv(HEADER).decode(FORMAT)
        n2 = connection.recv(HEADER).decode(FORMAT)
        send_message(connection, operation_type, n1, n2)
    connection.close()

def send_message(client, operation_type, n1, n2):
    result = 0
    match operation_type:
        case "Sum":
            result = n1+n2
            res = "Response: "+result
            data = res.encode(FORMAT)
            client.send(data)
        case "Sub":
            result = n1-n2
            res = "Response: "+result
            data = res.encode(FORMAT)
            client.send(data)
        case "Mult":
            result = n1*n2
            res = "Response: "+result
            data = res.encode(FORMAT)
            client.send(data)
        case "Div":
            result = n1/n2
            res = "Response: "+result
            data = res.encode(FORMAT)
            client.send(data)

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()
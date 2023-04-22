import socket
import threading

HEADER = 64
PORT = 3000
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!Disconnect"
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
USER_NAME = ""

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

def send(operation_type, n1, n2):
    operation_type = operation_type.encode(FORMAT)
    n1 = n1.encode(FORMAT)
    n2 = n2.encode(FORMAT)
    client.send(operation_type)
    client.send(n1)
    client.send(n2)

def handle_messages():
    while True:
        data = client.recv(HEADER).decode(FORMAT)
        print(data)

def start():
    thread = threading.Thread(target=handle_messages)
    thread.start()

    n1 = 0
    n2 = 0

    connected = True
    while connected:
        print("Remote Calculator")
        print("Choose an operation:")
        print("1 - Sum")
        print("2 - Sub")
        print("3 - Mult")
        print("4 - Div")
        print("5 - Disconnect")
        op = input()
        
        print("Type n1:")
        n1 = input()
        print("Type n2:")
        n2 = input()
        
        match op:
            case 1:
                print(f"Request: {n1}+{n2}")
                send("Sum", n1, n2)
            case 2:
                print(f"Request: {n1}-{n2}")
                send("Sub", n1, n2)
            case 3:
                print(f"Request: {n1}*{n2}")
                send("Mult", n1, n2)
            case 4:
                print(f"Request: {n1}/{n2}")
                send("Div", n1, n2)
            case 5:
                send(DISCONNECT_MESSAGE)
                connected = False
                client.close()

start()
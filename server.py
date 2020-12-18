import socket
import threading 
import pickle # this is used for object transfer

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) # this will get my local IP address
ADDR = (SERVER, PORT) # address we will bind our socket to
HEADER = 64 # this will be the first message received from the client that will tell us how big our message is
FORMAT = 'utf-8' # we will decode our received messages from byte form to a string with this format
DISC_MSG = "!DISCONNECT" # disconnect message we can receive from the client

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # this creates our socket connection. we are using an internet connection, streaming data
server.bind(ADDR)   # bound the socket to this address. whenever a client connects to the address it will hit our socket

def handle_client(conn, addr, player):
    global threadCount
    threadCount = 1

    print("[NEW CONNECTION] ", addr, " connected.")

    connected = True
    while connected:
        # here we will want to receive data and transfer data from one game to another
        pass

    conn.close()    # this will close our connection with the client safely

def start():
    server.listen() # have server start listening for clients
    print("[LISTENING] Server is listening on", SERVER)

    while True:
        conn, addr = server.accept() # this line waits for a new connection to the server. conn gets connection, addr gets where connection came from
        if threading.activeCount()-1 == 0:
            thread = threading.Thread(target=handle_client, args=(conn, addr, 0))   # we create a new thread
        else:
            thread = threading.Thread(target=handle_client, args=(conn, addr, threadCount))   # we create a new thread

        thread.start()  # start the thread
        print("[ACTIVE CONNECTIONS]", threading.activeCount()-1) # print how many active connections we have currently

print("[STARTING] server is starting...")
start()
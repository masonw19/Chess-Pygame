import socket
import threading 
import pickle # this is used for object transfer

from board import Board

PORT = 5050
SERVER = "localhost" # IPv4 address goes here. To find IPv4 address go to command prompt and enter 'ipconfig/all'
ADDR = (SERVER, PORT) # address we will bind our socket to
DISC_MSG = "!DISCONNECT" # disconnect message we can receive from the client

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # this creates our socket connection. we are using an internet connection, streaming data
server.bind(ADDR)   # bound the socket to this address. whenever a client connects to the address it will hit our socket

board = [Board(True), Board(False)]    # game boards


# acknowledgment protocol
def ack(conn, addr, data):
    conn.send(data)
    
def handle_client(conn, addr, connection_num):
    global threadCount
    threadCount = 1
    print(connection_num)
    print("[NEW CONNECTION] ", addr, " connected.")

    ack(conn, addr, pickle.dumps(board[connection_num]))    # send the board object to the client

    connected = True
    while connected:
        data = conn.recv(int(4096*3)) # this line waits until we receive a message from the client
        if not data:
            pass
        else:
            data = pickle.loads(data) # this line waits until we receive a message from the client

            if connection_num == 0:
                board[1] = data
            else:
                board[0] = data
                    
            if data.disc:   # if the client has disconnected we have to do this to safely close connection
                connected = False   # leave the while loop
                board[connection_num].disc = False    # change the disc variable to be back to false for if the the user reconnects
                print("[DISCONNECTED]", addr)   # print message to screen
                if board == 0:                 # if the player to disconnect was player 0 we need to keep track of the thread
                    threadCount = 0
                if board == 1:                 # if the player to disconnect was player 1 we need to keep track of the thread
                    threadCount = 1
            else:
                if connection_num == 0:     # if player 1 sends us the data, we reply with player 0's data
                    reply = board[0]
                else:               # if player 0 sends us the data, we reply with player 1's data
                    reply = board[1]
                ack(conn, addr, pickle.dumps(reply))
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
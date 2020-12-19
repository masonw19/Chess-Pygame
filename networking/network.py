import socket
import pickle

# when we make a network class instance we connect to the server
class Network:
    def __init__(self):
        self.server = socket.gethostbyname(socket.gethostname())    # this will get our local ip address
        self.client = self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # this will create our socket connection
        self.port = 5050    # server port
        self.addr = (self.server, self.port)    # address we will bind our socket to
        self.header = 64
        self.format = 'utf-8'   # format to decode bytes to strings
        self.receive_object = self.connect()
    
    # acknowledgment protocol. receive data from the server. this method will wait for a response
    def ack(self):
        data_length = self.client.recv(self.header).decode(self.format) # get the size of the message we are receiving
        if data_length:
            return pickle.loads(self.client.recv(int(data_length)))    # receive an object and return it

    def getBoard(self):
        return self.receive_object  # return the players board

    # connection protocol
    def connect(self):
        try:
            self.client.connect(self.addr)  # make connection
            return self.ack()
        except:
            print("[ERROR] cannot make connection")

    # data transmission protocol
    def send(self, data):
        try:
            data = pickle.dumps(data)   # object we want to send to other client
            data_length = len(data)     # length of data
            data_length = str(data_length).encode(self.format)  # get the length of data
            data_length += b' ' * (self.header - len(data_length))  # fill out length to 64 bytes   
            self.client.send(data_length)   # send length
            self.client.send(data)    # send objects

            return self.ack()
        except socket.error as e:
            print(e)
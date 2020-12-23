import socket
import pickle

# when we make a network class instance we connect to the server
class Network:
    def __init__(self):
        self.server = "192.168.0.61"#socket.gethostbyname(socket.gethostname())    # this will get our local ip address
        self.client = self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # this will create our socket connection
        self.port = 5050    # server port
        self.addr = (self.server, self.port)    # address we will bind our socket to
        self.header = 64
        self.format = 'utf-8'   # format to decode bytes to strings
        self.receive_object = self.connect()
    
    # acknowledgment protocol. receive data from the server. this method will wait for a response
    def ack(self):
        data = self.client.recv(int(4096*3))
        if not data:        # check if we have received any data before unpickling
            return None
        else:
            return pickle.loads(data)    # receive an object and return it

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
            self.client.send(data)    # send objects

            return self.ack()

        except socket.error as e:
            print(e)
            print("Desktop")
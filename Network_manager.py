import socket
from threading import Thread

class Server_manager(Thread):
    def __init__(self):
        super(Server_manager, self).__init__()
        self.connexion_list = {}
        self.HOST = ''
        self.PORT = 1050
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.HOST, self.PORT))
    
    def start_listen(self):
        print("listenning")
        self.s.listen(1)
        self.wait_connexion()
    
    def wait_connexion(self):
        conn, addr = self.s.accept()
        connexion = [conn, addr]
        while True:
            data =conn.recv(1024)
            if not data:
                break
            name = data.decode('utf-8')
            self.connexion_list[name] = connexion
        print("Connected by {}".format(name))
        self.wait_connexion()
    
    def diconnect(self):
        pass
    
    def run(self):
        self.start_listen()
    

class Client_manager:
    def __init__(self, name):
        self.HOST = 'localhost'
        self.PORT = 1050
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.HOST, self.PORT))
        byte = name.encode('utf-8')
        self.s.send(byte)
        print("Connected")
        self.s.close()

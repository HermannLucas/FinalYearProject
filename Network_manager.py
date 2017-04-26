import socket
import socketserver

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        self.server.clients[data] = self.client_address
        response = bytes(self.server.name, 'ascii')
        self.request.sendall(response)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    clients ={}
    
    def send(self, client, order):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((client))
            sock.sendall(order)

class Client:
    
    def connect(self, ip, port, name):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((ip, port))
            sock.sendall(bytes(name, 'ascii'))
            response = str(sock.recv(1024), 'ascii')
            print("Connected to : {}".format(response))
            return sock.getsockname()

    def listen(self, ip, port):
        with socketserver.TCPServer((ip, port),  Client_TCP_handler) as server:
            server.serve_forever()
    
class Client_TCP_handler(socketserver.BaseRequestHandler):
    
    def handle(self):
        data = self.request.recv(1024)
        print(data)
        print("Got contacted from {}.".format(self.client_address[0]))
        print(data)
    
#    def __init__(self, ord_dir):
#        super(Reciever_manager, self).__init__()
#        self.ord_dir = ord_dir
#        self.connexion_list = {}
#        self.HOST = ''
#        self.PORT = 1050
#        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        self.s.bind((self.HOST, self.PORT))
#    
#    def start_listen(self):
#        print("listenning")
#        self.s.listen(1)
#        self.wait_connexion()
#    
#    def wait_connexion(self):
#        conn, addr = self.s.accept()
#        connexion = [conn, addr]
#        while True:
#            data = conn.recv(1024)
#            if not data:
#                break
#            name = data.decode('utf-8')
#            self.connexion_list[name] = connexion
#            print (self.connexion_list[name][0])
#        print("Connected by {}".format(name))
#        self.wait_connexion()
#    
#    def disconnect(self, connexion):
#        if connexion in self.connexion_list:
#            self.connexion_list[connexion][0].close
#    
#    def run(self):
#        self.start_listen()
#    
#
#class Sender_manager:
#    def __init__(self, name):
#        self.HOST = 'localhost'
#        self.PORT = 1050
#        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        self.s.connect((self.HOST, self.PORT))
#        self.send(name)
#        print("Connected")
#    
#    def send(self, message):
#        if type(message) is str:
#            byte = message.encode('utf-8')
#        else :
#            byte = message.encode()
#        self.s.send(byte)
#    
#    def diconnect(self):
#        self.s.close()

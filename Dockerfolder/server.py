import socket
import threading
from word_game import WordGame

class ClientThread(threading.Thread):

    stats = dict()

    def __init__(self, client_address, client_socket, identity):
        threading.Thread.__init__(self)
        self.c_socket = client_socket
        print("Connection no. " + str(identity))
        print("New connection added: ", client_address)

    def run(self):
        correct_guesses = 0
        game = WordGame()
        game.get_phrase()
        print(game.phrase, 'from client', clientAddress)
        print("Connection from : ", clientAddress)
        name = self.c_socket.recv(2048)
        if name in self.stats:
            correct_guesses = self.stats[name]
        while True:
            data = self.c_socket.recv(2048)
            if data.decode() == '/L':
                self.c_socket.send(bytes(str(self.stats), 'UTF-8'))
            if data.decode() == 'yes':
                game.delete_phrase()
                game.get_phrase()
                print(game.phrase, 'from client', clientAddress)
            if not data:
                break
            msg = data.decode()
            print(msg)
            game.guess_word(msg)
            print("from client", clientAddress, ": ", msg)
            output = ''.join(map(str, game.return_phrase()))
            if output == 'You Win!':
                correct_guesses = correct_guesses + 1
            self.c_socket.send(bytes(output, 'UTF-8'))
        print("Client at ", clientAddress, " disconnected...")
        self.stats[name] = correct_guesses
LOCALHOST = "0.0.0.0"
PORT = 64002

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))

print("Server started")
print("Waiting for client request..")


counter = 0


while True:
    server.listen(1)
    my_socket, clientAddress = server.accept()
    counter = counter + 1
    new_thread = ClientThread(clientAddress, my_socket, counter)
    new_thread.start()


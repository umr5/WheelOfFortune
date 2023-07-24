import socket


SERVER = "127.0.0.1"
PORT = 64002

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER, PORT))

print("Welcome to the Wheel of Fortune!\nTo start the game, you shall enter your name!\nEnter [/L] to Display the current leaderboard")
name = input("Enter your name: ")
response = 'Y'
data_to_send = name
sock.sendall(bytes(data_to_send, 'UTF-8'))
while response == 'Y':

    sock.sendall(bytes(data_to_send, 'UTF-8'))
    data = sock.recv(1024)
    print('Received', repr(data.decode()))

    if data == b'You Win!':
        play_again = input('Do u want to play again? [Y/N]')
        if play_again == 'N':
            response = 'N'
        else:
            print("Display a new phrase[yes/no]: ")
    if response == 'Y':
        data_to_send = input("Enter data: ")

sock.close()


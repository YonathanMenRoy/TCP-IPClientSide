import socket, threading, json

HEADER = 64
PORT = 4840
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# Whatever IP address you found from running ifconfig in terminal.
SERVER = "10.4.1.140"

ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Officially connecting to the server.
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)



def handle_messages(connection: socket.socket):

    while True:
        try:
            msg = connection.recv(2048)

            if msg:
                x = msg.decode()
                string_json = json.loads(msg)
                print(msg)
            else:
                connection.close()
                break

        except Exception as e:
            print(f'Error handling message from server: {e}')
            #connection.close()
            #break


def chat():
    try:
        print('Connected to chat!')
        threading.Thread(target=handle_messages, args=[client]).start()
        while True:
            send(input())
    except KeyboardInterrupt:
        print(f'Error connecting to server socket {e}')
        client.close()


if __name__ == "__main__":
    chat()



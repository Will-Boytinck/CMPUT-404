import socket
from threading import Thread

BYTES_TO_READ = 4096
HOST = "127.0.0.1"
PORT = 8001

def handle_connection(conn,addr):
    '''
    This function was modified from the base code provided in the CMPUT 404 monday lab F23
    '''
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break
            print(data)
            conn.sendall(data)

# start single threaded echo server
def start_server():
    '''
    This function was modified from the base code provided in the CMPUT 404 monday lab F23
    '''
    print("Starting server...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print("Binding to port...")
        s.bind((HOST,PORT))
        #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print("Listening...")
        s.listen()
        conn, addr = s.accept()
        print("Handling connection...")
        handle_connection(conn,addr)


# start multithreaded echo server
def start_threaded_server():
    '''
    This function was modified from the base code provided in the CMPUT 404 monday lab F23
    '''
    print("Starting threaded server...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST,PORT))
        #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen(2)
        while True:
            conn, addr = s.accept()
            thread = Thread(target=handle_connection, args=(conn,addr))
            thread.run()



start_server()
#start_threaded_server()

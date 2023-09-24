import socket
from threading import Thread

BYTES_TO_READ = 4096
PROXY_SERVER_HOST = "127.0.0.1"
PROXY_SERVER_PORT = 8001


def send_request(host,port,request):
    '''
    This function was modified from the base code provided in the CMPUT 404 monday lab F23
    '''
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host,port))
        client_socket.send(request)
        client_socket.shutdown(socket.SHUT_WR)
        
        data = client_socket.recv(BYTES_TO_READ)
        result = b'' + data
        while len(data) > 0:
            data = client_socket.recv(BYTES_TO_READ)
            result += data
        # return response
        return result

def handle_connection(conn, addr):
    '''
    This function was modified from the base code provided in the CMPUT 404 monday lab F23
    '''
    with conn:
        print(f"Connected by {addr}")
        
        request = b''
        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break
            print(data)
            request += data
        response = send_request("www.google.com", 80, request)
        conn.sendall(response)

def start_server():
    '''
    This function was modified from the base code provided in the CMPUT 404 monday lab F23
    '''
    print("Starting server...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((PROXY_SERVER_HOST, PROXY_SERVER_PORT))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen(2) # allow queing of up to 2 connections
        '''
        wait for incoming connection, and when arrives, accept it and create a new
        socket called 'conn' to interact with it
        '''
        conn, addr = server_socket.accept()
        # pass 'conn' off to handle connection to do some logic
        handle_connection(conn,addr)
        
# start multi-threaded proxy server
def start_threaded_server():
    '''
    This function was modified from the base code provided in the CMPUT 404 monday lab F23
    '''
    print("Starting threaded server...")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((PROXY_SERVER_HOST, PROXY_SERVER_PORT))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen(2) # allow queing of up to 2 connections
        
        while True:
            conn, addr = server_socket.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()
            

start_server()
#start_threaded_server()

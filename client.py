import socket

def send_request(server_ip, port, query):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, port))
        s.sendall(query.encode('utf-8'))
        response = s.recv(1024)
    print('Received:', response.decode('utf-8'))

if __name__ == "__main__":
    send_request('localhost', 44445, '2;0;1;26;0;7;5;0;')

import socket
import ssl
import threading

def secure_socket(sock, use_ssl):
    if use_ssl:
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile='server.crt', keyfile='server.key')
        return context.wrap_socket(sock, server_side=True)
    return sock

def log_request(ip, query, execution_time, result):
    print(f"DEBUG: {ip} | {query} | {execution_time:.6f}s | {result}")

def handle_client(conn, addr, file_path, reread_on_query):
    try:
        data = conn.recv(1024).strip()
        search_string = data.decode('utf-8')
        if reread_on_query:
            from search_algorithms import search_algorithm_1
            result, exec_time = search_algorithm_1(file_path, search_string)
        else:
            result, exec_time = search_algorithm_1(file_path, search_string)
        log_request(addr, search_string, exec_time, result)
        conn.sendall(result.encode('utf-8') + b'\n')
    finally:
        conn.close()

def start_server(config):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', int(config['port'])))
    server_socket.listen()
    server_socket = secure_socket(server_socket, config.getboolean('ssl'))

    print(f"Server running on port {config['port']}")

    while True:
        conn, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(conn, addr[0], config['linuxpath'], config.getboolean('reread_on_query'))).start()

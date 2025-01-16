import socket

def start_server():
    # Створення сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Прив'язка сокета до адреси і порта
    server_socket.bind(('localhost', 12345))
    # Прослуховування вхідних з'єднань
    server_socket.listen(5)
    print("Сервер очікує з'єднання...")
    while True:
        # Прийняття нового з'єднання
        client_socket, client_address = server_socket.accept()
        print(f"З'єднання встановлено з {client_address}")
        # Отримання даних від клієнта
        data = client_socket.recv(1024)
        print(f"Отримано: {data.decode('utf-8')}")
        # Відправка даних клієнту (echo)
        client_socket.sendall(data)
        # Закриття з'єднання з клієнтом
        client_socket.close()

if __name__ == "__main__":
    start_server()
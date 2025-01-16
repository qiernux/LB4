import socket

def send_message(message):
    # Створення сокета
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Встановлення з'єднання з сервером
    client_socket.connect(('localhost', 12345))
    # Відправка даних на сервер
    client_socket.sendall(message.encode('utf-8'))
    # Отримання даних від сервера
    data = client_socket.recv(1024)
    print(f"Отримано від сервера: {data.decode('utf-8')}")
    # Закриття сокета
    client_socket.close()

if __name__ == "__main__":
    messages = [f"Hello from client {i + 1}" for i in range(5)]  # Підготовка 5 повідомлень
    for message in messages:
        send_message(message)
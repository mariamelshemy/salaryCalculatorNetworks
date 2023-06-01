import socket
workers = [
    {"id": 101, "base_salary": 50000 },
    {"id": 102, "base_salary": 60500},
    {"id": 103, "base_salary": 5500},
    {"id": 104, "base_salary": 7070},
    {"id": 105, "base_salary": 6500},
    {"id": 180, "base_salary": 6500}
]


def calculate_salary(commission,id):
    for worker in workers:
        if worker["id"] == id:
            base_salary = int(worker["base_salary"])
            break

    # Calculate the salary based commission
    salary = (base_salary * (commission/100))
    return salary


# Create a socket to communicate
# SOCK_STREAM indicates a TCP socket, which provides a reliable, stream-oriented connection
# AF_INET indicates that the socket will use IPv4 addresses
server_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the server address and port
server_address2 = ('localhost', 1346)
server_socket2.bind(server_address2)

# Listen for incoming connections
server_socket2.listen(1)
print("Server commission is listening on", server_address2)

while True:
    # Wait for a client to communicate over the socket
    print("Waiting for a client to connect...")
    client_socket, client_address = server_socket2.accept()
    print("Connected client:", client_address)

    # Receive data from the client
    data = client_socket.recv(1024).decode()
    split_data = data.split(",")
    flag = int(split_data[0])
    if flag == 1:

        new_worker = {"id": int(split_data[1]), "base_salary": int(split_data[2])}
        workers.append(new_worker)
        print(workers)
    else:

        commission = float(split_data[1])
        id = int(split_data[2])
        salary = calculate_salary(commission, id)
        client_socket.send(str(salary).encode())
    # Calculate the salary


    # Send the salary back to the client


    # Close the connection
    client_socket.close()







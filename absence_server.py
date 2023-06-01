import socket

workers = [
    {"id": 101, "absence_cost": 50 },
    {"id": 102, "absence_cost": 60},
    {"id": 103, "absence_cost": 55},
    {"id": 104, "absence_cost": 70},
    {"id": 105, "absence_cost": 65},
    {"id": 180, "absence_cost": 65}
]


def calculate_salary(absence,id):
    for worker in workers:
        if worker["id"] == id:
            absence_cost = int(worker["absence_cost"])
            break

    # Calculate the salary based on absence of specific id
    salary = absence * absence_cost
    print(salary)
    return salary

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the server address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Server absence is listening on", server_address)

while True:
    # Wait for a client to connect
    print("Waiting for a client to connect...")
    client_socket, client_address = server_socket.accept()
    print("Connected client:", client_address)

    # Receive data from the client
    data = client_socket.recv(1024).decode()
    split_data = data.split(",")
    flag = int(split_data[0])
    if flag == 1:

        new_worker = {"id": int(split_data[2]), "absence_cost": int(split_data[1])}
        workers.append(new_worker)
        print(workers)
    else:

        absence = int(split_data[1])
        id = int(split_data[2])
        salary = calculate_salary(absence, id)
        client_socket.send(str(salary).encode())

    # Calculate the salary


    # Send the salary back to the client

    # Close the connection
    client_socket.close()
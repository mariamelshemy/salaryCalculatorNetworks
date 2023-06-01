import socket

workers = [
    {"id": 101, "overtime_cost": 100 },
    {"id": 102, "overtime_cost": 600},
    {"id": 103, "overtime_cost": 500},
    {"id": 104, "overtime_cost": 70},
    {"id": 105, "overtime_cost": 65},
    {"id": 180, "overtime_cost": 65}
]
def calculate_salary(overtime,id):
    for worker in workers:
        if worker["id"] == id:
            overtime_cost = int(worker["overtime_cost"])
            break

    # Calculate the salary based on absence and commission
    salary = overtime * overtime_cost
    return salary


# Create a socket
server_socket3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the server address and port
server_address = ('localhost', 14347)
server_socket3.bind(server_address)

# Listen for incoming connections
server_socket3.listen(1)
print("Server overtime is listening on", server_address)

while True:
    # Wait for a client to connect
    print("Waiting for a client to connect...")
    client_socket, client_address = server_socket3.accept()
    print("Connected client:", client_address)

    # Receive data from the client
    data = client_socket.recv(1024).decode()
    split_data = data.split(",")
    flag=int(split_data[0])
    if flag==1:
        new_worker = {"id": int(split_data[1]), "overtime_cost": int(split_data[2])}
        workers.append(new_worker)
        print(workers)
    else:
      overtime = float(split_data[1])
      id = int(split_data[2])
      salary = calculate_salary(overtime, id)
      client_socket.send(str(salary).encode())
    # Calculate the salary


    # Send the salary back to the client


    # Close the connection
    client_socket.close()
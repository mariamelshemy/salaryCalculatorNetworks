import tkinter as tk
import socket


workers = [
    {"id": 101, "base_salary": 50000},
    {"id": 102, "base_salary": 60500},
    {"id": 103, "base_salary": 5500},
    {"id": 104, "base_salary": 7070},
    {"id": 105, "base_salary": 6500},
    {"id":180,"base_salary":6000}
]

def calculate_salary():
    try:
       flag2=0
       absence = int(absence_entry.get())
       commission = float(commission_entry.get())
       overtime = float(overtime_entry.get())
       worker_id = int(id_entry.get())
       if (absence<0)or(commission<0)or(overtime<0):
           result_label.config(text="please enter positive values.", fg="red")
           return
       for worker in workers:
           if worker["id"] == worker_id:
               print(worker["id"])
               base_salary = int(worker["base_salary"])
               flag2 =1
               break

       if flag2==0:
         result_label.config(text="Wrong ID, please try again.", fg="red")
         return

    except Exception as e:
        result_label.config(text=" Please re check the numbers " , fg="red")
        return
    # Search for the worker by ID

    # Create sockets and server addresses
    client_socket_comm = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket_overtime = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket_absence = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address_comm = ('localhost', 1346)
    server_address_overtime = ('localhost', 14347)
    server_address_absence = ('localhost', 12345)

    try:
        # Connect to the servers
        client_socket_comm.connect(server_address_comm)
        client_socket_overtime.connect(server_address_overtime)
        client_socket_absence.connect(server_address_absence)

        #result_label.config(text="Connected to the servers.", fg="green")

        flag=0
        # Send data to the servers
        data = f"{flag},{commission},{worker_id}"
        client_socket_comm.send(data.encode())

        data = f"{flag},{overtime},{worker_id}"
        client_socket_overtime.send(data.encode())

        data = f"{flag},{absence},{worker_id}"
        client_socket_absence.send(data.encode())

        # Receive salary from the servers
        salary_comm = float(client_socket_comm.recv(1024).decode())
        salary_overtime = float(client_socket_overtime.recv(1024).decode())
        salary_absence = float(client_socket_absence.recv(1024).decode())

        # Calculate the final salary
        salary = base_salary - salary_absence + salary_comm + salary_overtime

        # Display the salary
        result_label.config(text="Salary: $" + str(salary), fg="blue")

    except ConnectionRefusedError:
        result_label.config(text="Connection refused. Server not available.", fg="red")
    except Exception as e:
        result_label.config(text="An error occurred: " + str(e), fg="red")

    # Close the connections
    client_socket_comm.close()
    client_socket_overtime.close()
    client_socket_absence.close()

def addworker():
    global workers
    worker_id = int(workerid_entry.get())
    base_salary = int(basesalary_entry.get())
    overtime_cost = int(overtimecost_entry.get())
    commission = float(commissioncost_entry.get())
    absence = int(absencecost_entry.get())
    new_worker={"id":worker_id,"base_salary":base_salary}
    workers.append(new_worker)
    print(workers)
    client_socket_comm = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket_overtime = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket_absence = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address_comm = ('localhost', 1346)
    server_address_overtime = ('localhost', 14347)
    server_address_absence = ('localhost', 12345)

    try:
        # Connect to the servers
        client_socket_comm.connect(server_address_comm)
        client_socket_overtime.connect(server_address_overtime)
        client_socket_absence.connect(server_address_absence)

        # result_label.config(text="Connected to the servers.", fg="green")

        flag = 1
        # Send data to the servers
        data = f"{flag},{worker_id},{base_salary}"
        client_socket_comm.send(data.encode())

        data = f"{flag},{worker_id},{overtime_cost}"
        client_socket_overtime.send(data.encode())

        data = f"{flag},{absence},{worker_id}"
        client_socket_absence.send(data.encode())

    except ConnectionRefusedError:
        result_label.config(text="Connection refused. Server not available.", fg="red")
    except Exception as e:
        result_label.config(text="An error occurred: " + str(e), fg="red")

    # Close the connections
    client_socket_comm.close()
    client_socket_overtime.close()
    client_socket_absence.close()


# Create the main window
window = tk.Tk()
window.title("Salary Calculator")
window.geometry("400x700")
window.configure(bg="#F5F5F5")
#window.configure(bg="#00C4CC")

# Create labels and entry fields
id_label = tk.Label(window, text="Worker ID:", bg="#F5F5F5", fg="black")
id_label.grid(row=0, column=0, padx=18, pady=10, sticky="w")
#the box where we write input
id_entry = tk.Entry(window)
id_entry.grid(row=0, column=1, padx=10, pady=10)

absence_label = tk.Label(window, text="Number of Absences:", bg="#F5F5F5", fg="black")
absence_label.grid(row=1, column=0, padx=15, pady=10, sticky="w")
absence_entry = tk.Entry(window)
absence_entry.grid(row=1, column=1, padx=10, pady=10)

commission_label = tk.Label(window, text="Commission Rate:", bg="#F5F5F5", fg="black")
commission_label.grid(row=2, column=0, padx=15, pady=10, sticky="w")
commission_entry = tk.Entry(window)
commission_entry.grid(row=2, column=1, padx=10, pady=10)

overtime_label = tk.Label(window, text="Overtime Hours:", bg="#F5F5F5", fg="black")
overtime_label.grid(row=3, column=0, padx=15, pady=10, sticky="w")
overtime_entry = tk.Entry(window)
overtime_entry.grid(row=3, column=1, padx=10, pady=10)

calculate_button = tk.Button(window, text="Calculate Salary", command=calculate_salary, bg="#4CAF50", fg="white")
calculate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

result_label = tk.Label(window, text="Salary: $0.00", bg="#F5F5F5", fg="black", font=("Helvetica", 14, "bold"))
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Add a line  using frame for rectangular shape
separator = tk.Frame(window, height=2, bd=1, relief="groove")
separator.grid(row=6, column=0, columnspan=5, padx=10, pady=10, sticky="we")

workerid_label = tk.Label(window, text="Worker ID:", bg="#F5F5F5", fg="black")
workerid_label.grid(row=7, column=0, padx=18, pady=10, sticky="w")
#the box where we write input
workerid_entry = tk.Entry(window)
workerid_entry.grid(row=7, column=1, padx=10, pady=10)

basesalary_label = tk.Label(window, text="base salary:", bg="#F5F5F5", fg="black")
basesalary_label.grid(row=8, column=0, padx=18, pady=10, sticky="w")
#the box where we write input
basesalary_entry = tk.Entry(window)
basesalary_entry.grid(row=8, column=1, padx=10, pady=10)

overtimecost_label = tk.Label(window, text="overtime cost:", bg="#F5F5F5", fg="black")
overtimecost_label.grid(row=9, column=0, padx=18, pady=10, sticky="w")
#the box where we write input
overtimecost_entry = tk.Entry(window)
overtimecost_entry.grid(row=9, column=1, padx=10, pady=10)

commissioncost_label = tk.Label(window, text="commissoin cost:", bg="#F5F5F5", fg="black")
commissioncost_label.grid(row=10, column=0, padx=18, pady=10, sticky="w")
#the box where we write input
commissioncost_entry = tk.Entry(window)
commissioncost_entry.grid(row=10, column=1, padx=10, pady=10)

absencecost_label = tk.Label(window, text="absence cost:", bg="#F5F5F5", fg="black")
absencecost_label.grid(row=11, column=0, padx=18, pady=10, sticky="w")
#the box where we write input
absencecost_entry = tk.Entry(window)
absencecost_entry.grid(row=11, column=1, padx=10, pady=10)

calculate_button = tk.Button(window, text="Add Worker", command=addworker, bg="#4CAF50", fg="white")
calculate_button.grid(row=13, column=0, columnspan=2, padx=10, pady=20)
# Add additional labels for instructions or information
instruction_label = tk.Label(window, text="Enter worker details and click 'Calculate Salary'.", bg="#F5F5F5", fg="black")
instruction_label.grid(row=14, column=0, columnspan=2, padx=10, pady=10)

info_label = tk.Label(window, text="Note: Make sure that you enter a right id for a corresponding worker.", bg="#F5F5F5", fg="black")
info_label.grid(row=15, column=0, columnspan=2, padx=10, pady=10)

info_label = tk.Label(window, text="Make sure you enter all the fields with appropriate values", bg="#F5F5F5", fg="black")
info_label.grid(row=15, column=0, columnspan=2, padx=10, pady=10)
print(workers)
# Start the main event loop
window.mainloop()

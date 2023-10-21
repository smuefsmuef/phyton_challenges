# Petra Kohler, a01762430@tec.mx

# Write a program that identifies a group of "number_clients" clients, and how many are older than 17, how many are
# foreigners and how many are local_residents. Inside the loop, you must ask for the age and the city, and at the end
# you will print the results.


number_clients = int(input("Enter the number of clients: "))

total_clients = 0
older_than_17 = 0
foreigners = 0
local_residents = 0
client_count = 0

while client_count < number_clients:
    age = int(input(f"Enter the age of client {client_count + 1}: "))
    city = input(f"Enter the city of client {client_count + 1}: ")

    total_clients = total_clients + 1

    if age > 17:
        older_than_17 = older_than_17 + 1

    nationality = input(f"Is client {client_count + 1} a foreigner? (yes/no): ")

    if nationality == "yes":
        foreigners = foreigners + 1
    else:
        local_residents = local_residents + 1

    client_count = client_count + 1

# Print the results
print(f"Total clients: {total_clients}")
print(f"Clients older than 17: {older_than_17}")
print(f"Foreign clients: {foreigners}")
print(f"Local clients: {local_residents}")

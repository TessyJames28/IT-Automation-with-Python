# Opening the guest olist text file
def open_guest_file():
    with open("guests.txt") as guests:
        for line in guests:
            print(line)


# Text file containing visitors for a hotel
guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")
    
guests.close()


open_guest_file()


# Adding new guests
new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()

open_guest_file()


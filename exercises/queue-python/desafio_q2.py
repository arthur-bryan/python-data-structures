from time import sleep
from queue import Queue

def menu():
    option = input(
    """\n========== Data Structures Park ==========\n
[A] Add vehicle
[R] Remove vehicle
[S] See park satus
[E] Exit program\n
---> Choose a option: """).lower()
    if option == 'a':
        add_vehicle()
    elif option == 'r':
        del_vehicle()
    elif option == 's':
        park_status()
    elif option == 'e':
        exit()
    else:
        print("[!] Invalid choice!\n")
        sleep(1)
        menu()

def add_vehicle():
    vehicle_plate = input("[?] Type the car plate: ").upper()
    if vehicle_plate not in park.data:
        park.add_item(vehicle_plate)
        print(f"[+] {vehicle_plate} has entered the park!\n")
        sleep(1)
        menu()
    else:
        print("[!] Vehicle is already in the park!\n")
        sleep(1)
        menu()


def del_vehicle():
    plate = input("[?] Type the car plate: ").upper()
    try:
        exited = park.del_item(plate)
    except Exception as error:
        print(f"[!] Error, {error}\n")
        sleep(1)
        menu()
    else:
        print(f"[-] {plate} has exited the park!\n")
        sleep(1)
        menu()

def park_status():
    print(f"\n========= There are {park.len()} vehicles on the park. ========\n")
    [print(f"{position+1}º - {vehicle}") for position, vehicle in enumerate(park.get_itens())]
    menu()

def main():
    menu()


park = Queue()


if __name__ == '__main__':
    main()

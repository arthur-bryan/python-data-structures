from queue import Queue
from time import sleep


patients_queue = Queue()

def menu():
    try:
        option = int(input(
"""\n====== HOSPITAL ======\n
[1] Register patient
[2] Receive heart
[3] Show patients queue
[4] Exit\n
---> """))
    except ValueError:
        print("[!] Invalide choice!\n")
        sleep(1)
        menu()
    else:
        if option == 1:
            register(patients_queue)
        elif option == 2:
            receive_heart(patients_queue)
        elif option == 3:
            show_patients(patients_queue)
        elif option == 4:
            print("Exiting program...")
            sleep(1)
            exit(0)
        else:
            print("[!] Invalid choice!\n")
            sleep(1)
            menu()

def register(queue):
    name = input("[+] Patient's name: ").title()
    phone = input("[+] Patient's phone: ")
    urgency = int(input(
"""
[5] Very Urgent
[4] Urgent
[3] Medium
[2] Little Urgent
[1] Not Urgent
   ---> """))
    if (urgency > 0 and urgency < 6) and (phone not in list(map(lambda patient: patient['Phone'], queue.get_itens()))):
        data = {
        'Name': name,
        'Phone': phone,
        'Urgency': urgency
        }
        queue.add_item(data)
        queue.data.sort(key=lambda urgency_level: urgency_level['Urgency'], reverse=True)
        print("[+] Patient registered successfully!\n")
        sleep(1)
        menu()
    else:
        print("[!] Invalid choice or number already registered!\n")
        sleep(1)
        menu()

def receive_heart(queue):
    if queue.len() > 0:
        print("[+] Heart received!!")
        print(f"[+] The patient {queue.data[0]['Name']} will be operated! Her/his number is {queue.data[0]['Phone']}.\n")
        queue.data.pop(0)
        queue.size -= 1
        sleep(1)
        menu()
    else:
        print("[!] There is no patient waitingo for a heart donation!\n")
        sleep(1)
        menu()

def show_patients(queue):
    print(f"========== There are {queue.len()} patients waiting in the queue. ==========")
    [print(f"{i + 1} - Name: {patient['Name']}, Phone: {patient['Phone']}, Urgency: {patient['Urgency']}.") for i, patient in enumerate(queue.get_itens())]
    print()
    sleep(1)
    menu()


def main():
    menu()

if __name__ == '__main__':
    main()

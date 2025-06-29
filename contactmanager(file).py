import shutil
class ContactManager:
    def __init__(self):
        pass

    def add_contact(self, name, number):
        with open ('contacts.txt', 'r') as file:
            lines = file.readlines()
            target_line = f"{name} - {number} \n"
            if target_line in lines:
                print(f"The Contact {name} is already existed! ")
            else:
                with open ('contacts.txt', 'a') as file:
                    file.write (f"{name} - {number} \n")
                print (f"contact {name} successfully added...")

    def delete_contact (self, name, number):
        with open ('contacts.txt', 'r') as file:
            lines=file.readlines()
            target_line =  (f"{name} - {number} \n")
            new_lines = [line for line in lines if line != target_line]
        with open ('contacts.txt', 'w') as file:
            file.writelines (new_lines)
        if len(lines) == len(new_lines):
            print (f' The contact {name} not found')
        else:
            print (f'{name} deleted!')

    def backup_contact(self):
        shutil.copy('contacts.txt', 'backup.txt')
        print ('Backup file created as backup.txt')

    def search_contact (self,name):
        result = []
        with open ('contacts.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                if name.lower() in line.lower():
                    result.append(line)
                    print (f'Your searching results: {result}')
                else:
                    print (f"The contact {name} has not be found.")

    def display_contact(self):
        with open ('contacts.txt', 'r') as file:
            content= file.read()
            if content.strip() == '':
                print ("No Contacts To Display")
            else:
                print (f'The contacts are as bellow:\n {content}')


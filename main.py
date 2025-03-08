import multi_tool
from colorama import Fore, init

init(autoreset=True)

DARKRED = '\033[38;5;1m'  
BRIGHTRED = '\033[38;5;9m'  

logo = f"""
  {Fore.RED}█████████  {DARKRED}█████   {BRIGHTRED}████ █████ {Fore.RED}██████████  {BRIGHTRED}█████ {DARKRED}██████████   {Fore.RED}█████
 {BRIGHTRED}███░░░░░███{DARKRED}░░███   {BRIGHTRED}███░ ░░███ {Fore.RED}░░███░░░░░███░░███ {BRIGHTRED}░░███░░░░███ ░░███ 
{Fore.RED}░███    ░░░  {BRIGHTRED}░███  {DARKRED}████    ░███  {Fore.RED}░███    ░███ {BRIGHTRED}░███  ░███   ░░███ ░███ 
{DARKRED}░░█████████  {Fore.RED}░███████     ░███  {BRIGHTRED}░██████████  ░███  ░███    ░███ ░███ 
  ░░░░░░░░███ ░███░░███    ░███  ░███░░░░░███ ░███  ░███    ░███ ░███ 
 {BRIGHTRED}████    ░███ ░███ ░░███   ░███  ░███    ░███ ░███  ░███    ███  ░███ 
░░█████████  {Fore.RED}█████ ░░████ █████ ███████████  █████ {BRIGHTRED}█████████   █████
  ░░░░░░░░░  ░░░░░   ░░░░ ░░░░░ ░░░░░░░░░░░  ░░░░░ ░░░░░░░░░░   ░░░░░ 
                                                                     
                                                                     
                                                                     
          {BRIGHTRED}██████████    {Fore.RED}███████       {DARKRED}███████    {BRIGHTRED}█████              
         {Fore.RED}░█░░░███░░░█  {DARKRED}███░░░░░███   {BRIGHTRED}███░░░░░███ ░░███               
         ░   ░███  ░  ███     ░░███ ███     ░░███ ░███               
             ░███    ░███      ░███░███      ░███ ░███               
             ░███    ░███      ░███░███      ░███ ░███               
             ░███    ░░███     ███ ░░███     ███  ░███      █        
             █████    ░░░███████░   ░░░███████░   ███████████        
            ░░░░░       ░░░░░░░       ░░░░░░░    ░░░░░░░░░░░        
"""

def print_menu():
    print("Welcome to the Multi Tool!")
    print("1. Get System Info")
    print("2. Get Current Time")
    print("3. Ping a Host")
    print("4. Rename a File")
    print("5. Delete a File")
    print("6. Copy a File")
    print("7. Exit")
    print("Please choose an option (1-7): ")

while True:
    print(logo)
    print_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        multi_tool.system_info()
    elif choice == '2':
        multi_tool.get_time()
    elif choice == '3':
        host = input("Enter host to ping: ")
        multi_tool.ping_host(host)
    elif choice == '4':
        old_name = input("Enter the old file name: ")
        new_name = input("Enter the new file name: ")
        multi_tool.rename_file(old_name, new_name)
    elif choice == '5':
        filename = input("Enter the file name to delete: ")
        multi_tool.delete_file(filename)
    elif choice == '6':
        source = input("Enter the source file path: ")
        destination = input("Enter the destination file path: ")
        multi_tool.copy_file(source, destination)
    elif choice == '7':
        print("Exiting the Multi Tool. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")

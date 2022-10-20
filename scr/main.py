from linksClass import Links
from tools import clear_screen


def main():
    """Main function"""
    ask_user()


def ask_user():
    """Ask user for input"""
    link = Links()
    while True:
        print("1. Set Engine, Set Query\n2. Get Links\n3. Save Links\n4. Print Links\n5. Read Links\n6. Exit")
        choice = input(": ")
        if choice == "1":
            link.set_engine()
            link.set_query()
            clear_screen()
        elif choice == "2":
            link.get_links()
        elif choice == "3":
            link.save_links()
        elif choice == "4":
            link.print_links()
        elif choice == "5":
            link.read_links()
        elif choice == "6":
            exit()

if __name__ == "__main__":
    main()

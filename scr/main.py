from linksClass import Links
from tools import clear_screen, set_torrc


def main():
    """Main function"""
    ask_user()


def ask_user():
    """Ask user for input"""
    link = Links()
    while True:
        print(
            "1. Set Engine, Set Query, Get Links\n2. Save Links\n3. Print Links\n4. Read Links\n5. Set Torrc\n6. Exit"
        )
        choice = input(": ")
        if choice == "1":
            link.set_engine()
            link.set_query()
            link.get_links()
            clear_screen()
        elif choice == "2":
            link.save_links()
        elif choice == "3":
            link.print_links()
            clear_screen()
        elif choice == "4":
            print(link.read_links())
        elif choice == "5":
            set_torrc()
        elif choice == "6":
            exit()


if __name__ == "__main__":
    main()

from linksClass import Links


def main():
    """Main function"""
    link = Links()
    link.set_engine()
    link.set_query()
    link.get_links()
    link.save_links()

if __name__ == "__main__":
    main()

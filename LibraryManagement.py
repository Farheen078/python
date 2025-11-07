library = {}

while True:
    print("1. Add Book")
    print("2. Show Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter book name: ")
        author = input("Enter author name: ")
        qty = int(input("Enter quantity: "))
        library[name] = {"author": author, "quantity": qty}
        print("Book added!\n")

    elif choice == "2":
        if not library:
            print("No books available.\n")
        else:
            for name, info in library.items():
                print(f"{name} by {info['author']} - {info['quantity']} copies")
            print()

    elif choice == "3":
        name = input("Enter book name to borrow: ")
        if name in library and library[name]["quantity"] > 0:
            library[name]["quantity"] -= 1
            print("Book borrowed!\n")
        else:
            print("Book not available!\n")

    elif choice == "4":
        name = input("Enter book name to return: ")
        if name in library:
            library[name]["quantity"] += 1
            print("Book returned!\n")
        else:
            print("Book not found!\n")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!\n")

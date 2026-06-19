books = []

while True:

    print("\n===== LIBRARY MANAGEMENT =====")

    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        book_id = int(input("Enter Book ID: "))
        name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")

        book = {
            "id": book_id,
            "name": name,
            "author": author,
            "available": True
        }

        books.append(book)

        print("Book Added Successfully")

    elif choice == "2":
        if len(books) == 0:

            print("No Books Available")

        else:

            for book in books:

                print(
                    book["id"],
                    book["name"],
                    book["author"],
                    book["available"]
                )

    elif choice == "3":

        book_id = int(
            input("Enter Book ID: ")
        )

        found = False

        for book in books:

            if book["id"] == book_id:

                found = True

                if book["available"]:

                    book["available"] = False

                    print("Book Issued")

                else:

                    print(
                        "Book Already Issued"
                    )

        if not found:

            print("Book Not Found")

    elif choice == "4":

        book_id = int(
            input("Enter Book ID: ")
        )

        found = False

        for book in books:

            if book["id"] == book_id:

                found = True

                book["available"] = True

                print("Book Returned")

        if not found:

            print("Book Not Found")

    elif choice == "5":

        book_id = int(
            input("Enter Book ID: ")
        )

        found = False

        for book in books:

            if book["id"] == book_id:

                books.remove(book)

                found = True

                print("Book Deleted")

                break

        if not found:

            print("Book Not Found")

    elif choice == "6":

        print("Thank You")


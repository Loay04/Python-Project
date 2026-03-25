import os
book={   }
def clear():
    os.system("cls") if os.name =="nt" else os.system("clear")
def add_book():
    while True:
        clear()
        isbn = int(input("Entre ISBN: "))
        title = input("Entre the Title: ")
        author = input("Entre the name of Author")
        book[isbn] = {"Title":title,"Available":True }
        print(f"Book {title} by {author} added to catalog with {isbn}.")
        if input("Do yo want to add another book: (Y/N) ").upper() !="Y":
            break
def check_out_book():
    while True:
        clear()
        isbn = int(input("Entre ISBN on check book: "))
        if isbn in book: 
            if book[isbn]["Available"] == True:
              print(f"Book {book[isbn]["Title"]} checked out successfully.")
              book[isbn]["Available"] = False
            else:
                print("Sorry, the book is currently check out.")
        else:
            print("Book is not found in the calalog")
        if input("Do yo want to checked out another book: (Y/N) ").upper() !="Y":
            break
def check_in():
    while True:
        clear()
        isbn = int(input("Entre ISBN on check book: "))
        if isbn in book:
          if book[isbn]["Available"] == False:
            print(f"Book {book[isbn]["Title"]} check in successfully.")
            book[isbn]["Available"] = True
          else:
            print("The book is not check in.")
        else:
            print("Book is not found in the catalog")
        if input("Do yo want to checked out another book: (Y/N) ").upper() !="Y":
            break
def view():
    while True:
      clear()
      print("*** library catalog***")
      for isbn in book:
         book_info = book[isbn]
         print(f"ISBN: {isbn} Title: {book_info["Title"]} : {book_info["Available"]}")
      if input("Do yo want to checked out another book: (Y/N) ").upper() !="Y":
            break
while True:
    clear()
    print("1- Add a book")
    print("2- Check out book")
    print("3- Check in book")
    print("4- View book")
    print("5- Exist")
    choice = input("Entre the number between 1-5: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        check_out_book()
    elif choice == "3":
        check_in()
    elif choice == "4":
        view()
    elif choice == "5":
        exit()
    else:
        print("Please entre the number between 1-5")
        input("Please Entre any bottom to continue......")
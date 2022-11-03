### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.


def create_new_book(library):
    title = input("What is the title of the book you would like to add? - ")
    author = input("Who is the author of the book you would like to add? - ")
    try:
        year = int(input("What year was this book published? - "))
    except:
        year = int(input("Please type a number for the year - "))
    try:
        rating = float(input("What rating out of 5 would you give this book? - "))
    except:
        rating = float(input("Please type a number for the rating? - "))
    try:
        pages = int(input("What is the page count of the book? - "))
    except:
        pages = int(input("Please type a number for the pages? - "))
    print('New Book added to the favorites list!')

    with open(library, 'a') as f: #What is a again?
        f.write(f'{title}, {author}, {year}, {rating}, {pages}\n')


### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

def readbooks(library):
    print('Your favorite books:')
    with open('library.txt', 'r') as f:
        file = f.readlines()

    for line in file:
        title, author, year, rating, pages = line.split(', ')
        print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor


def get_books_as_list_of_dictionaries(library):
    books_list = []
    with open(library, "r") as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages = line.split(", ")
            books_list.append({
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            })
    return books_list

def get_book_printed(book):
    print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Rating: {book['rating']}, Pages: {book['pages']}")


def view_favorite_books(library):
    print("\nHere are all your books...\n")
    for book in get_books_as_list_of_dictionaries(library):
        get_book_printed(book)

def get_highest_rated_book(book_source):
    list = get_books_as_list_of_dictionaries(book_source)
    return max(list, key=lambda x: int(x["rating"]))

def get_lowest_rated_book(book_source):
    list = get_books_as_list_of_dictionaries(book_source)
    return min(list, key=lambda x: int(x["rating"]))

def main_menu(library):
    mainmenuopen = True
    while mainmenuopen:

        print('''Main Menu\nType a number for the following options:\n
    1. View Favorite Books\n
    2. Add a Favorite Book\n
    3. View Highest Rated Book\n
    4. View Lowest Rated Book\n
    5. View how many books\n
    ''')

        choice = input('Choose an option:')

        if choice == "1":
            if view_favorite_books(library) == False:
                print('You need to add a book first!')
            else:
                view_favorite_books(library)
        elif choice == "2":
            create_new_book(library)
        elif choice == "5":
            print(f"\nYou have a total of {len(get_books_as_list_of_dictionaries(library))} books.\n")
        elif choice == "3":
            print("\nHere is your highest rated book...\n")
            get_book_printed(get_highest_rated_book(library))
        elif choice == "4":
            print("\nHere is your lowest rated book...\n")
            get_book_printed(get_lowest_rated_book(library))
        else:
            print("\nInvalid Entry. Type an available option.\n")


## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!



if __name__ == '__main__':
    main_menu("library.txt")
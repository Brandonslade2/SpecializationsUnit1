### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

def create_new_book(book_dictionary):
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
    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }
    print('New Book added to the favorites list!')
    print(type(book_dictionary['title']))
    print(type(book_dictionary['author']))
    print(type(book_dictionary['year']))
    print(type(book_dictionary['rating']))
    print(type(book_dictionary['pages']))
    return book_dictionary

# create_new_book()




### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

# THIS WAS DONE ABOVE




### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

# THIS WAS DONE ABOVE


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

favoritebooks = ['a', 'b', 'c', 'd', 'e']

def mainmenuaddask():
    answer = False
    newbook = ''
    try:
        mainmenuadd = input('Would you like to add a book to your favorites? (Y/N)--')
    except:
        mainmenuadd = input('Please type Y for Yes or N for No (Y/N)--')
    while answer == False:
        if mainmenuadd == 'Y':
            newbook = create_new_book(newbook)
            favoritebooks.append(newbook)
            answer = True
        elif mainmenuadd == 'N':
            print('You replied No. Closing inquiry')
            answer = True
        else:
            print('You put in a wrong value to the inquiry. Type Y or N.')

mainmenuaddask()
print(favoritebooks)


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

# see above


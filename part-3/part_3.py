my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def mybook (a):
    string = f"uh"
    print(string)
    return string

mybook(my_book)


# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below



# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def mybooktitle(my_book):
    title = my_book['title']
    print(title)

def mybookauthor (my_book):
    author = my_book['author']
    print(author)

def mybookyear (my_book):
    year = my_book['year']
    print(year)

def mybookrating (my_book):
    rating = my_book['rating']
    print(rating)

def mybookpages (my_book):
    pages = my_book['pages']
    print(pages)

mybooktitle(my_book)
mybookauthor(my_book)
mybookyear(my_book)
mybookrating(my_book)
mybookpages(my_book)
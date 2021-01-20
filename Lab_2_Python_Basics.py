class Author:
    def __init__(self, name):
        self.name = name
        self.books = [] # We know its the same for every new author
    def publish(self, title): # New method called publish with arguement title
        if title not in self.books:
            self.books.append(title) # add to self.books list
        else:
            print(f'The book {title} has already been added')
    def __str__(self): #__str__ is like Java's ToString()
        if self.books:
            book_list = ', '.join(self.books) # If there is books create a book_list
            # join all the books with a comma
            # book_list = ', '.join(self.books) or 'No books'. Just this line without the else would work too
        else: 
            book_list = 'No books' # Remember empty list = false
        return f'Name: {self.name}. Books Published: {book_list}'

# Test it out
shakespeare = Author('William Shakespeare')
shakespeare.publish('Hamlet')
shakespeare.publish('Richard III')


print(shakespeare)

# Add another author
johnny = Author('Johnny')

print(johnny)

# Adding another book that is already in the list
shakespeare.publish('Hamlet')

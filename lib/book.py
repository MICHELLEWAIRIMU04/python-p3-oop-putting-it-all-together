#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
    def get_title(self):
        return self._title

    def set_title(self, title):
        if isinstance(title, str):
            self._title = title

        else:
            raise ValueError("Name must be a string")

    title = property(get_title, set_title) 

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        
        else:
            raise ValueError("page_count must be an integer")

    page_count = property(get_page_count, set_page_count)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def __str__(self):
        return f"Book: {self.title}, Pages: {self.page_count}"

book = Book("And Then There Were None", 272)
book = Book("The World According to Garp", 69)
print(book)
book.turn_page()

        
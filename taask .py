class Book:
    name="the book"
    auther ="zeeshanali"
    pages=200

    def decribe(self,name,auther,pages):
        self.name=name
        self.auther=auther
        self.pages=pages
        print("the name of book is",name,"written by",auther,"and it has",pages,"pages")


about =Book()
about.decribe("the book","zeeshanali",200)
about.decribe("the is a book","ali",300)
about.decribe("the book is a good book","zeeshan",400)

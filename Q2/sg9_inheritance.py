class Publication:                              #This creates a class called Publication.
    def __init__(self, title, author):          #These are the attributes.
        self.title = title
        self.author = author

    @property
    def get_title(self):                        #This method allows you to get the title of the publication.
        print(f"Title: {self.title}")
    
    @property
    def get_author(self):                       #This method allows you to get the author of the publication.
        print(f"Author: {self.author}")

    def set_title(self, new_title):             #This method allows you to set the title of the publication.
        self.title = new_title
        print(f"Title updated to: {self.title}")

    def set_author(self, new_author):           #This method allows you to set the author of the publication.
        self.author = new_author
        print(f"Author updated to: {self.author}")
    
    def display_info(self):                     #This method displays the title and author of the publication.
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
    
class Book(Publication):                        #This creates a class called Book that inherits from the Publication.
    def __init__(self, title, author, number_of_pages):  #These are the attributes of the class.
        super().__init__(title, author)                  #These are the attributes of the parent class.
        self.number_of_pages = number_of_pages

    def get_number_of_pages(self):                       #This method allows you to get the number of pages of the book.
        return self.number_of_pages

    def set_number_of_pages(self, updates_pages):        #This method allows you to set the number of pages that must be greater than 0.
        if updates_pages < 0:
            print("Number of pages cannot be negative.")
        else:
            self.number_of_pages = updates_pages
            print(f"Number of Pages updated to: {self.number_of_pages}")
        
class Magazine(Publication):                             #This creates a class called Magazine that inherits from the Publication.
    def __init__(self, title, author, issue_number):     #These are the attributes of the class.
        super().__init__(title, author)                  #These are the attributes of the parent class.
        self.issue_number = issue_number

    def get_issue_number(self):                          #This method allows you to get the issue number of the magazine.
        return self.issue_number

    def get_issue_number(self):                          #This method allows you to get the issue number of the magazine.
        return self.issue_number

    def set_issue_number(self, issue_num):               #This method allows you to set the issue number of the magazine that must be greater than 0.
        self.issue_number = issue_num
        if issue_num < 0:
            print("Issue number cannot be negative. Issue number not updated.")
        else:
            print(f"Issue Number updated to: {self.issue_number}")
        
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff & Van Dongen, H.")      #This creates an object of the Publication class.
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)                                          #This creates an object of the Book class.
mag1 = Magazine("National Geographic", "Various Authors", 202)                             #This creates an object of the Magazine class.

print("Public Information:")                       #This prints the information of the publication.
pub1.display_info()
print("\nBook Information:")                       
book1.set_number_of_pages(-310)
book1.display_info()
print(f"Number of Pages: {book1.get_number_of_pages()}")

print("\nMagazine Information:")                   #This prints the information of the magazine.
mag1.display_info()
print(f"Issue Number: {mag1.get_issue_number()}")

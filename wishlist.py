books = [
    "Learning Python: Powerful Object-Oriented Programming - Mark Lutz",
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinney",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
]

print("Suggested gift: {}".format(books[0]))

print("Books:")
for book in books:
  print("* " + book)

def display_wishlist(display_name, wishes):
    items = wishes.copy() #'item' makes sure a COPY of the list is edited so the original is kept
    print(display_name + ":")
    print("====> Suggested gift:", item[0], "<=====") 
    # Return a slice of the list from the 2nd element on...
    for items in items[1:]:
        print("* " + item)
    print()
    
display_wishlist("Books", books)
display_wishlist("Video Games", video_games)

quote = "The greatest teacher failure is"
words = quote.split() #takes the initial string and prints as a list
words #runs the new list from the .split() commands
import time #imports time functionality
for word in words:
  print(word)
  time.sleep(.5) #adds 1/2 second delay between prints

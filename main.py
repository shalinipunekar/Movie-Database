import csv
from time import sleep

# properties: title, genre, year, rating, director, box office (millions)
class Movie():
  def __init__(self, title, genre, year, rating, director, box_office):
    self.title = title
    self.genre = genre
    self.year = year
    self.rating = rating
    self.director = director
    self.box_office = box_office
  
  def display(self):
    print("Movie:", self.title)
    print("Genre:", self.genre)
    print("Year:", self.year)
    print("Rating:", self.rating)
    print("Director:", self.director)
    print("Box office:", self.box_office)

# properties: name of your database, a list of Movie objects, # of Movies in your list
class MovieDatabase():
  def __init__(self, name, movies):
    self.name = name
    self.movies = movies
    self.amount = len(movies)

  def display_info(self):
    print("Name of database:", self.name)
    print("Number of movies:", self.amount)

  def display_all(self):
    sleep(0.2)
    for i in self.movies:
      i.display()
      print()
      sleep(0.2)

  def display_title(self, title):
    sleep(0.2)
    found = False
    for i in self.movies:
      if i.title == title:
        i.display()
        print()
        sleep(0.2)
        found = True
    if found == False:
      print("We do not have a movie by that title.\n")
      
  def display_genre(self, genre):
    sleep(0.2)
    found = False
    for i in self.movies:
      if i.genre == genre:
        i.display()
        print()
        sleep(0.2)
        found = True
    if found == False:
      print("There are not movies by that genre.\n")

  def display_year(self, year):
    sleep(0.2)
    found = False
    for i in self.movies:
      if i.year == year:
        i.display()
        print()
        sleep(0.2)
        found = True
    if found == False:
      print("We do not have a movie that was released that year.\n")

  def display_director(self, director):
    sleep(0.2)
    found = False
    for i in self.movies:
      if i.director == director:
        i.display()
        print()
        sleep(0.2)
        found = True
    if found == False:
      print("We do not have a movie under that director.\n")

  def display_rating(self, rating, action):
    sleep(0.2)
    # action = 0 (equal) 1 (less than) 2 (greater than)
    found = False
    for i in self.movies:
      if action == 0 and i.rating == rating:
        i.display()
        print()
        sleep(0.2)
        found = True
      elif action == 1 and i.rating < rating:
        i.display()
        print()
        sleep(0.2)
        found = True
      elif action == 2 and i.rating > rating:
        i.display()
        print()
        sleep(0.2)
        found = True
    if found == False:
      print("WE do not have movies under that range of rating.\n")

  def display_boxoffice(self, boxoffice, action):
    sleep(0.2)
    found = False
    for i in self.movies:
      if i.box_office == boxoffice and action == 0:
        i.display()
        print()
        sleep(0.2)
        found = True
      elif action == 1 and i.box_office < boxoffice:
        i.display()
        print()
        sleep(0.2)
        found = True
      elif action == 2 and i.box_office > boxoffice:
        i.display()
        print()
        sleep(0.2)
        found = True
    if found == False:
      print("We do not have movies under those boxoffice earnings.\n")

def import_data(filename):
  data = []

  with open(filename, mode ='r') as file:
    # reading the CSV file
    csvFile = csv.reader(file)
    # displaying the contents of the CSV file
    for lines in csvFile:
      lines[2] = int(lines[2])
      lines[3] = int(lines[3])
      lines[-1] = float(lines[-1])
      # print(lines)
      data.append(lines)
  
  return data

def setup():
  data = import_data('data/movies.csv')

  movies = [] # our list of movie objects 
  for i in data:
    e = Movie(i[0], i[1], i[2], i[3], i[4], i[5])
    movies.append(e)

  db = MovieDatabase("My Movie Collection", movies)
  return db

def welcome_message(db):
  print("Welcome to", db.name) 
  print("We have", db.amount, "movies.\n")
  
def print_menu():
  print("a) Search for a movie by title")
  print("b) Search for a movie by genre")
  print("c) Search for a movie by year")
  print("d) Search for a movie by rating")
  print("e) Search for a movie by director")
  print("f) Search for a movie by box office")
  print("g) Display all movies")
  print("h) Exit program\n")

def get_user(db):
  user_input = input("What option would you like to choose? Type the letter: ")
  print()
  if user_input == "a":
    print("You chose to search for movies by title.\n")
    title = input("Enter title: ")
    print()
    db.display_title(title)
  elif user_input == "b":
    print("You chose to search for movie by genre.\n")
    genre = input("Enter genre: ")
    print()
    db.display_genre(genre)
  elif user_input == "c":
    print("You chose to search for movies by the release year.\n")
    year = input("Enter year: ")
    while year.isnumeric() == False:
      print("\nInvalid option!\n")
      year = input("Enter year: ")
    year = int(year)
    print()
    db.display_year(year)
  elif user_input == "d":
    print("You chose to search for movies by rating.\n")
    rating = input("Enter rating: ")
    while rating.isnumeric() == False:
      print("\nInvalid response!\n")
      rating = input("Enter rating: ")
    rating = int(rating)
    print("\n0 (equal), 1 (less than), 2 (greater than)")
    user = input("Choose 0, 1, or 2 as your action: ")
    while user.isnumeric() == False:
      print("\nInvalid reply!\n")
      user = input("Choose 0, 1, or 2 as your action: ")
    user = int(user)
    print()
    db.display_rating(rating, user)
  elif user_input == "e": 
    print("You chose to search for movies by the director.\n")
    director = input("Enter director: ")
    print()
    db.display_director(director)
  elif user_input == "f":
    print("You chose to search for movies by box office.\n")
    box = input("Enter box office: ")
    while box.isnumeric() == False:
      print("\nInvalid reply\n")
      box = input("Enter box office: ")
    box = float(box)
    print("\n0 (equal), 1 (less than), 2 (greater than)")
    user = input("Choose 0, 1, or 2 as your action: ")
    while user.isnumeric() == False:
      print("\nInvalid reply!\n")
      user = input("Choose 0, 1, or 2 as your action: ")
    user = int(user)
    print()
    db.display_boxoffice(box, user)
  elif user_input == "g":
    print("You chose to display all movies\n")
    db.display_all()
  elif user_input == "h":
    print("You have chosen to stop scrolling", db.name, "\n")
  else:
    print("You chose an invalid letter.\n")
  return user_input

def goodbye_message(db):
  print("Thank you for using", db.name,"!") 

def main():
  x = setup()
  welcome_message(x)
  y = '' 
  while (y != "h"):
    print_menu()
    y = get_user(x)
  goodbye_message(x)

main()
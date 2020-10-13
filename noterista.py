statement = """
Welcome to noterista
To create a New note enter N
To Edit an Existing note enter E
To Delete a note enter D
To View all notes enter V
To Quit enter Q
"""

def getUserInput():
  print(statement)
  return input() 

noteList = []

def newCard():
  print("welcome to the newCard() function")

def editCard():
  print("welcome to the editCard() function")

def deleteCard():
  print("welcome to the deleteCard() function")

def viewCards():
  print("welcome to the viewCards() function")

while True:
  userInput = getUserInput()
  if userInput == 'N':
    newCard()
  elif userInput == 'E':
    editCard()
  elif userInput == 'D':
    deleteCard()
  elif userInput == 'V':
    viewCards()
  elif userInput == 'Q':
    break

print("you have reached the end of the program... good-bye")


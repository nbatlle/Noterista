# crud 

statement = """
Welcome to quicknote.
To create a New note enter N
To Edit an Existing note enter E
To Delete a note enter D
To View all notes enter V
To Quit enter Q
"""

def getUserInput():
  print(statement)
  userInput = input()
  return userInput

noteList = []

def newCard():
  print("welcome to the newCard() function")
  print("enter a note now:")
  newText = input()
  newId = len(noteList) 
  note = {"noteId": newId, "noteText": newText, "deleteMarker": False}
  noteList.append(note)
  print("new note created")

def editCard():
  print("welcome to the editCard() function")
  print("to edit a note, first enter the noteId of the note")
  print("if not known, enter X to exit this feature, then enter V to view all notes")
  userInput = input()
  if userInput == 'X':
    return
  else:
    noteToEditId = int(userInput)
    for note in noteList:
      if noteToEditId == note["noteId"]:
        print("you have selected note #", noteToEditId, "...", note)
        print("enter the text to replace the existing note:")
        newText = input()
        note["noteText"] = newText 
        print("note #", noteToEditId, "edited")

def deleteCard():
  print("welcome to the deleteCard() function")
  print("to delete a note, first enter the noteId of the note")
  print("if not known, enter X to exit this feature, then enter V to view all notes")
  userInput = input()
  if userInput == 'X':
    return
  else:
    noteToDeleteId = int(userInput)
    for note in noteList:
      if noteToDeleteId == note["noteId"]:
        print("you have selected note #", noteToDeleteId, "...", note)
        print("are you sure you want to delete this?  enter Y or N")
        userInput = input()
        if userInput == 'Y':
          note["deleteMarker"] = True
        else:
          return

def viewCards():
  print("welcome to the viewCards() function")
  print("here are your notes:")
  for note in noteList:
    if note["deleteMarker"] == False:
      print(noteList.index(note), note)

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


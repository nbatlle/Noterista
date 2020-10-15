# noterista.py
# use this file to develop basic object-less functionality
# begin new file when ready for objects

# SQLite setup:
#   connect to db
#   create table if not present
#   display existing notes

import sqlite3 
from sqlite3 import Error 

try:
  conn = sqlite3.connect('noterista.db')
  print(sqlite3.version)
except Error as e:
  print(e)

cur = conn.cursor()

sql_create_notes_table = """
CREATE TABLE IF NOT EXISTS notes (
  ID integer PRIMARY KEY,
  Note text NOT NULL,
  DeleteMarker integer
);"""

noteList = []

try:
  cur.execute(sql_create_notes_table)
  cur.execute("SELECT * FROM notes")
  rows = cur.fetchall()
  print("Here are your notes")
  for row in rows:
    note = list(row)
    noteList.append(note)
    print(row)
except Error as e:
  print(e)


# CRUD begins here
# use lists (not tuples as it says in notes below) instead of dictionaries for now
# w/o some extra work SQLite rows seem to function as tuples
# changed tuples to lists above (line36 for now) b/c tuples are immutable
# conceptually, think of note lists as dictionaries w/ keys id, text, deletemarker corresponding to indeces 0,1,2
# eventually they will be objects anyway, so for now just choose the path of least resistance

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

def newCard():
  print("welcome to the newCard() function")
  print("enter a note now:")
  newText = input()
  newId = len(noteList) 

  """ changing dictionary to tuple
  note = {"noteId": newId, "noteText": newText, "deleteMarker": 0}
  """

  note = (newId, newText, 0)
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

      """ changing dictionary to tuple
      if noteToEditId == note["noteId"]:
      """

      if noteToEditId == note[0]:
        print("you have selected note #", noteToEditId, "...", note)
        print("enter the text to replace the existing note:")
        newText = input()
        note[1] = newText 
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

      """ changing dictionary to tuple
      if noteToDeleteId == note["noteId"]:
      """

      if noteToDeleteId == note[0]:
        print("you have selected note #", noteToDeleteId, "...", note)
        print("are you sure you want to delete this?  enter Y or N")
        userInput = input()
        if userInput == 'Y':
          note[2] = 1 
        else:
          return

def viewCards():
  print("welcome to the viewCards() function")
  print("here are your notes:")
  for note in noteList:

    """ changing dictionary to tuple
    if note["deleteMarker"] == 0:
    """
  
    if note[2] == 0:
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


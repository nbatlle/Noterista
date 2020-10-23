# main.py

# move SQL setup and CRUD while loop to this file after implementing Note class
# turn CRUD function calls into Note method calls

import sqlite3
from sqlite3 import Error

import databasefunctions as dbf

from noteClass import Note


###
# SQL Setup
###

def dbsetup():
  print("connecting to db...")
  conn = dbf.connect('noterista.db')

  print("checking notes table...")
  c = dbf.table(conn)

  print("reading notes from table...")
  dbf.tableToNote(c)

  print("here are your notes...")
  for note in Note.noteList:
    note.view()

  dbStuff = [conn, c]
  return dbStuff


###
# CRUD Functions 
###

commands = "Commands are N (New note), E (Edit note), D (Delete note), V (View all notes), C (see Commands) and Q (Quit)"
prompt = "Enter a command:"
welcome = "Welcome to Noterista. " + commands + prompt

###

def begin():
  print(welcome)
  userInput = input()
  return userInput 

###

def nextCommand():
  print(prompt)
  return input()

###
# starting w/ newNote, and going through remaining crud functions:
# move user input prompt from crud function to main
# in order to facilitate streamlining of UI
# ie newNote does not need to request user input b/c it has already been provided
###

def newNote(conn, c, noteText):
  #print("Enter a note:")
  #userInput = input()
  noteId = Note.nextId
  note = Note(noteId, noteText)
  dbf.newNote(conn, c, noteId, noteText)

###

def editNote(conn, c):
  print("Enter the Id of the note to edit:")
  noteToEditId = int(input())
  for note in Note.noteList:
    if noteToEditId == note.idNum:
      print("Enter the corrected text:")
      newText = input()
      note.edit(newText)
      dbf.editNote(conn, c, noteToEditId, newText) 

###

def deleteNote(conn, c):
  print("Enter the Id of the note to delete:")
  noteToDeleteId = int(input())
  for note in Note.noteList:
    if noteToDeleteId == note.idNum:
      print("Are you sure you want to delete note #", noteToDeleteId, "?")
      print("Enter Y or N:") 
      if input() in ['y', 'Y']:
        note.delete()
        dbf.deleteNote(conn, c, noteToDeleteId)

###

def viewNotes():
  for note in Note.noteList:
    note.view()


###

def printNotes():
  for note in Note.noteList:
    note.print()


###

def commandOptions():
  print(commands)


###
# Main Function
###

def main():

  dbStuff = dbsetup()
  conn = dbStuff[0]
  c = dbStuff[1]

  userInput = begin()
  while True:
    if userInput in ['n', 'N']:
      print("Enter a note:")
      noteText = input()
      newNote(conn,c, noteText)
      userInput = nextCommand() 
    elif userInput in ['e', 'E']:
      editNote(conn,c)
      userInput = nextCommand()
    elif userInput in ['d', 'D']:
      deleteNote(conn,c)
      userInput = nextCommand()
    elif userInput in ['v', 'V']:
      viewNotes()
      userInput = nextCommand()
    elif userInput in ['p', 'P']:
      printNotes()
      userInput = nextCommand()
    elif userInput in ['c', 'C']:
      commandOptions()
      userInput = nextCommand()
    elif userInput in ['q', 'Q', 'x', 'X']:
      break
    #fast new note:
    else:
      newNote(conn, c, userInput)
      userInput = nextCommand()
    #add fast edit & fast delete below 
    #actually, add them above fast new note 
    #fast newnote should be the elif statement
 
  print("program exited by user")


###

if __name__ == "__main__":
  main()


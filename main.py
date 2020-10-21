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
  print("")
  conn = dbf.connect('noterista.db')

  print("checking notes table...")
  print("")
  c = dbf.table(conn)

  print("reading notes from table...")
  dbf.tableToNote(c)

  print("here are your notes...")
  for note in Note.noteList:
    note.view()
    print("")
  print("the next note will be #", Note.nextId)
  print("")

  dbstuff = [conn, c]
  return dbstuff


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

def newNote(conn, c):
  print("Enter a note:")
  userInput = input()
  noteId = Note.nextId
  note = Note(noteId, userInput)
  dbf.newNote(conn, c, noteId, userInput)

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
      if input() == "Y":
        note.delete()
        dbf.deleteNote(conn, c, noteToDeleteId)

###

def viewNotes():
  for note in Note.noteList:
    if note.delMarker == 0:
      note.view()
  for note in Note.noteList:
    note.print()
#keep second for loop for now, useful for testing

###

def commandOptions():
  print(commands)


###
# Main Function
###

def main():

  dbstuff = dbsetup()
  conn = dbstuff[0]
  c = dbstuff[1]

  userInput = begin()
  while True:
    if userInput == 'N':
      newNote(conn,c)
      userInput = nextCommand() 
    elif userInput == 'E':
      editNote(conn,c)
      userInput = nextCommand()
    elif userInput == 'D':
      deleteNote(conn,c)
      userInput = nextCommand()
    elif userInput == 'V':
      viewNotes()
      userInput = nextCommand()
    elif userInput == 'C':
      commandOptions()
      userInput = nextCommand()
    elif userInput == 'Q':
      break
     
  print("program exited by user")


###

if __name__ == "__main__":
  main()


# databasefunctions.py

import sqlite3
from sqlite3 import Error

from noteClass import Note


###

def connect(dbfile):
  try:
    conn = sqlite3.connect(dbfile)
    print(sqlite3.version)
  except Error as e:
    print(e)
  return conn


###

def table(conn):
  createNotesTable = """
  CREATE TABLE IF NOT EXISTS notes (
    ID integer PRIMARY KEY,
    Note text NOT NULL,
    DeleteMarker integer
  );"""

  try:
    c = conn.cursor()
    c.execute(createNotesTable)
  except Error as e:
    print(e)
  return c


###

def tableToNote(c):
  try:
    c.execute("SELECT * FROM notes")
    rows = c.fetchall()
    for row in rows:
      # print lines are for testing/clarification
      # print("from table: ")
      # print(row)
      # print("")
      # print("to note: ")
      idNum = row[0]
      noteText = row[1]
      delMarker = row[2]
      note = Note(idNum, noteText, delMarker)
      # note.view()
      # print("here is your noteList: ", Note.noteList)
      # print("here is your nextId: ", Note.nextId)
  except Error as e:
    print(e)


###

def newNote(conn, c, idNum, noteText):
  try:
    c.execute("INSERT INTO notes VALUES (?,?,?)", (idNum, noteText, 0))
    conn.commit()
  except Error as e:
    print(e)
    print("this is your dbf module speaking to you")


###

def editNote(conn, c, idNum, noteText):
  try:
    c.execute("UPDATE notes SET Note = ? WHERE ID = ?", (noteText, idNum))
    conn.commit()
  except Error as e:
    print(e)


###

def deleteNote(conn, c, idNum):
  try:
    c.execute("UPDATE notes SET DeleteMarker = ? WHERE ID = ?", (1, idNum))
    conn.commit()
  except Error as e:
    print(e)

 
###


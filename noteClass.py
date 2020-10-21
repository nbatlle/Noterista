# noteClass.py

class Note:

  """
  Note Class attributes that are functional as of 10/21:
    ID
    note text
    delete marker
  Attributes to implement next (not in order):
    task
    project
    date created
    date last edited

  The Note class is also responsible for keeping track of noteList and nextId, updated after every new note.
  """

  noteList = []
  nextId = 0

  def __init__(self, idNum, noteText, delMarker = 0):
    assert (idNum == Note.nextId), "uh oh, we have a problem!"
    # specifically for reading notes from db table during setup - make sure no skipping/repeating
    self.idNum = Note.nextId 
    self.noteText = noteText
    self.delMarker = delMarker
    Note.noteList.append(self)
    Note.nextId += 1


###
# currently view all notes done from main
# probably makes sense to move that implementation to Note class
###

  def view(self):
    print(self.idNum, self.noteText, self.delMarker)


###

  def edit(self, noteText):
    self.noteText = noteText
    print("note edited to read ", noteText)


###

  def delete(self):
    self.delMarker = 1
    print("note deleted")


###
# redundant w/ view(), but sometimes the different format is handy
# keep for now
###

  def print(self):
    print(self.idNum)
    print(self.noteText)
    print(self.delMarker)

###

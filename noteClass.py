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

  def edit(self, noteText):
    self.noteText = noteText
    print("note edited")


###

  def delete(self):
    self.delMarker = 1
    print("note deleted")


###
# view & print:
# update calls to both from main() to allow for view/print of a subset of notes (as in v:5-10)
# view will be user accessible command in final product
#   only shows relevant attributes - usually id and text
#   if note is task/project etc this will be noted w/ along w/ relevant attributes
#   if deleted prints note is deleted 
# use print for testing, shows all attributes
#   print() should be accessible via p command, but don't show command in menu
#   add SQL call to print row attributes from table as well as from notelist, make sure the agree
###

  def view(self):
    if self.delMarker == 0:
      print(self.idNum, self.noteText)
    else:
      print("note #", self.idNum, "has been deleted")
    # TODO: include relevant task/project attributes when those are implemented


  def print(self):
    print(self.idNum)
    print(self.noteText)
    print(self.delMarker)
    # TODO: add new attributes as they are implemented
    # TODO: SQL call

###

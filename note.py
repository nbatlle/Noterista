# note.py

class Note:

  """
  Note class properties will be a changing list while I work on various functionalities.
  In general class properties and db table columns should be aligned,
  but during development it's ok if I have more properties than columns.
  Properties as of now (10/16):
    ID
    note text
    delete marker
    task
    project
    date created
    date last edited
  (The last 4 haven't been implemented yet, just placeholders for now.)
  Need to decide whether SQL calls should go here, in main.py, or in their own module.
  """

  def __init__(self):
    self.idNum = -1
    self.noteText = ''
    self.delMarker = 0
    self.task = 0
    self.project = 0
    self.dateCreated = 0
    self.dateLastEdited = 0

###

  def new(self, nextId, noteText, delMarker = 0, task = 0, project = 0, dateCreated = 0, dateLastEdited = 0):

    # do I need a global nextId?
    # nextId needs to be updated back in main.py

    self.idNum = nextId
    self.noteText = noteText
    self.delMarker = delMarker
    self.task = task
    self.project = project
    self.created = dateCreated
    self.lastEdited = dateLastEdited 

    print("note # " + str(nextId) + " created")
    nextId += 1
    print("Id of next note is " + str(nextId))

###

  def table(self, note):
    self.idNum = note[0]
    self.noteText = note[1]
    self.delMarker = note[2]
    """
    # uncomment following lines after db table is updated w/ new properties
    self.task = note[3]
    self.project = note[4]
    self.dateCreated = note[5]
    self.dateLastEdited = note[6]
    # for now set all to default to 0
    """
    self.task = 0
    self.project = 0
    self.dateCreated = 0
    self.dateLastEdited = 0

    print("note # ", note[0], " updated from db table"

###

  def view(self):
    print(self.idNum, self.noteText)

###

  def edit(self, noteText):
    self.noteText = noteText

    print("note edited to read ", noteText)

###

  def delete(self)
    self.delMarker = 1
    print("note deleted")

###

  def print(self):
    print(self.idNum)
    print(self.noteText)
    print(self.delMarker)
    print(self.task)
    print(self.project)
    print(self.dateCreated)
    print(self.dateLastEdited)  

###

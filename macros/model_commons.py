class SCNObject(object):
  """docstring for SCNObject"""
  #name = ''
  #summary = ''
  #description = ''
  def __init__(self, name): self.name = name

  def setName(self, arg): self.name = arg

  def setSummary(self, arg): self.summary = arg

  def setDescription(self, arg): self.description = arg

class SCNEnumeration(SCNObject):
  """docstring for SCNClass"""
  #litterals = []
  def __init__(self, name):
    super(SCNEnumeration, self).__init__(name)
    #SCNObject.__init__(self, name)

class SCNClass(SCNObject):
  """docstring for SCNClass"""
  #attributes = []
  #operations = []
  #inheritsFrom = []

class SCNAttribute(SCNObject):
  """docstring for SCNAttribute"""
  #scn_type = ''
  #multiplicityMin = 1
  #multiplicityMax = 1

class SCNOperation(SCNObject):
  """docstring for SCNOperation"""
  #esgserg = ''

class SCNType(object):
  """docstring for SCNType"""

  @staticmethod
  def getType(self, _type):
    pass

"""
=========================================================
                       GenOCL.py
 Generate a USE OCL specification from a UML package
=========================================================

FILL THIS SECTION AS SHOWN BELOW AND LINES STARTING WITH ###
@author Julien Avert <avert.julien@gmail.com>
@author Mohammed Menber <mohammed.menber@gmail.com>
@group  G235

Current state of the generator
----------------------------------
FILL THIS SECTION
Explain which UML constructs are supported, which ones are not.
What is good in your generator?
What are the current limitations?

Current state of the tests
--------------------------
FILL THIS SECTION
Explain how did you test this generator.
Which test are working?
Which are not?

Observations
------------
Additional observations could go there
"""

#---------------------------------------------------------
#   Helpers on the source metamodel (UML metamodel)
#---------------------------------------------------------
# The functions below can be seen as extensions of the
# modelio metamodel. They define useful elements that
# are missing in the current metamodel but that allow to
# explorer the UML metamodel with ease.
# These functions are independent from the particular
# problem at hand and could be reused in other
# transformations taken UML models as input.
#---------------------------------------------------------

# example


def isAssociationClass(element):
  """
  Return True if and only if the element is an association
  that have an associated class, or if this is a class that
  has a associated association. (see the Modelio metamodel
  for details)
  """
  # TODO


#---------------------------------------------------------
#   Application dependent helpers on the source metamodel
#---------------------------------------------------------
# The functions below are defined on the UML metamodel
# but they are defined in the context of the transformation
# from UML Class diagramm to USE OCL. There are not
# intended to be reusable.
#---------------------------------------------------------

# example
def associationsInPackage(package):
  """
  Return the list of all associations that start or
  arrive to a class which is recursively contained in
  a package.
  """


#---------------------------------------------------------
#   Helpers for the target representation (text)
#---------------------------------------------------------
# The functions below aims to simplify the production of
# textual languages. They are independent from the
# problem at hand and could be reused in other
# transformation generating text as output.
#---------------------------------------------------------

def indent(something, level=0):
  return (level * '    ') + str(something)

# for instance a function to indent a multi line string if
# needed, or to wrap long lines after 80 characters, etc.

#---------------------------------------------------------
#           Transformation functions: UML2OCL
#---------------------------------------------------------
# The functions below transform each element of the
# UML metamodel into relevant elements in the OCL language.
# This is the core of the transformation. These functions
# are based on the helpers defined before. They can use
# print statement to produce the output sequentially.
# Another alternative is to produce the output in a
# string and output the result at the end.
#---------------------------------------------------------


def attributes2OCL(elem, indentLevel=0):
  if elem.ownedAttribute:
    print indent('attributes', indentLevel)
    for attr in elem.ownedAttribute:
      print indent('%s : %s%s' % (attr.name, basicType2OCL(attr.type.name), (' -- @derived' if attr.isDerived else '')), (indentLevel + 1))


def operations2OCL(elem, indentLevel=0):
  if elem.ownedOperation:
    print indent('operations', indentLevel)
    for op in elem.ownedOperation:
      ret = ''
      if op.return:
        ret = basicType2OCL(op.return.type.name)
        if op.return.multiplicityMax == '*':
          ret = 'Set(%s)' % ret
        ret = ' : %s' % ret
      # else if int(op.return.multiplicityMax) > 1:
      #  ret = '%s[%s]' % (ret, op.return.multiplicityMax)
      params = ''
      for param in op.IO:
        params += '%s : %s, ' % (param.name, basicType2OCL(param.type.name))
      params = params[:-2]
      print indent('%s(%s)%s' % (op.name, params, ret), (indentLevel + 1))


def basicType2OCL(type_):
  """
  Generate USE OCL basic type. Note that
  type conversions are required.
  """
  if type_ in ('integer', 'long', 'short'):
    return 'Integer'
  if type_ in ('float', 'double'):
    return 'Real'
  if type_ in ('string', 'char'):
    return 'String'
  if type_ in ('boolean'):
    return 'Boolean'
  return type_


def association2OCL(association_):
  kind = 'association'
  for end in association_.end:
    if end.aggregation == AggregationKind.KINDISCOMPOSITION:
      kind = 'composition'
    if end.aggregation == AggregationKind.KINDISAGGREGATION:
      kind = 'aggregation'
  print indent('%s %s between' % (kind, association_.name))
  for end in association_.end:
    card = ''
    if end.multiplicityMax == end.multiplicityMin:
      card = '[%s]' % end.multiplicityMax
    elif end.multiplicityMin == '0' and end.multiplicityMax == '*':
      card = '[*]'
    else:
      card = '[%s..%s]' % (end.multiplicityMin, end.multiplicityMax)
    #print indent('%s%s role %s' % (end.target.name, card, end.name), 1)
    print indent('%s%s role %s%s' % (end.oppositeOwner.owner.name, card, end.name, (' ordered' if end.isOrdered else '')), 1)
  print indent('end')


def associationClass2OCL(associationClass_):
  print indent('%sassociationclass %s between' % (('abstract ' if associationClass_.isAbstract else ''), associationClass_.name))
  for end in associationClass_.linkToAssociation.associationPart.end:
    card = ''
    if end.multiplicityMax == end.multiplicityMin:
      card = '[%s]' % end.multiplicityMax
    elif end.multiplicityMin == '0' and end.multiplicityMax == '*':
      card = '[*]'
    else:
      card = '[%s..%s]' % (end.multiplicityMin, end.multiplicityMax)
    print indent('%s%s role %s%s' % (end.target.name, card, end.name, (' ordered' if end.isOrdered else '')), 1)
  attributes2OCL(associationClass_)
  operations2OCL(associationClass_)
  print indent('end')


def class2OCL(class_):
  """
  Generate USE OCL code for the enumeration
  """
  parents = ''
  if class_.parent:
    parents += ' < '
    for p in class_.parent:
      parents += '%s, ' % p.superType.name
    parents = parents[:-2]
  print indent('%sclass %s%s' % (('abstract ' if class_.isAbstract else ''), class_.name, parents))
  attributes2OCL(class_)
  operations2OCL(class_)
  print indent('end')


def enumeration2OCL(enumeration_):
  """
  Generate USE OCL code for the enumeration
  """
  print indent('enum %s {' % enumeration_.name)
  values = ''
  for val in enumeration_.value:
    values += indent('%s,\n' % val.name, 1)
  print values[:-2]
  print indent('}')


def package2OCL(package_):
  """
  Generate a complete OCL specification for a given package.
  The inner package structure is ignored. That is, all
  elements useful for USE OCL (enumerations, classes,
  associationClasses, associations and invariants) are looked
  recursively in the given package and output in the OCL
  specification. The possibly nested package structure that
  might exist is not reflected in the USE OCL specification
  as USE is not supporting the concept of package.
  """
  print indent('model %s' % package_.name)


def buildModel(package_):
  # if package_.uuid not in models:
    #models[package_.uuid] = OCLModel(package_.name)
  for elem in package_.ownedElement:
    if isinstance(elem, Package):
      buildModel(elem)
    if isinstance(elem, Enumeration):
      # models[package_.uuid].addEnumeration(elem)
      model.addEnumeration(elem)
    if isinstance(elem, Class):
      # models[package_.uuid].addClass(elem)
      model.addClass(elem)


class OCLModel(object):

  """docstring for OCLModel"""

  classes = []
  associationClasses = []
  enumerations = []
  associations = {}

  def __init__(self, name):
    super(OCLModel, self).__init__()
    self.name = name

  def isEmpty(self):
    return len(self.classes) == len(self.associationClasses) == len(self.enumerations) == len(self.associations) == 0

  def addClass(self, class_):
    if class_.linkToAssociation:
      self.addAssociationClass(class_)
    else:
      self.classes.append(class_)

    for ass in class_.targetingEnd:
      self.addAssociation(ass.association)

  def addAssociationClass(self, assocClass_):
    self.associationClasses.append(assocClass_)

  def addEnumeration(self, enum_):
    self.enumerations.append(enum_)

  def addAssociation(self, assoc_):
    if assoc_.uuid not in self.associations and assoc_.linkToClass == None:
      self.associations[assoc_.uuid] = assoc_

  def generateOCL(self):
    if not self.isEmpty():
      package2OCL(self)
      for enum in self.enumerations:
        print ''
        enumeration2OCL(enum)
      for cla in self.classes:
        print ''
        class2OCL(cla)
      for ass in self.associations.values():
        print ''
        association2OCL(ass)
      for ass in self.associationClasses:
        print ''
        associationClass2OCL(ass)


#---------------------------------------------------------
#           User interface for the Transformation
#---------------------------------------------------------
# The code below makes the link between the parameter(s)
# provided by the user or the environment and the
# transformation functions above.
# It also produces the end result of the transformation.
# For instance the output can be written in a file or
# printed on the console.
#---------------------------------------------------------

# (1) computation of the 'package' parameter
# (2) call of package2OCL(package)
# (3) do something with the result
if len(selectedElements) == 1:
  elem = selectedElements[0]
# for elem in selectedElements:
  if isinstance(elem, Package):
    model = OCLModel(elem.name)
    buildModel(elem)

# for model in models.values():
model.generateOCL()

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

def indent(something, level = 0):
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

def generateAttributes(elem, indentLevel = 0):
    if elem.ownedAttribute:
        print indent('attributes', indentLevel)
        for attr in elem.ownedAttribute:
            print indent('%s : %s%s' % (attr.name, umlBasicType2OCL(attr.type.name), (' -- @derived' if attr.isDerived else '')), (indentLevel + 1))

def generateOperations(elem, indentLevel = 0):
    if elem.ownedOperation:
        print indent('operations', indentLevel)
        for op in elem.ownedOperation:
            print indent('%s()' % (op.name), (indentLevel + 1))


def umlBasicType2OCL(type_):
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

def umlClass2OCL(class_):
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

    generateAttributes(class_)

    generateOperations(class_)

    print indent('end')

def umlEnumeration2OCL(enumeration_):
    """
    Generate USE OCL code for the enumeration
    """
    print 'enum %s {'

    print '}'

# etc.

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
    for elem in package_.ownedElement:
        if isinstance(elem, Package):
            package2OCL(elem)
        if isinstance(elem, Enumeration):
            umlEnumeration2OCL(elem)
        if isinstance(elem, Class):
            umlClass2OCL(elem)

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

for elem in selectedElements:
    if isinstance(elem, Package):
        package2OCL(elem)

import model_commons as model
# reload(model_commons) !!!

classes = []
enums = []


def create_enum(enum):
	name = enum.getName()
	summary = ''
	description = ''
	for desc in enum.getDescriptor():
		if desc.getModel().getName() == 'summary':
			summary = desc.getContent()
		elif desc.getModel().getName() == 'description':
			description = desc.getContent()

	scnenum = model.SCNEnumeration(name)
	#scnenum.setName(name)
	scnenum.setSummary(summary)
	scnenum.setDescription(description)
	enums.append(scnenum)

def parse_package(pkg):
	for elem in pkg.ownedElement:
		if isinstance(elem, Package):
			pass
		if isinstance(elem, Enumeration):
			create_enum(elem)
		if isinstance(elem, Class):
			pass

if len(selectedElements) == 1:
	elem = selectedElements[0]
# for elem in selectedElements:
if isinstance(elem, Package):
	parse_package(elem)

for e in enums:
	print e.name
	if e.summary:
		print '    S: %s' % e.summary
	if e.description:
		print '    D: %s' % e.description

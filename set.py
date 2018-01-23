import pprint

sipc = {'lewei', 'peiyun', 'yan'}
ieg = {'ting', 'wamei', 'yan'}
face = {'lewei','zehuan'}

pprint.pprint(sipc.union(ieg))
pprint.pprint(sipc.difference(face))
pprint.pprint(sipc.intersection(ieg))

print("yan" in ieg)
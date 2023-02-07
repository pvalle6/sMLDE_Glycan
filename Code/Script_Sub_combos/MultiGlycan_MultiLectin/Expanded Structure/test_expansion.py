expansion = '(b1-4)RibOP-ol(5-1)RibOP-ol(5-3)GalNAC(b1-3)GlcNAC'
repeat = 'GlcA(b1-3)Xyl(a1-3)'
base = 'GlcA(b1-4)Xyl'
units_add = ''
glycans = []
for i in range(10):
	units_add = ''
	for y in range(i):
		units_add = units_add + repeat
	glycans.append(units_add + base + expansion)

print(glycans)
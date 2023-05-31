"""Library for use in Lectin-Matriglycan Project"""


def generate_matriglycan(length: int) -> list:
    """Generates a matriglycan IUPAC-condensed from length"""
    expansion = '(b1-4)RibOP-ol(5-1)RibOP-ol(5-3)GalNAc(b1-3)GlcNAc(b1-4)Man'
    repeat = 'GlcA(b1-3)Xyl(a1-3)'
    base = 'GlcA(b1-4)Xyl'
    units_add = ''
    glycans = []
    for i in range(length):
        units_add = ''
        for y in range(i):
            units_add = units_add + repeat
        glycans.append(units_add + base + expansion)
    return glycans

from lectinmatpack.functions import generate_matriglycan


def test_pos():
    assert generate_matriglycan(5,True) == ['GlcA(b1-4)Xyl(b1-4)RibOP-ol(5-1)RibOP-ol(5-3)GalNAc(b1-3)GlcNAc(b1-4)Man',
                                       'GlcA(b1-3)Xyl(a1-3)GlcA(b1-4)Xyl(b1-4)RibOP-ol(5-1)RibOP-ol(5-3)GalNAc(b1-3)GlcNAc(b1-4)Man',
                                       'GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-4)Xyl(b1-4)RibOP-ol(5-1)RibOP-ol(5-3)GalNAc(b1-3)GlcNAc(b1-4)Man',
                                       'GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-4)Xyl(b1-4)RibOP-ol(5-1)RibOP-ol(5-3)GalNAc(b1-3)GlcNAc(b1-4)Man',
                                       'GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-4)Xyl(b1-4)RibOP-ol(5-1)RibOP-ol(5-3)GalNAc(b1-3)GlcNAc(b1-4)Man']
def test_neg():
    assert generate_matriglycan(5,False) == ['GlcA(b1-4)Xyl',
                                       'GlcA(b1-3)Xyl(a1-3)GlcA(b1-4)Xyl',
                                       'GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-4)Xyl',
                                       'GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-4)Xyl',
                                       'GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-4)Xyl']
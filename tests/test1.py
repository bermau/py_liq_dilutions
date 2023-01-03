from  liquid_dilutions import *


mater = Liquid("COVID")
diluent = Liquid("Diluent")
tube1 = Aliquot(mater, 200, 154)
tube_ct_mere = Aliquot(mater, 500, ct=20.5, unit_type='ct')


print(tube1)
print(tube2)
preparer(200, 15, tube1)
preparer(200, 35, tube_ct_mere, comment=True)


fille_de_mere = diluer(tube_ct_mere, 10)
print(fille_de_mere)
print(fille_de_mere['tube_fille'].ct)


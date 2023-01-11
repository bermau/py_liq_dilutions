from  liquid_dilutions import *


mater = Liquid("COVID")
diluent = Liquid("Diluent")

tube_as_cc = Aliquot(mater, 200, 154)
tube_ct_mere = Aliquot(mater, 500, ct=20.5, unit_type='ct')

# mater = Liquid("COVID_Pos")
# diluent = Liquid("Diluent")
tube1 = Aliquot(mater, 210, 154)
tube2 = Aliquot(diluent, 1100, 0)



print(tube_as_cc)

print(tube2)

preparer(200, 15, tube_as_cc)
preparer(200, 35, tube_ct_mere, comment=True)


fille_de_mere = diluer(tube_ct_mere, 10)
print(fille_de_mere)
print(fille_de_mere['tube_fille'].ct)


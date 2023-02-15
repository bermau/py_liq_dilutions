# Exemple avec
"""Exemple d'utilisation """
from liquid_dilutions import *

mater = Liquid("COVID JAL/BEA")
diluent = Liquid("UTM")

tube_ct_mere = Aliquot(mater, volume=500, ct=15, unit_type='ct')

# On a un CT à 20,5 et on veut l'amener vers 33


print(f"""\nSOLUTION DEPART :
  ** {tube_ct_mere} 
  ** Caractéristiques : {tube_ct_mere.describe()}
       """)

dil_imposes = [[300, 1000]]  # [[dilution, volume]  ...]


res = preparer(vf=2000, ct_cc_cible=33, tube=tube_ct_mere, n_dil=3
               # , lst_imposed_dil=dil_imposes
               , comment=True)
print()
for item in res:
    print(item)

# Exemple avec
"""Exemple d'utilisation """
from liquid_dilutions import *

mater = Liquid("Ceph_PEYMAT_FluA")
diluent = Liquid("UTM")

tube_ct_mere = Aliquot(mater, volume=500, ct=17.1, unit_type='ct')

# On a un CT à 20,5 et on veux l'amener vers 33


print(f"""\nSOLUTION DEPART :
  ** {tube_ct_mere} 
  ** Caractéristiques : {tube_ct_mere.describe()}
       """)

dil_imposes = [[50, 2000]]  # [[dilution, volume]  ...]

# res = preparer(vf=3, ct_cc_cible=30, tube=tube_ct_mere, n_dil=3,
#                lst_imposed_dil=dil_imposes, comment=True)

res = preparer(vf=1000, ct_cc_cible=33, tube=tube_ct_mere, n_dil=2
               # , lst_imposed_dil=dil_imposes
               , comment=True)
print()
for item in res:
    print(item)

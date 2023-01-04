"""Exemple d'utilisation """
from liquid_dilutions import *

mater = Liquid("VRS")
diluent = Liquid("UTM")

tube_ct_mere = Aliquot(mater, volume=500, ct=20.5, unit_type='ct')

# On a un CT à 20,5 et on veux l'amener vers 33


print(f"""\nSOLUTION DEPART :
  ** {tube_ct_mere} 
  ** Caractéristiques : {tube_ct_mere.describe()}
       """)
dil_imposes = [[25, 200]]  # [[dilution, volume]  ...]

# res = preparer(vf=3, ct_cc_cible=30, tube=tube_ct_mere, n_dil=3,
#                lst_imposed_dil=dil_imposes, comment=True)

res = preparer(vf=3000, ct_cc_cible=30, tube=tube_ct_mere, n_dil=2
               , lst_imposed_dil=dil_imposes
               , comment=True)
print()
for item in res:
    print(item)

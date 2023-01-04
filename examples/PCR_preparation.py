"""Exemple d'utilisation """
from liquid_dilutions import *

mater = Liquid("COVID")
diluent = Liquid("UTM")

tube_ct_mere = Aliquot(mater, volume=500, ct=20.5, unit_type='ct')

# On a un CT à 20,5 et on veux l'amener vers 33


print(f"""\nSOLUTION DEPART :
  ** {tube_ct_mere} 
  ** Caractéristiques : {tube_ct_mere.describe()}
       """)
dil_imposes = [[15, 200], [25, 210]]  # [[dilution, volume]  ...]
res = preparer(vf=2500, ct_cc_cible=33, tube=tube_ct_mere, n_dil=3,
               lst_imposed_dil=dil_imposes, comment=True)
print()
for item in res:
    print(item)

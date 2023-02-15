# Exemple trouver la concentration initiale d'une solution dont la dilution au 1/N vaut x CT.

from liquid_dilutions import *
import math

data = [{'nom': Liquid("GAI_VAL_vrs"), 'mesure': 29.3, 'dilution': 5792.62},
        {'nom': Liquid("PEY_MAT_Grp"), 'mesure': 27.4, 'dilution': 247.28},
        {'nom': Liquid("JAL_BEA_Cov"), 'mesure': 32.05, 'dilution': 64 * 64},
        ]

for exper in data:
    ct_init = nice(calcul_concentration_initiale(exper['dilution'], exper['mesure']))
    print(f"Pour {exper['nom']}, la mesure au 1/ {exper['dilution']} est {exper['mesure']}. La cc initiale = {ct_init}")

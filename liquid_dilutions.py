#!/usr/bin/env python
# coding: utf-8

# # Utilitaire pour la dilution simple
# Quelques fonctions pour définir un liquide contenu dans un tube et préparer des dilutions.
# La concentration du liquide peut être exprimée en concentration (pour la chimie usuelle) ou en CT (pour la PRC). 

import math


def nice(flt):
    return "{:.2f}".format(flt)


# # Définition des classes Liquid et Aliquot


class Liquid:
    def __init__(self, name, tag=''):
        """define a liquid by it name. Possibility to add a tag (example : pure, dil 1, dil 2)"""
        self.name = name
        self.tag = tag

    def __repr__(self):
        if self.tag:
            return f"<Liquid : {self.name}/{self.tag}>"
        else:
            return f"<Liquid : {self.name}>"


class Aliquot:
    def __init__(self, liquid: Liquid, volume, concentration=None, ct=None, unit_type='cc', ):
        """La solution est en concentration, sauf si ct est indiquée.
        """
        self.liquid = liquid
        self.volume = volume
        self.unit_type = unit_type
        if unit_type == 'cc':
            self.concentration = concentration
        elif unit_type == 'ct':
            self.ct = ct

    def __repr__(self):
        if self.unit_type == "cc":
            return f"<Aliquot, vol : {self.volume} contenant {self.liquid}>"
        if self.unit_type == "ct":
            return f"<Aliquot, vol : {self.volume} contenant {self.liquid}>"

    def describe(self):
        common = f"  Tube de type {self.unit_type}"
        if self.unit_type == 'ct':
            return common + f", CT : {self.ct}"
        else:
            return common + f", CC : {self.concentration}"

mater = Liquid("COVID_Pos")
diluent = Liquid("Diluent")
tube1 = Aliquot(mater, 210, 154)
tube2 = Aliquot(diluent, 1100, 0)


# # Dilution d'un liquide aliquoté dans un tube

def diluer(tube: Aliquot, dilution=5, volume_final=100, tag='fille', comment=False):
    """Préparer une solution fille par dilution d'une solution mère."""
    source_v = volume_final / dilution
    diluent_v = volume_final - source_v
    liquid_fille = Liquid(tube.liquid.name, tag)
    tube_fille = None
    if tube.unit_type == 'cc':
        tube_fille = Aliquot(liquid_fille, volume_final, concentration=tube.concentration / dilution, unit_type='cc')
    elif tube.unit_type == 'ct':
        tube_fille = Aliquot(liquid_fille, volume_final, ct=tube.ct + math.log(dilution, 2), unit_type='ct')

    if comment:
        print(f"Prélever {nice(source_v)} µl de solution mère {tube}, ajouter {nice(diluent_v)} de diluent ")
        print(f"En sortie on aura le tube : {tube_fille}")

    return {'vol_mere': source_v, 'vol_diluent': diluent_v, 'tube_fille': tube_fille}


class Pipette:
    def __init__(self, nom, mini, maxi):
        self.name = nom
        self.min = mini
        self.max = maxi


P1000 = Pipette("Pip 1000", 100, 900)
P200 = Pipette("Pip 200", 10, 200)


def preparer(vf, ct_cc_cible, tube, n_dil=1, lst_imposed_dil=None, comment=False):
    """
    Obtenir un volume vf à concentration finale de CT ct_cc_cible à partir d'un Aliquot en tube dont le CT est connu
    lst_imposed_dil est une liste de dilutions pour forcer les première dilutions
    """
    # produit
    dilution = 1
    if tube.unit_type == 'cc':
        dilution = tube.concentration / ct_cc_cible
    elif tube.unit_type == 'ct':
        dilution = pow(2, ct_cc_cible - tube.ct)

    dilution_elementaire = dilution ** (1 / n_dil)

    if comment:
        print(f"préparer une dilution finale au : {nice(dilution)}")

    if n_dil == 1:
        dico = diluer(tube1, dilution=dilution, volume_final=vf, comment=True)
        return [dico]

    elif n_dil > 1:
        list_dil = []
        if lst_imposed_dil:
            # Verifier n_dil sup a liste
            assert len(lst_imposed_dil) < n_dil
            if comment:
                print("Nous allons préparer les dilution imposées puis les libres")
            # retour_tube = None  # {} # contiendra la succession des dilutions
            tube_en_cours_de_dil = tube

            for i in range(n_dil):
                if i < len(lst_imposed_dil):
                    print("\ndilution imposée", i + 1)
                    print(f"   on dilue au 1/{lst_imposed_dil[i][0]} en volume de {lst_imposed_dil[i][1]} µl")
                    data_tube = diluer(tube_en_cours_de_dil, dilution=lst_imposed_dil[i][0],
                                         volume_final=lst_imposed_dil[i][1],
                                         tag="imposé_" + str(i + 1), comment=True)
                    list_dil.append(data_tube)
                    print(data_tube['tube_fille'].describe())
                    tube_en_cours_de_dil = data_tube['tube_fille']
                else:
                    produit_des_dilutions = 1
                    dils = [item[0] for item in lst_imposed_dil]
                    for dil in dils:
                        produit_des_dilutions *= dil
                    dilution_restante = dilution / produit_des_dilutions
                    print(f"\nLe produit des dilutions imposées est {produit_des_dilutions}. "
                          f"Il reste une dilution au {dilution_restante}")
                    data_last_tube = diluer(tube_en_cours_de_dil, dilution=dilution_restante,
                                       volume_final=vf,
                                       tag="calculé_" + str(i + 1), comment=True)
                    list_dil.append(data_last_tube)
        else:
            # N dilutions successives identiques
            if comment:
                print(f"Nous allons préparer {n_dil} dilutions au {nice(dilution_elementaire)}")
            for i in range(0, n_dil):
                print("dilution", i + 1)
                dico = diluer(tube, dilution=dilution_elementaire, tag='dil_' + str(i + 1), volume_final=vf,
                              comment=True)
                list_dil.append(dico)

        return list_dil


if __name__ == '__main__':
    tube_ct_mere = Aliquot(mater, 500, ct=20.5, unit_type='ct')
    # preparer(200, 35, tube_ct_mere, comment=True)
    # print()
    # preparer(800, 35, tube_ct_mere, n_dil=3, comment=True)
    # print()
    ret = preparer(800, 35, tube_ct_mere, n_dil=3, lst_imposed_dil=[[10, 550], [10, 120]], comment=True)
    # preparer(800, 35, tube_ct_mere, n_dil=3, lst_imposed_dil=[[100, 550], [50, 120]], comment=True)
    for item in ret :
        print(item)
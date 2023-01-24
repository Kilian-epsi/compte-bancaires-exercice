import uuid
from abc import ABC

from src.exception import MontantMinAtteint, MontantNegatif


class Compte(ABC):
    """
        Abstract class Compte
    """

    def __init__(self, nomProprietaire="Default User", **kwargs):
        self.nomProprietaire = nomProprietaire
        self.numeroCompte = uuid.uuid1()
        self.limiteMin = 1000
        self.solde = 0
        for key, value in kwargs.items():
            setattr(self, key, value)

    def retrait(self, montant=0):
        pass

    def versement(self, montant=0):
        try:
            if montant > 0:
                self.solde += montant
            else:
                raise MontantNegatif('\033[1;31mImpossible de verser un montant négatif! \033')
        except MontantNegatif:
            print('\033[1;31mImpossible de verser un montant négatif! \033')

    def afficherSolde(self):  # pragma: no cover
        result = "{total:.2f}€"
        return result.format(total=self.solde)

    def __repr__(self):
        return ""


class CompteCourant(Compte):
    def __init__(self, nomProprietaire, **kwargs):
        super().__init__(nomProprietaire, **kwargs)
        self.agios = 10/100

    def retrait(self, montant=0):
        try:
            if montant > 0:
                try:
                    if self.solde - montant > -self.limiteMin:
                        self.solde -= montant
                    else:
                        raise MontantMinAtteint("\033[1;31mVous ne pouvez pas dépasser le montant de -1000€\033")
                except MontantMinAtteint:
                    print("\033[1;31mVous ne pouvez pas dépasser le montant de -1000€\033")
            else:
                raise MontantNegatif('\033[1;31mImpossible de verser un montant négatif ! \033')
        except MontantNegatif:
            print('\033[1;31mImpossible de verser un montant négatif! \033')
        if self.solde < 0:
            self.appliquer_agios()

    def appliquer_agios(self):
        self.solde += self.agios * self.solde


class CompteEpargne(Compte):
    def __init__(self, nomProprietaire, **kwargs):
        super().__init__(nomProprietaire, **kwargs)
        self.limiteMin = 0
        self.interet = 20 / 100

    def retrait(self, montant=0):
        try:
            if montant > 0:
                try:
                    if self.solde - montant > -self.limiteMin:
                        self.solde -= montant
                    else:
                        raise MontantMinAtteint("\033[1;31mVous ne pouvez pas dépasser le montant de 0\033")
                except MontantMinAtteint:
                    print("\033[1;31mVous ne pouvez pas dépasser le montant de 0\033")
            else:
                raise MontantNegatif('\033[1;31mImpossible de verser un montant négatif! \033')
        except MontantNegatif:
            print('\033[1;31mImpossible de verser un montant négatif! \033')

    def versement(self, montant=0):
        try:
            if montant > 0:
                self.solde += montant
            else:
                raise MontantNegatif('\033[1;31mImpossible de verser un montant négatif! \033')
        except MontantNegatif:
            print('\033[1;31mImpossible de verser un montant négatif! \033')
        self.appliquer_interet()

    def appliquer_interet(self):
        self.solde += self.interet * self.solde

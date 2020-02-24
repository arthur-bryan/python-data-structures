#! /usr/bin/python3.7
# -*- coding: utf-8 -*-

def calcular_tmb(peso_metabolico, grupo):
    """
    :param peso_metabólico e grupo:
    :return TMB resultante:
    """
    if grupo.lower() == "passeiformes":
        k = 129
    elif grupo.lower() == "não passeriformes":
        k = 78
    elif grupo.lower() == "mamíferos placentários":
        k = 70
    elif grupo.lower() == "marsupiais e edenatas":
        k = 49
    elif grupo.lower() == "répteis":
        k = 10
    else:
        return "Grupo inválido! Verifique o nome e a acentuação."
    return f"O TMB resultante é: {(peso_metabolico ** 0.75) * k}."

def main():
    """
    Recebe o peso do animal, qual grupo ele pertence e imprime a TMB resultante.
    """
    peso_metabolico = float(input("Informe o peso metabólico do animal: "))
    grupo = input("A qual grupo o animal pertence? ")
    print(calcular_tmb(peso_metabolico, grupo))



if __name__ == '__main__':
    main()

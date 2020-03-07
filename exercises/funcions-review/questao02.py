# !/usr/bin/python3.7
# -*- coding: utf-8 -*-


def calcular_taxa(peso_metabolico, grupo, potencia):
    """
    :param peso metabólico, grupo e potencia:
    :return Resultado da respectiva taxa:
    """
    if potencia == 0.25:
        taxa = 'taxa metabólica específica'
    else:
        taxa = 'taxa betabólica basal'

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
    return f"A {taxa} é: {(peso_metabolico ** potencia) * k}."


def definir_calculo(peso_metabolico, grupo, letra):
    """
    :param peso metabólico, grupo e letra:
    :return resultado da respectiva tacha (de acordo com a letra):
    """
    if letra.upper() == 'B':
        return calcular_taxa(peso_metabolico, grupo, 0.75)
    elif letra.upper() == 'E':
        return calcular_taxa(peso_metabolico, grupo, 0.25)
    else:
        return f"Flag inválida! Escolha 'E' ou 'B'."


def main():
    peso_animal = float(input("Informe o peso metabólico do animal: "))
    grupo_animal = input("A qual grupo o animal pertence? ")
    letra = input("Informe a letra da taxa correspondente (E/B): ")
    print(definir_calculo(peso_animal, grupo_animal, letra))


if __name__ == '__main__':
    main()

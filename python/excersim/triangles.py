#!/usr/bin/env python3
def inequality_violation(lista):
    if len(lista) != 3:
        raise ValueError("La lista debe contener exactamente tres elementos")
    a, b, c = lista

    # Verificar si cualquier valor es mayor que la suma de los otros dos
    if a > b + c or b > a + c or c > a + b:
        return True
    return False


def son_todos_diferentes_de_cero(lista):
    for elemento in lista:
        if elemento == 0:
            return False
    return True


def equilateral(sides):
    if len(set(sides)) == 1 and son_todos_diferentes_de_cero(sides):
        return True
    return False


def isosceles(sides):
    if not inequality_violation(sides):
        if len(set(sides)) == 2 or equilateral(
                sides) and son_todos_diferentes_de_cero(sides):
            return True
        return False
    return False


def scalene(sides):
    if not inequality_violation(sides):
        if len(set(sides)) == 3 and son_todos_diferentes_de_cero(sides):
            return True
    return False

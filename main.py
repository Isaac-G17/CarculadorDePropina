nombre = input("Por favor ingrese su nombre =")
precio_de_comida = float(input("Por favor ingrese el precio de su comida ="))


if precio_de_comida < 20:

    propina = precio_de_comida * 0.10

    print("El valor de la propina es:", propina)
    print("El total a pagar es:", precio_de_comida + propina)

elif precio_de_comida >= 20 and precio_de_comida <= 50:

    propina = precio_de_comida * 0.15

    print("El valor de la propina es:", propina)
    print("El total a pagar es:", precio_de_comida + propina)

else:
    propina = precio_de_comida * 0.20

    print("El valor de la propina es:", propina)
    print("El total a pagar es:", precio_de_comida + propina)

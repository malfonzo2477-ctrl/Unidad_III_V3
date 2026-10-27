# Validamos que la cantidad sea un entero mayor que cero
if cantidad <= 0:
    print("Error: La cantidad de números a analizar debe ser mayor que cero.")
else:
    # contadores y acumulador antes de entrar al ciclo
    positivos = 0
    negativos = 0
    ceros = 0
    suma_total = 0.0

    # Ciclo for para iterar la cantidad exacta 
    for i in range(1, cantidad + 1):
        num = float(input(f"Ingrese el número {i}: "))

        # Sumamos al acumulador
        suma_total += num

        # Condicionales para clasificar cada número
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1
        else:
            ceros += 1

    # Calculamos el promedio
    promedio = suma_total / cantidad

    # Formateamos la suma si es un entero exacto para coincidir con la salida del ejemplo
    if suma_total == int(suma_total):
        suma_imprimir = int(suma_total)
    else:
        suma_imprimir = f"{suma_total:.2f}"

    # Mostramos los resultados finales
    print(f"Cantidad de positivos: {positivos}")
    print(f"Cantidad de negativos: {negativos}")
    print(f"Cantidad de ceros: {ceros}")
    print(f"Suma total: {suma_imprimir}")
    print(f"Promedio: {promedio:.2f}")
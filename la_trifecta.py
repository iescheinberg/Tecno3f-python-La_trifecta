
while True:
    # Solicitar el número al usuario.
    numero = input("Ingrese un numero mayor a 0 para iniciar (o cualquier otro caracter para salir): ")
    
    # Verificar si el valor ingresado es un numero y si este es mayor a 0.
    if not numero.isdigit() or int(numero) <= 0:
        print("Ha salido del programa.")
        break
    
    # Convertir tipo de dato a int number
    numero = int(numero)
    
    # Solicitar el palabra o frase al usuario.
    palabra = input("Ingrese una palabra o frase: ")
    
    # Calcular número de caracteres de la palabra o frase.
    numero_caracteres = len(palabra)
    print(f"El numero de caracteres de la palabra o frase es: {numero_caracteres}")
    
    # Calcular el factorial del numero de caracteres de la palabra o frase ingresada.
    resultado = 1
    for i in range(1, numero_caracteres + 1):
        resultado *= i
    
    # Imprimir el resultado.
    print(f"El factorial del número es: {resultado}")
    
    # Determinamos si el resultado es par o impar.
    if resultado % 2 == 0:
        print("El factorial es par.")
    else:
        print("El factorial es impar.")
    
    print("-" * 80)


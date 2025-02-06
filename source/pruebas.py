import os

def limpiar_pantalla():
    """Limpia la terminal según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def calculadora():
    while True:
        limpiar_pantalla()  # Limpia la pantalla al inicio del bucle
        try:
            # Mostrar el menú principal con diseño amigable
            print("############################################")
            print("#          CALCULADORA INTERACTIVA         #")
            print("############################################")
            print("\nSeleccione la operación que desea realizar:")
            print("[1] Suma")
            print("[2] Resta")
            print("[3] Multiplicación")
            print("[4] División")
            print("[0] Salir")
            print("############################################")

            # Solicitar la operación
            operacion = int(input("Ingrese el número de la operación deseada: "))

            # Salir del programa si se selecciona 0
            if operacion == 0:
                print("\nGracias por usar la calculadora. ¡Hasta luego!")
                break
            elif operacion in [1, 2, 3, 4]:
                # Solicitar números al usuario
                num1 = float(input("\nIngrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))

                # Mostrar el resultado según la operación seleccionada
                print("\n############################################")
                if operacion == 1:
                    print(f"Resultado: {num1} + {num2} = {num1 + num2}")
                elif operacion == 2:
                    print(f"Resultado: {num1} - {num2} = {num1 - num2}")
                elif operacion == 3:
                    print(f"Resultado: {num1} * {num2} = {num1 * num2}")
                elif operacion == 4:
                    if num2 != 0:
                        print(f"Resultado: {num1} / {num2} = {num1 / num2}")
                    else:
                        print("Error: No se puede dividir entre cero.")
                print("############################################")

                # Pausa para que el usuario pueda leer el resultado
                input("\nPresione Enter para continuar...")
            else:
                print("\nOperación no válida. Por favor, seleccione una opción válida.")
                input("\nPresione Enter para continuar...")
        except ValueError:
            print("\nError: Por favor, ingrese un número válido.")
            input("\nPresione Enter para continuar...")
        except Exception as e:
            print(f"\nOcurrió un error inesperado: {e}")
            input("\nPresione Enter para continuar...")

# Llamar a la función calculadora si el script es ejecutado directamente
if __name__ == "__main__":
    calculadora()

import random
import string

def generate_password(length, use_upper, use_lower, use_numbers, use_special, use_spaces):
    charset = ""
    password = []
    if use_upper:
        charset += string.ascii_uppercase
    if use_lower:
        charset += string.ascii_lowercase
    if use_numbers:
        charset += string.digits
    if use_special:
        charset += "!@#$%^&*()_+"
    if use_spaces:
        charset += " "  
        password.append(" ")

    if not charset:
        print("Error: No hay caracteres seleccionados.")
        return None

    return ''.join(random.choice(charset) for _ in range(length))

def validate_selection(options):
    return sum(options) == 3

while True:
    print("Selecciona el nivel de seguridad:")
    print("1. Bajo (8 caracteres)")
    print("2. Medio (12 caracteres)")
    print("3. Alto (16 caracteres o más)")
    try:
        security_level = int(input("Elige el nivel de seguridad (1, 2 o 3): "))
        if security_level == 1:
            length = 8
        elif security_level == 2:
            length = 12
        elif security_level == 3:
            length = 16
        else:
            print("Por favor, selecciona una opción válida (1, 2 o 3).")
            continue
        break
    except ValueError:
        print("Por favor, ingresa un número válido (1, 2 o 3).")

while True:
    print("Selecciona 3 de las 5 siguientes opciones:")
    use_upper = input("Incluir letras mayúsculas (y/n): ").lower() == 'y'
    use_lower = input("Incluir letras minúsculas (y/n): ").lower() == 'y'
    use_numbers = input("Incluir números (y/n): ").lower() == 'y'
    use_special = input("Incluir caracteres especiales (y/n): ").lower() == 'y'
    use_spaces = input("Incluir espacios en blanco (y/n): ").lower() == 'y'

    if validate_selection([use_upper, use_lower, use_numbers, use_special, use_spaces]):
        break
    else:
        print("Debes seleccionar exactamente 3 opciones. Inténtalo de nuevo.")

password = generate_password(length, use_upper, use_lower, use_numbers, use_special, use_spaces)
if password:
    print(f"Tu contraseña generada es: {password}")

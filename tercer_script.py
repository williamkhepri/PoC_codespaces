# Generar passwords fuertes
import random
import string 
# Este script genera passwords de 18 caracteres
word_length = 18

# Generar una lista de letras, digitos, y signos de puntuación
components = [string.ascii_letters, string.digits, "!@#$%&"]
# Metiendo los componentes en una lista de caracteres
chars = []
for clist in components: 
    for item in clist:
        chars.append(item)
def generate_password():
    # Almacenamos la contraseña generada
    password = []
    # Elegimos un random item de 'chars' y lo añadimos a 'password'
    for i in range(word_length):
        rchar = random.choice(chars)
        password.append(rchar)
    # Devolvemos el password creado como un string
    return "".join(password)
# Mostramos el password por consola
print(generate_password())
import re

codigo_postal = input("Ingrese su codigo postal aqui: ")

def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    verificar = re.search(patron, cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")


verificar_cp(codigo_postal)
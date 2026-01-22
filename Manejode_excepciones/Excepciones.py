from Numeros_identicos_exception import NumerosIdenticosException
resultado = None
try:
    a = int(input("Primer numero: "))
    b = int(input("Segundo numero: "))
    if a  == b:
        raise NumerosIdenticosException("Numeros identicos")
    resultado = a / b
except ZeroDivisionError as zde:
    print(f"Ocurrio un error: {zde}, {type(zde)}")
except TypeError as te:
    print(f"Ocurrio un error: {te},{type(te)}")
except ValueError as ve:
    print(f"Ocurrio un error: {ve},{type(ve)}")
except Exception as e:
    print(f"Ocurrio un error: {e},{type(e)}")

else:
    print("No se arrojó nínguna excepción")

finally:
    print("Ejecucion de bloque finally")
print(f"Resultado: {resultado}")
print("Continuamos...")
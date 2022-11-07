

# try:
#     n = int(input("Ingrese N: "))
#     m = 5

#     print(f"{n}/{m} = {n/m}")

# except:
#     print("error")

# print("Despues del try")

def dividir(a,b):
    return a/b

try:
    a = int(input("Ingrese primer número: "))
    b = int(input("Ingrese segundo número: "))

    resultado = dividir(a,b)
    print(resultado)
except TypeError:
    print("No se puede hacer operaciones con tipos de datos distintos")
except ValueError:
    print("Tenes que digitar números")
except ZeroDivisionError:
    print("No se puede dividir un número entre 0")
except Exception as e:
    print("Excepción no capturada antes: ", type(e).__name__)

print("casa")
print("casaaaaaa")

# except Exception as error:
#     tipo_error = type(error).__name__
#     print("El tipo error", tipo_error)

#     if tipo_error == "ZeroDivisionError":
#         print("NO se puede dividir entre 0")



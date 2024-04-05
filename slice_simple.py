def slice_simple():
    texto = "Awesome"
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.
    texto = ("Awesome")
    print (texto[0:3].lower())
    medio = len (texto)//2
    print (texto[medio -1:medio +2].lower())
    print (texto[0:4].lower()+texto[-3:])


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`

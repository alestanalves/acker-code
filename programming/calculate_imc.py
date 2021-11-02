def calculate_imc(peso: int, altura: int) -> float:
    """Calculando o indice de massa corporal"""

print(calculate_imc.__name__)
# Resultado calculate_imc
print(calculate_imc.__doc__)
# Resultado Calculando o indice de massa corporal
print(calculate_imc.__annotations__)
# Resultado {'peso': <class 'int'>, 'altura': <class 'int'>, 'return': <class 'float'>}
print(calculate_imc.__code__.co_varnames)
# Resultado ('peso', 'altura')

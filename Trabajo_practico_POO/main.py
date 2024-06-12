# main de mi main

from Electronico import Electronico
from Alimento import Alimento

celular1 = Electronico("Nokia", 100.26, 50, "Nokia", "Nokia 1100",100)
alimento_congelado1 = Alimento("Pizza congelada", 3899, 200, "2024-8-12")

print(celular1.mostrar_informacion())
print(alimento_congelado1.mostrar_informacion())


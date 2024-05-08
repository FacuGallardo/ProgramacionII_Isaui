import random

numero_aleatorio = random.randint(1,100)
def jugar_adivinar_numero() :
    intento = 0
    print("Estoy pensando en cuantos dolares me debes... entre 1 y 100")
    
    while True:
        intento = int(input("En que numero estoy pensando?:"))
        intento += 1
        
        if intento < numero_aleatorio:
            print("Mas bajo que estatura de Juan, subale subale!!!")
        
        elif intento > numero_aleatorio:
            print("Mas alto que jirafa, baje baje!!!")
            
        else:
            print("Felicidades!!!, usted sabe la deuda que tiene conmigo, es {intento} asi que vaya pagando")
            
            break
        jugar_adivinar_numero()
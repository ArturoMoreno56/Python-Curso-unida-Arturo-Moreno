
def suma(lista):
    suma=0
    for i in lista:
        suma=suma+i

    return suma

def promedio_lista(lista):
    prom=0
    tamb=len(lista)

    prom=suma(lista)/tamb
    return prom

def mayor(lista):
    mayor=0

    for i in lista:
        if i>mayor:
            mayor=i

            
    return mayor

def menor(lista):
    menor=lista[0]

    for i in lista:
        if i<menor:
            menor=i

    return menor

def mayor_prom(lista):
    lista_may=[]
    prob=promedio_lista(lista)
    for i in lista:
        if i>prob:
            lista_may.append(i)

    return lista_may



def cargar(lista):
    lista_Cargar = []
    n = int(input("Ingrese un elemento para la lista -99 para salir: "))

    while n != -99:
        lista_Cargar.append(n)
        n = int(input("Ingrese un elemento para la lista -99 para salir: "))
    
    return lista_Cargar

def main():
    

    lista=[]


    lista=cargar(lista)
   
    
    print(lista)

    print(f"La suma de elementos es {suma(lista)}")
    print(f"EL promedio es {promedio_lista(lista)}")
    print(f"El mayor es {mayor(lista)} y el menor {menor(lista)}")
    print(f"Mayores a promedio {mayor_prom(lista)}")


main()
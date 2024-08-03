
def elementos(lista,elemento,saltos):
    lista_borrar=[]

    indice=(lista.index(elemento))

    for i in range (indice,len(lista),saltos):
        lista_borrar.append(lista[i])
      
    return lista_borrar

def borrar(lista_borrar,lista_fin):

  for i in range(0,len(lista_borrar),1):
    if(lista_borrar[i] in lista_fin):
        lista_fin.remove(lista_borrar[i])
  
  lista_fin.reverse()
  return lista_fi

def cargar(lista):
    lista_Cargar = []
    n = int(input("Ingrese un elemento para la lista -99 para salir: "))

    while n != -99:
        lista_Cargar.append(n)
        n = int(input("Ingrese un elemento para la lista -99 para salir: "))
    
    return lista_Cargar

def main():
    rodrigo=[]

    rodrigo=cargar(rodrigo)

    valor_buscar=int(input("Ingresa el valor a buscar :"))

    while valor_buscar<1:
        valor_buscar=int(input("Valor positivo"))

    saltos=int(input("Ingresa los saltos :"))

    while saltos<1:
        saltos=int(input("Solo saltos positivos"))

    if valor_buscar in rodrigo:
              
        borrar1=elementos(rodrigo,5,2)

        rodrigo.reverse()
        borrar2=elementos(rodrigo,5,2)

        fin=borrar1+borrar2

        borrar(fin,rodrigo)

        print(f"La lista final es {rodrigo}")


main()
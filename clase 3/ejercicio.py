

rodrigo=[1,2,3,4,5,6,7,8,9,10]

valor_buscar=5
saltos=2

buscar_borrar=[valor_buscar]
if(5 in rodrigo):
    origen=rodrigo.index(5)
   while :
     buscar_borrar.append(rodrigo[origen+2])
     rodrigo.remove(origen+2)


print(buscar_borrar)
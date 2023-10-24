#Defino la clase en la que estare trabajando
class Store:
    def __init__ (self):
        #Aquí recibo al usuario y le pregunto su nombre
        Usuario = (input("Inserta tu nombre: "))
        print ("Bienvenido " + Usuario)

        #Defino las variables con las que trabajare
        total = 0
        costo = 0
        iva = 0.0
        total_Iva = 0.0
        
        #Defino la lista de productos que se pueden comprar. 
        #La lista prendas simplifica guardar los datos, y el for simplifica que se impriman.
        print ("Este es el menú de productos. Elige el número del producto que deseas comprar:")
        prendas = [["1: Pantalon","2: Playera","3: Chaqueta","4: Calcetines"],[100,125,300,75]]
        #Con el for mando a imprimir solo la primera lista de "prendas",
#       #para que le muestre las distintas opciones al usuario
        for x in prendas[0]:
            print (x)
        
        #Aquí defino la lista que se imprimirá al final con todos los productos que compró el usuario
        total_Productos = []
        
        #Aquí hago el ciclo que calcula el precio 
        n = (input("¿Quieres hacer una compra (si/no)? "))
        #Defino que mientras el usuario diga que si quiere seguir comprando se siga ejecutando el while
        while n == "si" :    
            opcion = int(input("Ingresa el número del producto(1-4): "))            
            #En base al producto que elija, se le va aumentar el costo final,
            #y se le va a guardar su compra en una lista.
            if opcion == 1:
                costo = prendas[1][0]
                total_Productos.append("Pantalón")
            elif opcion == 2:
                costo = prendas[1][1]
                total_Productos.append("Playera")
            elif opcion == 3:
                costo = prendas[1][2]
                total_Productos.append("Chaqueta")
            elif opcion == 4:           
                costo = prendas[1][3]
                total_Productos.append("Calcetines")
            #Calculo el costo extra por el IVA
            iva = self.__get_Iva(costo) 
            #Calculo el costo total incluído el IVA
            total = total + ( costo + iva )
            total_Iva = total_Iva + iva
            #Imprimo su costo total y el costo extra por el IVA
            print("El costo de tu producto es: $" + str(costo))
            print ("Y el iva del producto es: $" + str(iva))
            #Le vuelvo a preguntar al usuaio si queire comprar algo mas
            n = (input("¿Quieres hacer otra compra (si/no)? "))
            
        #Aqui imprimo los datos que se le mostrarán al usuario
        #Lista de los productos que compró
        print (f"Los prodcutos que compró fueron: {total_Productos}")
        #Total de $ a pagar
        print ("El costo total de tu compra fue de $" + str(total))
        #Total de $ a pagar por parte del IVA
        print ("The total cost of IVA is: $" + str(total_Iva))
        #Mensaje final
        print ("Gracias por tu compra")
        d_Finales = [[total_Productos], [total], [total_Iva]]
        print (d_Finales)

    #Aqui defino la función iva con la que conseguiré el costo extra por el IVA
    #costo_iva significa el costo del producto con iva
    def get_Iva(self, value):        
      return (value * 16) /100
    __get_Iva = get_Iva
     
Store()
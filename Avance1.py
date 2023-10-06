class Store:
    def __init__ (self):
        #Aquí recibo al usuario y le pregunto su nombre
        Usuario = (input("Inserta tu nombre: "))
        print ("Bienvenido " + Usuario)

        #Aquí pregunto por lo que quiere comprar
        total = 0
        costo = 0
        iva = 0.0
        totalIva = 0.0
        
        #Defino la lista de productos que se pueden comprar. La lista prendas simplifica guardar los datos, y el for simplifica que se impriman.
        print ("Este es el menú de productos. Elige el número del producto que deseas comprar:")
        prendas = [["1: Pantalon","2: Playera","3: Chaqueta","4: Calcetines"],[100,125,300,75]]
        for x in prendas[0]:
            print (x)
        #Antiguo método antes de usar la lista "prendas" y el ciclo for
        """
        print("1: Pantalon ")
        print("2: Playera")
        print("3: Chaqueta")
        print("4: Calcetines")
        """
        #Aquí defino la lista que se imprimirá al final con todos los productos que compró el usuario
        totalProductos = []
        
        #Aquí hago el ciclo que calcula el precio 
        n = (input("¿Quieres hacer una compra (si/no)? "))

        while n == "si" :    
            opcion = int(input("Ingresa el número del producto(1-4): "))            
        
            if opcion == 1:
                costo = prendas[1][0]
                totalProductos.append("Pantalón")
            elif opcion == 2:
                costo = prendas[1][1]
                totalProductos.append("Playera")
            elif opcion == 3:
                costo = prendas[1][2]
                totalProductos.append("Chaqueta")
            elif opcion == 4:           
                costo = prendas[1][3]
                totalProductos.append("Calcetines")

            iva = self.__getIva(costo) 
            
            total = total + ( costo + iva )
            totalIva = totalIva + iva
            
            print("El costo de tu producto es: $" + str(costo))
            print ("Y el iva del producto es: $" + str(iva))
        
            n = (input("¿Quieres hacer otra compra (si/no)? "))
            
        
        """
        print ("Los prodcutos que compró fueron: ")
        print (totalProductos) 
        """
        #Aqui imprimo los datos que se le mostrarán al usuario
        #Lista de los productos que compró
        print (f"Los prodcutos que compró fueron: {totalProductos}")
        #Total de $ a pagar
        print ("El costo total de tu compra fue de $" + str(total))
        #Total de $ a pagar por parte del IVA
        print ("The total cost of IVA is: $" + str(totalIva))
        #Mensaje final
        print ("Gracias por tu compra")
        dFinales = [[totalProductos], [total], [totalIva]]
        print (dFinales)

    #Aqui defino la función iva 
    #costo_iva significa el producto con iva
    def getIva(self, value):        
      return (value * 16) /100


    __getIva = getIva
    
    
Store()
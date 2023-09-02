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
        print ("Este es el menú de productos. Elige el número del producto que deseas comprar:")
        print("1: Pantalon ")
        print("2: Playera")
        print("3: Chaqueta")
        print("4: Calcetines")

        #Aquí hago el ciclo que calcula el precio 
        n = (input("¿Quieres hacer una compra (si/no)? "))

        while n == "si" :    
            opcion = int(input("Ingresa el número del producto(1-4): "))            
        
            if opcion == 1:
                costo = 100
            elif opcion == 2:
                costo = 125
            elif opcion == 3:
                costo = 300
            elif opcion == 4:           
                costo = 35

            iva = self.__getIva(costo) 
            
            total = total + ( costo + iva )
            totalIva = totalIva + iva
            
            print("El costo de tu producto es: $" + str(costo))
            print ("Y el iva del producto es: " + str(iva))
        
            n = (input("¿Quieres hacer otra compra (si/no)? "))
            
            
            
        print ("El total de tu compra fue de $" + str(total))
        print ("The total cost of IVA is: " + str(totalIva))
        print ("Gracias por tu compra")
    
    #Aqui defino la función iva 
    #costo_iva significa el producto con iva
    def getIva(self, value):        
      return (value * 16) /100


    __getIva = getIva
    
    
Store()
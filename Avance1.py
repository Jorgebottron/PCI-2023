#Aquí recibo al usuario y le pregunto su nombre
Usuario = (input("Inserta tu nombre: "))
print ("Bienvenido " + Usuario)

#Aquí pregunto por lo que quiere comprar
total = 0
costo = 0
print ("Este es el menú de productos. Elige el número del producto que deseas comprar:")
print("1: Pantalon ")
print("2: Playera")
print("3: Chaqueta")
print("4: Calcetines")

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
                       
        total = total + costo
        
        print("El total de tu compra es: " + str(total))
        
        n = (input("¿Quieres hacer otra compra (si/no)? "))
        
        
  
print ("El total de tu compra es de " + str(total))
print ("Gracias por tu compra")
  
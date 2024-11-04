

#variables iniciales
int_id = 0
name = ""
float_price = 0.0
int_stocks = 0

opcion = ""

#se crea las variables como listas para guardar los datos
productos_id = []
productos_name = []
productos_price = []
productos_stocks = []

#metodo para agregar productos a las listas
def crearProductos(int_id, name, float_price, int_stocks):
    productos_id.append(int_id)
    productos_name.append(name)
    productos_price.append(float_price)
    productos_stocks.append(int_stocks)

#metodo para obtener los productos
def obtenerProductos():
    #se usa un for para iterar cada valor que esta en la lista
    for i in range(len(productos_id)):
        print("id del producto:", productos_id[i])
        print("nombre del producto:", productos_name[i])
        print("precio del producto:", productos_price[i])
        print("stocks del producto:", productos_stocks[i])
        print()

#metodo para obtener un valor en especifico usando el nombre del producto
def obtenerProductoEspecifico(name):
    #se obtiene el indice o posicion de un producto en la lista
    indexProduct = productos_name.index(name)
    print("id del producto:", productos_id[indexProduct])
    print("nombre del producto:", productos_name[indexProduct])
    print("precio del producto:", productos_price[indexProduct])
    print("stocks del producto:", productos_stocks[indexProduct])

#metodo para actualizar el producto
def actualizarProducto(name):
    #se obtiene el indice o posicion de un producto en la lista
    indexProduct = productos_name.index(name)

    #variables de entradas por el usuario
    int_id = int(input("id del producto: "))
    name = input("nombre del producto: ")
    float_price = float(input("precio del producto: "))
    int_stocks = int(input("stocks del producto: "))

    #verifica si el precio o stocks son mayor a 0
    if float_price > 0 and int_stocks > 0 and int_id > 0:
        productos_id[indexProduct] = int_id
        productos_name[indexProduct] = name
        productos_price[indexProduct] = float_price
        productos_stocks[indexProduct] = int_stocks
    else:
        print("lo siento vuelva a intentarlo")

#metodo para eliminar un producto
def eliminarProducto(name):
    indexProduct = productos_name.index(name)
    productos_id.pop(indexProduct)
    productos_name.pop(indexProduct)
    productos_price.pop(indexProduct)
    productos_stocks.pop(indexProduct)

#se imprime las opciones para que el usuario elija
print("""
    0. salir
    1. crear producto
    2. obtener todos los productos
    3. obtener un producto en especifico
    4. actualizar un producto
    5. eliminar un producto de la lista
""")
#se hace un loop siempre y cuando la variable opcion no sea igual a 0
while opcion != "0":
    try:
        opcion = input("seleccion: ")
        
        if opcion == "1":
            int_id = int(input("id del producto: "))
            name = input("nombre del producto: ")
            float_price = float(input("precio del producto: "))
            int_stocks = int(input("stocks del producto: "))

            #se verifica si los precios y stocks son mayor a 0
            if float_price > 0 and int_stocks > 0 and int_id > 0:
                crearProductos(int_id, name, float_price, int_stocks)
            else:
                print("lo siento vuelva a intentarlo")

        elif opcion == "2":
            obtenerProductos()

        elif opcion == "3":
            name = input("nombre del producto a buscar: ")
            obtenerProductoEspecifico(name)

        elif opcion == "4":
            name = input("nombre del producto a actualizar: ")
            actualizarProducto(name)

        elif opcion == "5":
            name = input("nombre del producto a eliminar: ")
            eliminarProducto(name)

    except:
        print("parece que hubo un error")

    print()


















        

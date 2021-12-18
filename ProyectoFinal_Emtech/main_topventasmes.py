from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

prod_ventas = []
cantidad_de_productos = len(lifestore_products)

for id in range(cantidad_de_productos):
    verdadero_id = id + 1
    renglon = [verdadero_id, 0]
    prod_ventas.append(renglon)
meses = ['/01/', '/02/', '/08/']
for venta in lifestore_sales:
    fecha_venta = venta[3]
    if meses[2] in fecha_venta:
        print(fecha_venta)
    #id_prod = venta[1]
    #prod_ventas[id_prod - 1][1] = prod_ventas[id_prod - 1][1] + 1


# print(prod_ventas)
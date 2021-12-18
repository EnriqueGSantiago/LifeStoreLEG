from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
from operator import itemgetter


def ftoppromediores():
#if 1==1:
    prod_res = []
    prod_ventas = []
    cantidad_de_productos = len(lifestore_products)
    # INICIALIZACIÓN DE LISTA CON ID DE PRODUCTO Y CERO
    for id in range(cantidad_de_productos):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0]
        prod_res.append(renglon)

    for id in range(cantidad_de_productos):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0]
        prod_ventas.append(renglon)
    #print(prod_res)

     
    # CONTADOR DE RESEÑAS
    for ventas_1 in lifestore_sales:
        #lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
        id_prod_1 = ventas_1[1]
        prod_res[id_prod_1 - 1][1] = prod_res[id_prod_1 - 1][1] + ventas_1[2]

    #print(prod_res) 
    for venta in lifestore_sales:
        id_prod = venta[1]
        prod_ventas[id_prod - 1][1] = prod_ventas[id_prod - 1][1] + 1
        
    #print(prod_res)
    #print('\n')
    #print(prod_ventas)

    prod_prom_res = []
    cantidad_de_productos_2 = len(lifestore_products)
    for id in range(cantidad_de_productos_2):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0]
        prod_prom_res.append(renglon)

    i_it = 0
    for ven in prod_ventas:
        id_prod = ven[0]
        if ven[1] != 0:
            prod_prom_res[i_it][1] =  prod_res[i_it][1]/ven[1]
        i_it += 1

    #print(prod_prom_res)
    
    prod_res_sorted = []
    prod_res_sorted = sorted(prod_prom_res, key=itemgetter(1), reverse=True)

    print(prod_res_sorted)


    limpiarPantalla = '\n' * 15
    print(limpiarPantalla)
    print('***************** TOP 20 PRODUCTOS MEJOR RESEÑA ********************') 
    print('____________________________________________________________________')
    print('ID PRODUCTO   PROMEDIO            NOMBRE DEL PRODUCTO ')
    print('____________________________________________________________________')
    for i in range(20):
        prod_complete = lifestore_products[prod_res_sorted[i][0]-1][1]
        prod_desc = prod_complete.split(',')

        print('     '+str(prod_res_sorted[i][0]) + '           ' + str(prod_res_sorted[i][1]) +  '              ' + str(prod_desc[0])) 
        i += 1
    print('_______________________________________________________________________________________')
    print('\n')
    retro = input("PARA CERRAR SESIÓN PRESIONE CUALQUIER TECLA, SI DESEA REALIZAR OTRA CONSULTA PRESIONE 'Y': ")
    return retro
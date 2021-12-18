from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
from operator import itemgetter

def fmenorventacat():
#if 1==1:
    prod_ventas = []
    cantidad_de_productos = len(lifestore_products)
    # INICIALIZACIÓN DE LISTA CON ID DE PRODUCTO Y CERO
    for id in range(cantidad_de_productos):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0, lifestore_products[id][3]]
        prod_ventas.append(renglon)

    # CONTADOR DE VENTAS
    for venta in lifestore_sales:
        refund = venta[4]
        if refund == 1:
            continue
        else:
            id_prod = venta[1]
            prod_ventas[id_prod - 1][1] = prod_ventas[id_prod - 1][1] + 1
    # IMPRIMIR LOS 5 MÁS VENDIDOS
    prod_sorted = []
    prod_sorted = sorted(prod_ventas, key=itemgetter(1), reverse=True)

    print(prod_sorted)
    # IMPRESIÓN EN PANTALLA

    categorias = []
    for id in range(cantidad_de_productos):
        if len(categorias) == 0:
            categorias.append(lifestore_products[id][3])
        else:
            for cat in categorias:
                flag_after_loop = False
                if cat == lifestore_products[id][3]:
                    continue
                else:
                    flag_after_loop = True
            if flag_after_loop == True:
                categorias.append(lifestore_products[id][3])
    print(categorias)


    prod_v_cat = []
    cantidad_cat = len(categorias)
    # INICIALIZACIÓN DE LISTA CON ID DE PRODUCTO Y CERO
    for cate in range(cantidad_cat):
        renglon = []
        prod_v_cat.append(renglon)
    print(prod_v_cat)

    i_cat = 0
    for categoria in categorias:
        for prod_cat in prod_sorted:
            if categoria == prod_cat[2]:
                prod_v_cat[i_cat].append(prod_cat)
        i_cat += 1
    print(prod_v_cat)


    limpiarPantalla = '\n' * 15
    print(limpiarPantalla)
    i_imp = 0
    print('*** PRODUCTOS CON MENOS VENTAS POR CATEGORÍA ***')
    print('________________________________________________')
    print('\n')
    for categoria in categorias:
        print('             ' + categoria + '    ')
        print('**************************************')
        i_imp_limite = 0
        for venta in reversed(prod_v_cat[i_imp]):
            if venta[1] != 0 and i_imp_limite < 5:
                print('El producto con ID: ' + str(venta[0]) + ' tuvo: ' + str(venta[1])+ ' ventas')
                i_imp_limite += 1
        i_imp += 1
        print('_________________________________________________')
        print('\n')

    retro = input(" PARA CERRAR SESIÓN PRESIONE CUALQUIER TECLA, SI DESEA REALIZAR OTRA CONSULTA PRESIONE 'Y': ")
    return retro


def fmenorbusquedacat():
    prod_busquedas = []
    cantidad_de_productos = len(lifestore_products)
    # INICIALIZACIÓN DE LISTA CON ID DE PRODUCTO Y CERO
    for id in range(cantidad_de_productos):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0, lifestore_products[id][3]]
        prod_busquedas.append(renglon)

    for busqueda in lifestore_searches:
        prod_b =  busqueda[1]
        prod_busquedas[prod_b-1][1] += 1 
        # IMPRIMIR LOS 5 MÁS BUSCADOS
    prod_b_sorted = []
    prod_b_sorted = sorted(prod_busquedas, key=itemgetter(1), reverse=True)
    print(prod_b_sorted)

    categorias = []
    for id in range(cantidad_de_productos):
        if len(categorias) == 0:
            categorias.append(lifestore_products[id][3])
        else:
            for cat in categorias:
                flag_after_loop = False
                if cat == lifestore_products[id][3]:
                    continue
                else:
                    flag_after_loop = True
            if flag_after_loop == True:
                categorias.append(lifestore_products[id][3])
    print(categorias)

    prod_v_cat = []
    cantidad_cat = len(categorias)
    # INICIALIZACIÓN DE LISTA CON ID DE PRODUCTO Y CERO
    for cate in range(cantidad_cat):
        renglon = []
        prod_v_cat.append(renglon)
    print(prod_v_cat)

    i_cat = 0
    for categoria in categorias:
        for prod_cat in prod_b_sorted:
            if categoria == prod_cat[2]:
                prod_v_cat[i_cat].append(prod_cat)
        i_cat += 1
    print(prod_v_cat)

    limpiarPantalla = '\n' * 15
    print(limpiarPantalla)
    i_imp = 0
    print('** PRODUCTOS CON MENOS BUSQUEDAS POR CATEGORÍA **')
    print('________________________________________________')
    print('\n')
    for categoria in categorias:
        print('             ' + categoria + '    ')
        print('**************************************')
        i_imp_limite = 0
        for venta in reversed(prod_v_cat[i_imp]):
            if venta[1] != 0 and i_imp_limite < 5:
                print('El producto con ID: ' + str(venta[0]) + ' tuvo: ' + str(venta[1])+ ' busquedas')
                i_imp_limite += 1
        i_imp += 1
        print('_________________________________________________')
        print('\n')
    
    retro = input("PARA CERRAR SESIÓN PRESIONE CUALQUIER TECLA, SI DESEA REALIZAR OTRA CONSULTA PRESIONE 'Y': ")
    return retro
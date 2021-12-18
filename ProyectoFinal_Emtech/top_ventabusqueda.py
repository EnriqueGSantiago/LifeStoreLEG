from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
from operator import itemgetter

def ftopventas():
#if 1==1:
    prod_ventas = []
    cantidad_de_productos = len(lifestore_products)
    # INICIALIZACIÓN DE LISTA CON ID DE PRODUCTO Y CERO
    for id in range(cantidad_de_productos):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0]
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

    # IMPRESIÓN EN PANTALLA
    limpiarPantalla = '\n' * 15
    print(limpiarPantalla)
    print('*********************** TOP 5 DE PRODUCTOS MÁS VENDIDOS 2020 **************************')
    print('_______________________________________________________________________________________')
    for i in range(5):
        prod_complete = lifestore_products[prod_sorted[i][0]-1][1]
        prod_desc = prod_complete.split(',')
        print('El producto ' + str(prod_desc[0]) + ', con ID ' 
        + str(prod_sorted[i][0]) + ' tuvo: ' + str(prod_sorted[i][1]) + ' ventas')
        i += 1
    print('_______________________________________________________________________________________')
    print('\n')
    retro = input(" PARA CERRAR SESIÓN PRESIONE CUALQUIER TECLA, SI DESEA REALIZAR OTRA CONSULTA PRESIONE 'Y': ")
    return retro
    #retro = input('¿Quieres retornar al menú principal? Y/N: ')
    #return retro

#lifestore_products
#[1, 'Procesador AMD Ryzen 3 3300X S-AM4, 3.80GHz, Quad-Core, 16MB L2 Cache', 3019, 'procesadores', 16],



def ftopventames(vmes):
#if 1==1:
    # Ventas Validas
    ventas = []
    # lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
    for sale in lifestore_sales:
        # refund = sale[-1]
        refund = sale[4]
        if refund == 1:
            continue
        else:
            ventas.append(sale)
    meses = [
        '/01/', '/02/', '/03/', '/04/', '/05/', '/06/',
        '/07/', '/08/', '/09/', '/10/', '/11/', '/12/'
        ]

    ventas_por_mes = []
    for mes in meses:
        lista_vacia = []
        ventas_por_mes.append(lista_vacia)

    #print(ventas_por_mes)

    for venta in ventas:
        # Datos de la venta
        id_venta = venta[0]
        fecha = venta[3]
        # Clasificar en mes
        # Comienzo en el mes 0 ('/01/')
        contador_de_mes = 0

        for mes in meses:
            if mes in fecha:
                ventas_por_mes[contador_de_mes].append(id_venta)
                continue
            contador_de_mes = contador_de_mes + 1 
    #print(ventas_por_mes)

    meses_v = [ ['Enero',0], ['Febrero',1], ['Marzo',2], ['Abril',3], ['Mayo',4], ['Junio',5], ['Julio', 6], ['Agosto',7], ['Septiembre',8], ['Octubre',9], ['noviembre',10], ['Diciembre',11]]
    """lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]"""
    vp_pormes = []
    toppormes = []
   
    for mes_v in meses_v:
        if vmes == mes_v[0]:
            rango_mes = len(ventas_por_mes[mes_v[1]])
            for pos_id_venta in range(rango_mes):
                id_venta = ventas_por_mes[mes_v[1]][pos_id_venta]
                id_prod_m = lifestore_sales[id_venta-1][1]
                vp_pormes.append([id_venta,id_prod_m])

    rango_mp = len(vp_pormes)

    for prod_v in vp_pormes:
        rango_nueva = len(toppormes)
        if rango_nueva == 0:
            toppormes.append([prod_v[1], 1])
        else:
            flag_after_loop = False
            i_vp = 0
            for vent_prod in toppormes:
                if vent_prod[0] == prod_v[1]:
                    toppormes[i_vp][1] += 1
                    i_vp += 1
                    flag_after_loop = False
                else:
                    flag_after_loop = True
                    i_vp += 1
            if flag_after_loop == True:
                toppormes.append([prod_v[1], 1]) 
                flag_after_loop = False
    prod_sorted_m = []
    prod_sorted_m = sorted(toppormes, key=itemgetter(1), reverse=True)
    print(prod_sorted_m)

    limpiarPantalla = '\n' * 15
    print(limpiarPantalla)
    print('******************* TOP 5 PRODUCTOS MÁS VENDIDOS EN: '+ vmes +' **********************')
    print('_______________________________________________________________________________________')
    cont_i = 0
    for vm in prod_sorted_m:
        longitud_pm = len(prod_sorted_m)
        if cont_i < 5:
            prod_complete_mes = lifestore_products[vm[0]-1][1]
            prod_desc_mes = prod_complete_mes.split(',')

            print('El producto ' + str(prod_desc_mes[0]) + ', con ID ' 
            + str(vm[0]) + ' tuvo: ' + str(vm[1]) + ' ventas')
        cont_i += 1
    print('_______________________________________________________________________________________')
    retro = input("PARA CERRAR SESIÓN PRESIONE CUALQUIER TECLA, SI DESEA REALIZAR OTRA CONSULTA PRESIONE 'Y': ")
    return retro


def ftopbusquedas():
    prod_busquedas = []
    cantidad_de_productos = len(lifestore_products)
    # INICIALIZACIÓN DE LISTA CON ID DE PRODUCTO Y CERO
    for id in range(cantidad_de_productos):
        verdadero_id = id + 1
        renglon = [verdadero_id, 0]
        prod_busquedas.append(renglon)

    for busqueda in lifestore_searches:
        prod_b =  busqueda[1]
        prod_busquedas[prod_b-1][1] += 1 
        # IMPRIMIR LOS 5 MÁS BUSCADOS
    prod_b_sorted = []
    prod_b_sorted = sorted(prod_busquedas, key=itemgetter(1), reverse=True)

    #print(prod_busquedas)

    # IMPRESIÓN EN PANTALLA
    limpiarPantalla = '\n' * 15
    print(limpiarPantalla)
    print('*********************** TOP 10 PRODUCTOS CON MÁS BUSQUEDAS **************************')
    print('_______________________________________________________________________________________')
    for i in range(10):
        prod_complete = lifestore_products[prod_b_sorted[i][0]-1][1]
        prod_desc = prod_complete.split(',')
        print('El producto ' + str(prod_desc[0]) + ', con ID ' 
        + str(prod_b_sorted[i][0]) + ' tuvo: ' + str(prod_b_sorted[i][1]) + ' ventas')
        i += 1
    print('_______________________________________________________________________________________')
    print('\n')
    retro = input(" PARA CERRAR SESIÓN PRESIONE CUALQUIER TECLA, SI DESEA REALIZAR OTRA CONSULTA PRESIONE 'Y': ")
    return retro
    #47, 'SSD XPG SX8200 Pro, 256GB







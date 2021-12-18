import login_pf
import menu
import submenu
import top_ventabusqueda
import total_ingresos
import menores_ventabusqueda
import resena_promedio

if login_pf.flogin() == True:
    
    while True:
        vseleccion_menu = menu.fmenu()
        if vseleccion_menu == 1:
            #primer archivo de ordenamiento
            v_seleccion_submenu = submenu.fsubmenu(1)
            if v_seleccion_submenu == 101:
                if top_ventabusqueda.ftopventas() != 'Y':
                    break
                else:
                    continue
            elif v_seleccion_submenu == 102:
                print('INGRESA EL MES A REVISAR (Ingresa un valor válido o regresarás al menú principal)')
                vmes_in = input( '・➣ ')
                vmeses_in = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
                if vmes_in in vmeses_in:
                    if top_ventabusqueda.ftopventames(vmes_in) != 'Y':
                        break
                    else:
                        continue
                else:
                    break
            elif v_seleccion_submenu == 200:
                if top_ventabusqueda.ftopbusquedas() != 'Y':
                    break
                else:
                    continue
            elif v_seleccion_submenu == 300:
                if menores_ventabusqueda.fmenorventacat() != 'Y':
                    break
                else:
                    continue
            elif v_seleccion_submenu == 400:
                if menores_ventabusqueda.fmenorbusquedacat() != 'Y':
                    break
                else:
                    continue

        elif vseleccion_menu == 2:
            #
            v_seleccion_submenu = submenu.fsubmenu(2)
            if v_seleccion_submenu == 2000:
                if resena_promedio.ftoppromediores() != 'Y':
                    break
                else:
                    continue

        elif vseleccion_menu == 3:
            #
            v_seleccion_submenu = submenu.fsubmenu(3)
            if v_seleccion_submenu == 3:
                if total_ingresos.ftotalingresos() != 'Y':
                    break
                else:
                    continue
            print("1")
        elif vseleccion_menu == 4:
            print("Acabas de cerrar sesión")
            exit()
        else:
            continue
    
    print("Acabas de cerrar sesión")
    exit()
        

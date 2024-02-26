from tabulate import tabulate

def list_departaments():
    departament = ["AMAZONAS", "ANTIOQUIA", "ARAUCA", "ATLANTICO", "BOLIVAR", "BOYACA", "CALDAS",
    "CAQUETA","CASANARE", "CAUCA", "CESAR", "CHOCO", "CORDOBA", "CUNDINAMARCA", "GUAINIA", "GUAVIARE",
    "HUILA", "GUAJIRA", "MAGDALENA", "META", "NARINO", "NORTE SANTANDER", "PUTUMAYO", "QUINDIO", 
    "RISARALDA", "SAN ANDRES", "SANTANDER", "SUCRE", "TOLIMA", "VALLE", "VAUPES", "VICHADA"]
    return departament
    
def menu_departaments():
    i = 1
    print("DEPARTAMENTOS:")
    departament = list_departaments()
    for name_departament in departament:
        print("{0}. {1}".format(i, name_departament))
        i += 1

#Se usa en el main
def ask_info_to_user():
    menu_departaments()
    opcion_depart = int(input("Ingresa la opcion que corresponda al departamento que desea consultar: "))

    while opcion_depart <= 0 or opcion_depart > 32:
        print("Opcion ingresada invalida.")
        opcion_depart = int(input("Ingresa una opcion valida: "))
    
    departament_list = list_departaments()
    departament = departament_list[opcion_depart - 1]
    limit_records = int(input("Ingresa la cantidad de registros para mostrar: "))
    while (limit_records < 0 or limit_records >= 1000):
        print("Cantidad de registros no válidos")
        limit_records = int(input("Ingresa una cantidad de registros válida (0 - 999): "))
        
    return limit_records, departament

def print_table(datas):
    headers = ["N°","Ciudad de Ubicacion", "Departamento", "Edad", "Tipo", "Estado", "Pais de Procedencia"]
    print(tabulate(datas, headers=headers))



    



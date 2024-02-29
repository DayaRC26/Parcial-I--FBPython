from tabulate import tabulate #libreria para tabla

#Funcion encargada de retornar lista de departamentos
def list_departaments():
    departament = ["AMAZONAS", "ANTIOQUIA", "ARAUCA", "ATLANTICO", "BOLIVAR", "BOYACA", "CALDAS",
    "CAQUETA","CASANARE", "CAUCA", "CESAR", "CHOCO", "CORDOBA", "CUNDINAMARCA", "GUAINIA", "GUAVIARE",
    "HUILA", "GUAJIRA", "MAGDALENA", "META", "NARINO", "NORTE SANTANDER", "PUTUMAYO", "QUINDIO", 
    "RISARALDA", "SAN ANDRES", "SANTANDER", "SUCRE", "TOLIMA", "VALLE", "VAUPES", "VICHADA"]
    return departament

#Imprime el menu de departamentos    
def menu_departaments():
    i = 1
    print("DEPARTAMENTOS:")
    departament = list_departaments()
    for name_departament in departament:
        print("{0}. {1}".format(i, name_departament))
        i += 1

#Pregunta la informacion necesaria al usuario, se usa en el main
def ask_info_to_user():
    menu_departaments()
    departament = list_departaments()
    opcion_depart = input("Ingresa el departamento que desea consultar: ").upper()

    #si la opcion se pasa de los limites de los departamentos no lo deja salir del bucle
    while(opcion_depart not in departament):
        print("El departamento ingresado no es valido.\n")
        opcion_depart = input("Ingresa el departamento que desea consultar: ").upper()
     
    limit_records = int(input("Ingresa la cantidad de registros para mostrar: "))

    #si la opcion se pasa de los limites de los departamentos no lo deja salir del bucle
    while (limit_records < 0 or limit_records >= 1000):
        print("Cantidad de registros no válidos")
        limit_records = int(input("Ingresa una cantidad de registros válida (0 - 999): "))
        
    return limit_records, opcion_depart

#Imprime la informacion del DataFrame en una tabla
def print_table(datas):
    headers = ["N°","Ciudad de Ubicacion", "Departamento", "Edad", "Tipo de Contagio", "Estado", "Pais de Procedencia"]
    datas.index = range(1, len(datas) + 1) #para que el indice comience desde 1
    print(tabulate(datas, headers=headers, tablefmt = "double_grid"))



    



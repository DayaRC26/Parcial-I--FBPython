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
    option_depart = input("Ingresa el departamento de Colombia que desea consultar: ").upper()

    #si la opcion se pasa de los limites de los departamentos no lo deja salir del bucle
    while(option_depart not in departament):
        print("El departamento ingresado no es valido.\n")
        option_depart = input("Ingresa el departamento que desea consultar: ").upper()
    
    option_municipio = input("Ingresa el municipio que desea consultar: ").upper()

    option_cultivo = input("Ingresa el cultivo que desea consultar: ")

    limit_records = int(input("Ingresa la cantidad de registros para mostrar: "))

    #si la opcion se pasa de los limites de los departamentos no lo deja salir del bucle
    while (limit_records < 0 or limit_records >= 1000):
        print("Cantidad de registros no válidos")
        limit_records = int(input("Ingresa una cantidad de registros válida (0 - 999): "))

    user_input = [limit_records, option_depart, option_municipio, option_cultivo]
        
    return user_input

def calcule_median(df):
    median_ph = df['ph_agua_suelo_2_5_1_0'].median()
    median_p = df['f_sforo_p_bray_ii_mg_kg'].median()
    median_k = df['potasio_k_intercambiable_cmol_kg'].median()

    return median_ph, median_p, median_k

def extract_info_df(df):
    departamento = df['departamento'].iloc[0]
    municipio = df['municipio'].iloc[0]
    cultivo = df['cultivo'].iloc[0]
    topografia = df['topografia'].iloc[0]
    median_ph, median_p, median_k = calcule_median(df)
    datos = [departamento, municipio, cultivo, topografia, median_ph, median_p, median_k]

    return datos

#Imprime la informacion del DataFrame en una tabla
def print_table(datas):
    datos = extract_info_df(datas)
    headers = ["Departamento","Municipio", "Cultivo", "Topología", "pH", "Fosforo", "Potasio"]
    print(tabulate([datos], headers=headers, tablefmt = "double_grid"))



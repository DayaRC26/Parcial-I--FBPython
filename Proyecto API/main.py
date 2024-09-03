#Funciones importadas de los paquetes y modulos
from UI.user_interface import ask_info_to_user, print_table 
from API.api import obtener_df_api

def main ():
    user_input = ask_info_to_user()
    data = obtener_df_api(user_input)
    print_table(data)

main()

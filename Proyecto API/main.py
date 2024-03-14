#Funciones importadas de los paquetes y modulos
from UI.user_interface import ask_info_to_user, print_table 
from API.api import api_casos
from API.data_visualization import show_plot_data, print_data_information

def main ():
    limit_records, departament = ask_info_to_user()
    data = api_casos(limit_records, departament)
    print_data_information(data) 
    print_table(data)
    show_plot_data(data)

main()

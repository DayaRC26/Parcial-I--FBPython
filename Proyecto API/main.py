from UI.user_interface import ask_info_to_user, print_table
from API.api import api_casos 

def main ():
    limit_records, departament = ask_info_to_user()
    data = api_casos(limit_records, departament)
    print_table(data)

main()

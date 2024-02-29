import pandas as pd
from sodapy import Socrata

#obtiene  la informacion del API, recibe dos parametros
def api_casos(limit_records, departament):
    client = Socrata ("www.datos.gov.co", None )

    #corresponde a la informacion que se le pide al api
    selected_data = "ciudad_municipio_nom, departamento_nom, edad, fuente_tipo_contagio, estado, pais_viajo_1_nom"
    results = client.get ("gt2j-8ykr", limit = limit_records , departamento_nom = departament, select = selected_data )
    results_df = pd.DataFrame(results)

    if 'pais_viajo_1_nom' not in results_df.columns:
        results_df['pais_viajo_1_nom'] = "Sin Registro"
    
    return results_df



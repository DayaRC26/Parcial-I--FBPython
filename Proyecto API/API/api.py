import pandas as pd
import numpy as np
from sodapy import Socrata

#obtiene  la informacion del API, recibe dos parametros
def api_casos(limit_records, departament):
    client = Socrata ("www.datos.gov.co", None )

    #corresponde a la informacion que se le pide al api
    selected_data = "ciudad_municipio_nom, departamento_nom, edad, fuente_tipo_contagio, estado, pais_viajo_1_nom"
    results = client.get ("gt2j-8ykr", limit = limit_records , departamento_nom = departament, select = selected_data )
    results_df = pd.DataFrame(results)

    if 'pais_viajo_1_nom' not in results_df.columns:
        results_df['pais_viajo_1_nom'] = pd.NA

    results_df.fillna("Sin Registro", inplace = True)
    data_information (results_df)

    
    return results_df

def data_information (dataf):
    print("\nInformacion general:")
    print("Numero de filas:",dataf.shape[0])
    print("Numero de columnas:",dataf.shape[1] )
    print("Nombre Columnas:",dataf.columns.values.tolist())
    print("Tipo de datos columnas:\n",dataf.dtypes)
    print("\nInformacion valores perdidos:")
    print("Columna con valores perdidos:",dataf.columns[dataf.isnull().any()].tolist())
    print("Numero de Filas con valores perdidos:", len(dataf[pd.isnull(dataf).any(axis=1)]))
    print("Indices con valores perdidos: ", np.where(pd.isnull(dataf).any())[0][:5])
    print("\nEstadísticas Generales:")
    print(dataf.info())
    print("\nResumen de estadisticas:" )
    print(dataf.describe())



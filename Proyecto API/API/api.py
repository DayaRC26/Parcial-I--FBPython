import pandas as pd
from sodapy import Socrata

def change_type_float(results_df):
    results_df["ph_agua_suelo_2_5_1_0"] = results_df["ph_agua_suelo_2_5_1_0"].astype(float)
    results_df["f_sforo_p_bray_ii_mg_kg"] = results_df["f_sforo_p_bray_ii_mg_kg"].astype(float)
    results_df["potasio_k_intercambiable_cmol_kg"] = results_df["potasio_k_intercambiable_cmol_kg"].astype(float)

    return results_df


#obtiene  la informacion del API, recibe dos parametros
def obtener_df_api(user_input):
    client = Socrata ("www.datos.gov.co", None )

    selected_data = "departamento, municipio, cultivo, topografia, ph_agua_suelo_2_5_1_0, f_sforo_p_bray_ii_mg_kg, potasio_k_intercambiable_cmol_kg"
    results = client.get ("ch4u-f3i5", limit = user_input[0], departamento = user_input[1], municipio = user_input[2], cultivo = user_input[3], select = selected_data )
    results_data = pd.DataFrame(results)
    results_df = change_type_float(results_data)

    return results_df



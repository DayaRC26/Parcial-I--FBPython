import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def print_data_information(dataf):
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

def show_plot_data(dataf):
    dataf.groupby('estado')['edad'].mean().plot.bar()
    plt.title('Estado de Población según su edad')
    plt.xlabel('Estado')
    plt.ylabel('Edad')
    plt.show()

    dataf.edad.hist(color='green')
    plt.title('Distribución de edades')
    plt.xlabel('edad')
    plt.ylabel('departamento_nom')
    plt.show()

    sns.boxplot(data=dataf, x='edad', y='fuente_tipo_contagio')
    plt.title('Distribución de edades según la fuente de contagio')
    plt.show()

    sns.swarmplot(data=dataf, x='edad', y='ciudad_municipio_nom', size = 5)
    plt.title('Distribución de edades según el municipio')
    plt.show()
    
    
    

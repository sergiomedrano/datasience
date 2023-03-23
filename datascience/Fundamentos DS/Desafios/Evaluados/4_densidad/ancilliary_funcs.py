import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def variables_continuas(df):
    #Calcula medidas descriptivas para los casos continuos
    des_continua = df.describe()
    #Calcula frecuencia para cada variable discreta
    frec_ht_region = df['ht_region'].value_counts()
    
    describe = des_continua[['gle_cgdpc','undp_hdi','imf_pop']]
    
    return describe


def funcion(df, var, print_list=False):
    df_na = df.isna()
    n = len(df[var])
    n_perdidos = len(df_na[df_na[var] == True])
    porcentaje = round((n_perdidos*100)/n,2)
    
    df_fil = df[df_na[var] == True]
    
    if print_list == False:
        return n_perdidos,porcentaje
    else:
        return n_perdidos, porcentaje, df_fil
    

def graf_histograma(sample_df, full_df, var, sample_mean=False, true_mean=False):
    
    plt.figure(figsize=(4,6))
    #Grafico Sample
    plt.subplot(2,1,1)
    plt.hist(sample_df[var], color='grey', alpha=.4)
    if sample_mean:
        plt.axvline(sample_df[var].mean(),color='dodgerblue', linestyle='--', lw=2)
    plt.title(f'Histograma de la media variable {var} datos de la muestra')
    
    #Grafico Full
    plt.subplot(2,1,2)
    plt.hist(full_df[var], color='grey', alpha=.4)
    if true_mean:
        plt.axvline(full_df[var].mean(),color='dodgerblue', linestyle='--', lw=2)
    plt.title(f'Histograma de la media variable {var} datos Full')
    plt.tight_layout()
    
    return round(sample_df[var].mean(),3),round(full_df[var].mean(),3)


def graf_dotplot(dataframe, plot_var, plot_by, statistic='mean', global_stat=False):
    if statistic == 'median':
        group = round(dataframe.groupby(plot_by)[plot_var].median(),2)
        plt.axvline(dataframe[plot_var].median(), color = 'tomato', linestyle = '--')
    else:
        group = round(dataframe.groupby(plot_by)[plot_var].mean(),2)
        plt.axvline(dataframe[plot_var].mean(), color = 'tomato', linestyle = '--')
    
    plt.title(plot_var)
    if not global_stat:
        plt.plot(group.values, group.index, 'o', color = 'grey')
    else:
        plt.plot(dataframe[plot_var], dataframe[plot_var].index, 'o', color = 'grey')
    
    return True
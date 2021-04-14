import pandas as pd 
import numpy as np 
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler





def processing_num_vars(df):
    df_personas = df.copy()
    df_personas['log_ingreso_mens']=np.log(df_personas['ingreso_mens'] + 1)
    df_personas['log_num_seguros_salud']=np.log(df_personas['num_seguros_salud']+1)
    df_personas['log_rcc_nro_prod']=np.log(df_personas['rcc_nro_prod']+1)
    df_personas['log_rcc_linea_tc_max']=np.log(df_personas['rcc_linea_tc_max'] + 1)
    df_personas['log_rcc_num_ent_sbs']=np.log(df_personas['rcc_num_ent_sbs'] + 1)
    df_personas['log_edad']=np.log(df_personas['edad'] + 1)
    df_personas['log_diff_lj_created']=np.log(df_personas['diff_lj_created'] + 1)

    return df_personas


def get_nse(serie):
    
    #print(serie)
    
    if (serie["sit_laboral"] == "DEP") and (serie["tipo_vivienda"] in ["propia"]):
        return "A"
    elif (serie["sit_laboral"] == "DEP") and (serie["tipo_vivienda"] in ["fami", "hipot"]):
        return "B"
    elif (serie["sit_laboral"] == "DEP") and (serie["tipo_vivienda"] in ["fami", "alqui"]):
        return "C"
    else: 
        return "D"
    


def processing_cat_vars(df):
    df_personas = df.copy()
    
    df_personas.loc[df_personas.rcc_cal_gral=='OK','enc_rcc_cal_gral']=5
    df_personas.loc[df_personas.rcc_cal_gral=='CPP','enc_rcc_cal_gral']=4
    df_personas.loc[df_personas.rcc_cal_gral=='DEF','enc_rcc_cal_gral']=3
    df_personas.loc[df_personas.rcc_cal_gral=='DUD','enc_rcc_cal_gral']=2
    df_personas.loc[df_personas.rcc_cal_gral=='PER','enc_rcc_cal_gral']=1
    df_personas.loc[df_personas.rcc_cal_gral=='OTR','enc_rcc_cal_gral']=0
    
    df_personas.loc[df_personas.nse=='A','enc_nse']=4
    df_personas.loc[df_personas.nse=='B','enc_nse']=3
    df_personas.loc[df_personas.nse=='C','enc_nse']=2
    df_personas.loc[df_personas.nse=='D','enc_nse']=1
    df_personas.loc[df_personas.nse=='E','enc_nse']=0
    
    df_personas.loc[df_personas.segmento=='SEGM4','enc_segmento']=3
    df_personas.loc[df_personas.segmento=='SEGM3','enc_segmento']=2
    df_personas.loc[df_personas.segmento=='SEGM2','enc_segmento']=1
    df_personas.loc[df_personas.segmento=='SEGM1','enc_segmento']=0

    
    df_personas['enc_gender'] = df_personas['gender'].map(df_personas['gender'].value_counts()/len(df_personas))
    df_personas['enc_provincia'] = df_personas['provincia'].map(df_personas['provincia'].value_counts()/len(df_personas))
    
    le=LabelEncoder()
    df_personas['le_provincia']=le.fit_transform(df_personas['provincia'])
    
    return df_personas

def process_data(df_personas):
    
    df_personas["created"] = pd.to_datetime(df_personas["created"], format='%m/%d/%y %H:%M')
    df_personas["_last_judgment_at"] = pd.to_datetime(df_personas["_last_judgment_at"], format='%m/%d/%y %H:%M')

    df_personas["diff_lj_created"] = (df_personas["_last_judgment_at"].dt.year.astype(int)*360 + df_personas["_last_judgment_at"].dt.month.astype(int)*30).astype(int) - (df_personas["created"].dt.year.astype(int)*360 + df_personas["created"].dt.month.astype(int)*30).astype(int)   #- df_personas["created"].dt.to_period("M")
    df_personas["nse"] = df_personas.apply(get_nse, axis=1)
    
    
    df_personas = processing_cat_vars(df_personas)
    df_personas = processing_num_vars(df_personas)

    return df_personas
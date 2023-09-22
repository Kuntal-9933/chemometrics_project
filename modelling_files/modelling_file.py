import joblib
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter



def model_func(path,wl=17,p=2,d=2,target="Brix"):

    """path = path of the file where the csv file is located\n
       wl= window length for savgol filter (default = 27)\n
       p= order of the polynomial to be fitted (default = 2)\n
       d= order of the derivative (default = 0)\n
        target = Curcumin (default)\n\t
                 Moisture\n\t
                 Starch\n\t
                 Olerosin"""
    #########   spectra data gathering ##########
    df=pd.read_csv(path)
    #########   other factors data gathering ##########
    spectral_data=df["Reflectance"].values
    def SNV(data_set):
        output_data=np.zeros_like(data_set)
        output_data= (data_set-np.mean(data_set))/np.std(data_set)
        return output_data

    x_snv_test=SNV(spectral_data)

    x_sg_test=savgol_filter(x_snv_test,window_length=wl , polyorder=p, deriv=d)
    if target =="Brix":
        model=joblib.load("F:\\accenture_interview_project\\modelling_files\\model.pkl")
        pred=model.predict([x_sg_test])[0][0]
    else:
        return 0

    return pred
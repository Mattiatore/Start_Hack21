# -*- coding: utf-8 -*-

import pandas as pd
import tsfresh

# setting parameters
#quantile for coal
q_coal=0.9

#quantile for gas
q_gas=0.85

#quantile for lignite
q_lignite=0.87

#quantile for nuc
q_nuc=0.95

#German market powerplants data 
coal= pd.read_csv("C:/Users/Mattia/Desktop/Start_Hack21/dataset/Powerplant/COAL_production/28138.csv", names= ["Time", "Quantity"], skiprows=1)
gas= pd.read_csv("C:/Users/Mattia/Desktop/Start_Hack21/dataset/Powerplant/GAS_production/28336.csv", names= ["Time", "Quantity"], skiprows=1)
lignite= pd.read_csv("C:/Users/Mattia/Desktop/Start_Hack21/dataset/Powerplant/LIGNITE_production/28266.csv", names= ["Time", "Quantity"], skiprows=1)
nuc= pd.read_csv("C:/Users/Mattia/Desktop/Start_Hack21/dataset/Powerplant/NUC_production_capacity/21899.csv", names= ["Time", "Quantity"], skiprows=1)

print("Coal: " + str(int(tsfresh.feature_extraction.feature_calculators.quantile(coal.Quantity, q_coal))))

print("Gas: " + str(int(tsfresh.feature_extraction.feature_calculators.quantile(gas.Quantity, q_gas))))

print("Lignite: " + str(int(tsfresh.feature_extraction.feature_calculators.quantile(lignite.Quantity, q_lignite))))

print("Nuclear: " + str(int(tsfresh.feature_extraction.feature_calculators.quantile(nuc.Quantity, q_nuc))))


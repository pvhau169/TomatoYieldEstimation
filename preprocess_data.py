import numpy as np
import pandas as pd

#constant 
general_path = '2016_spring/2016_spring_CC.csv'
yield_path = '2016_spring/2016_spring.csv'
data_type = "CC"
max_day = 80

if __name__ =="__main__":
    #read data
    general_data = pd.read_csv(general_path)
    yield_data = pd.read_csv(yield_path)
    column = general_data.keys()[:4]
    value_data = general_data[general_data.keys()[4:]]
    #generate new table with columns ["id", "yield", "variety", "reps"]
    df_new = pd.DataFrame(columns=(reversed(general_data.keys()[:4])), data=(general_data[reversed(general_data.keys()[:4])].values))
    df_new["plantDate"] = yield_data["plantDate"]
    df_new["Mulching"] = yield_data["Mulching"]
    # df_new["daysAfterPlanting"] = 
    print(df_new.shape)
    print(value_data.keys())
    

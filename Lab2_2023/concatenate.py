import numpy as np
import pandas as pd
import os

address = os.getcwd()
i = True


for filename in os.listdir(address):
    f = os.path.join(address, filename) 
    if(f.endswith('.dat')):
        df = np.loadtxt(f)
        if i:
            data = np.empty(df.shape)
            data = df
            print("henlo")
            i = False
        else:
            data = np.vstack([data,df])        
np.savetxt("data.txt",data)
        
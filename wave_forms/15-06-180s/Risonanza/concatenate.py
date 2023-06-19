import numpy as np
import pandas as pd
import os

address = os.getcwd()
i = True
I = []
Q = []
freq = []
print("henlo")
for filename in os.listdir(address):
    f = os.path.join(address, filename) 

    if(f.endswith('.dat')):
        df = np.loadtxt(f)
        I_value = df[:,0].mean()
        #print(I_value)
        Q_value = df[:,1].mean()
        #print(Q_value)
        f_value = df[0,3]
        #print(f_value)
        I.append(I_value)
        Q.append(Q_value)
        freq.append(f_value)
      
data = np.column_stack((I,Q,freq))     
np.savetxt("data.txt",data)
        
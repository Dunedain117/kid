import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
from tqdm import tqdm

i_c, q_c = 1.699 , 1.449
iq_ratio = 0.97
means = []
times = []
I = []
Q = []
def get_phase(data):
    q = (data.q - q_c) * iq_ratio + q_c
    return np.unwrap(2*np.arctan((q-q_c)/(data.i-i_c)))/2

for i in tqdm(range(20000)): #in teoria tutto
    try:
      df = pd.read_csv(f"signal{i}.dat", sep=' ')
      df.columns = ["i", "q", "t"]
    except:
      continue
    if np.sum(df.i > 4096): continue
    df = df.sort_values(["t"])
    df = df.reset_index()
    df.i *= 3.3/4095
    df.q *= 3.3/4095
    
    df["phase"] = get_phase(df)*1000
    for element in df.phase:
        means.append(element)
    for element in df.t:
        times.append(element)
    for element in df.i:
        I.append(element)
    for element in df.q:
        Q.append(element)

plt.plot(times[:1000000],I[:1000000],'.')
plt.plot(times[:1000000],Q[:1000000],'.')
plt.show()
means = np.array(means)
print(np.mean(means))
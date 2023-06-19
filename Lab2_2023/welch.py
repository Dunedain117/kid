from scipy.fft import rfft, rfftfreq
from scipy.signal import welch
import numpy as np
import pandas as pd


i_c, q_c = 1.699 , 1.449
iq_ratio = 0.878787878

def get_phase(frame):
    q = (frame.q - q_c) * iq_ratio + q_c
    return np.unwrap(2*np.arctan((frame.q-q_c)/(frame.i-i_c)))/2
def get_amp(data):
    q = (data.q - q_c) * iq_ratio + q_c
    return np.sqrt((q-q_c)**2 + (data.i-i_c)**2)

df = pd.read_csv('data.txt',sep = ' ')
df.columns = ["i", "q", "t"]
df = df.sort_values(["t"])

off = 43.085
off_vec = np.full(df.i.shape,off)
df.i = df.i - off_vec
df.i *= 3.3/4095
df.q *= 3.3/4095
df.t *= 1/1000000
print(df.i, df.q)
sample_rate = 166666 #Hz
N = len(df.t)

x = get_amp(df)**2
x = 10*np.log10(x)
x = get_phase(df)
print(x)
print("starting welch")
freq,power = welch(x,sample_rate,nperseg = 512,average='mean')
import matplotlib.pyplot as plt
plt.plot(freq,np.log10(power))
#plt.ylim([0,70000])
#plt.xlim([0,120000])
plt.grid()
plt.savefig("welch.png")
plt.show()
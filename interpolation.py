from scipy.interpolate import interp1d
import numpy as np
import pandas as pd

ggafile = open("filepath/161201N.GGA")
sbfile = open("filepath/161201.SB")
hvefile = open("filepath/161201.HVE")
E97lst = []
N97lst = []
Elst = []
Nlst = []
Tlst = []
Alst = [] #antenna
Ulst = [] #undulation

for line in ggafile:
  l_data = line.split(",")
  n = float(l_data[8])
  e = float(l_data[10])
  #convert mm to dd
  N = np.floor(n/100)+(n-np.floor(n/100)*100)/60
  E = np.floor(e/100)+(e-np.floor(e/100)*100)/60
  Tlst.append(float(l_data[0]))
  N97lst.append(float(l_data[1]))
  E97lst.append(float(l_data[2]))
  Nlst.append(N)
  Elst.append(E)
  Alst.append(float(l_data[15]))
  Ulst.append(float(l_data[17]))
#time series data interpolation function 
E97_t = interp1d(Tlst,E97lst)
N97_t = interp1d(Tlst,N97lst)
E_t = interp1d(Tlst,Elst)
N_t = interp1d(Tlst,Nlst)
A_t = interp1d(Tlst,Alst)
U_t = interp1d(Tlst,Ulst)


hvelst = []
timelst = []
for line in hvefile:
  l_data = line.split(",")
  timelst.append(float(l_data[0]))
  hvelst.append(float(l_data[1]))
#time series data interpolation function
hve_t = interp1d(timelst, hvelst)


#以sb file 為基準
time = []
depth = []
heave = []
E = []
N = []
lat = []
lon = []
antenna = []
undulation = []
method = []

for line in sbfile:
  l_data = line.split(",")
  Ts = float(l_data[0])
  sb = float(l_data[1])
  #由於看航線圖可以發現頭與尾的資料最終不會列入主測線區域，
  #因此時間的選擇就選三個資料中開始時間點最晚，
  #以及結束時間點最早作為閥值。
  if Ts >= 42705.65996986 and Ts<= 42705.70152604:
    time.append(Ts)
    depth.append(sb)
    #interpolation
    heave.append(hve_t(Ts))
    N.append(np.around(N97_t(Ts),3))
    E.append(np.around(E97_t(Ts),3))
    lat.append(np.around(N_t(Ts),7))
    lon.append(np.around(E_t(Ts),7))
    antenna.append(np.around(A_t(Ts),3))
    undulation.append(np.around(U_t(Ts),3))
    method.append("SB")

#dataframe
df = pd.DataFrame()
df.insert(0,"Time",time)
df.insert(1,"Depth",depth)
df.insert(2,"Heave Compensation",heave)
df.insert(3,"E",E)
df.insert(4,"N",N)
df.insert(5,"longitude",lon)
df.insert(6,"latitude",lat)
df.insert(7,"Antenna Height",antenna)
df.insert(8,"Undulation",undulation)
df.insert(9,"Survey Method", method)
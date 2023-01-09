import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

#hve EDA
hvefile = open("filepath/161201.HVE")
time = []
heave = []
for line in hvefile:
  one = line.split(",")
  time.append(float(one[0]))
  heave.append(float(one[1]))
plt.plot(time, heave)
plt.title("Heave compensation by time")
plt.xlabel("Time")
plt.ylabel("Heave compensation")
plt.show()

#sb EDA
sbfile = open("filepath/161201.SB")
time = []
depth = []
for line in sbfile:
  one = line.split(",")
  time.append(float(one[0]))
  depth.append(float(one[1]))
plt.plot(time, depth)
plt.title("Water depth by time")
plt.xlabel("Time")
plt.ylabel("Depth (m)")
plt.show()

#GGA route EDA
ggafile = open("filepath/161201N.GGA")
lon_plot = []
lat_plot = []
time_plot = []
for line in ggafile:
  l_data = line.split(",")
  lon_plot.append(float(l_data[2]))
  lat_plot.append(float(l_data[1]))
  time_plot.append(float(l_data[0]))

plt.figure(dpi=100, figsize=(8,4))
plt.scatter(lon_plot, lat_plot, marker="o", s=3.5, c=time_plot, cmap="gist_rainbow")
plt.xlabel("lon")
plt.ylabel("lat")
plt.title("Route (TM2)")
x_major_locator=MultipleLocator(50)
y_major_locator=MultipleLocator(50)
ax=plt.gca()
ax.set_aspect(1)
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)
plt.colorbar()
plt.show()

#GGA route EDA(plotly)
ggafile = open("filepath/161201N.GGA")
lon_plot = []
lat_plot = []
time_plot = []
for line in ggafile:
  l_data = line.split(",")
  lon_plot.append(float(l_data[2]))
  lat_plot.append(float(l_data[1]))
  time_plot.append(float(l_data[0]))

fig = px.scatter(x=lon_plot, y=lat_plot, color=time_plot, 
                 color_continuous_scale="rainbow")
fig

#GGA height EDA
ggafile = open("filepath/161201N.GGA")
time = []
altitude = []
n = []
for line in ggafile:
  one = line.split(",")
  time.append(float(one[0]))
  altitude.append(float(one[15]))
  n.append(float(one[17]))

plt.plot([], [], color='aqua', label = 'Geoidal separation (m)')
plt.plot([], [], color='g', label = 'Antenna altitude (m)')
plt.stackplot(time, n, altitude, colors= ['aqua', 'g'])
plt.title('Ellipsoid Height')
plt.xlabel("Time")
plt.legend()
plt.show()
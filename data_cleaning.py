import pandas as pd
#確認基準方向: "向上為正(水面以上為正值)"
#在dataframe新增兩個欄位: Water Depth、EH
depth = df["Depth"]
hve = df["Heave Compensation"]
waterDepth = []
for i in range(73670):
  water = depth[i] - depth[i]*2 + hve[i]
  waterDepth.append(round(water,3))
a = df["Antenna Height"]
u = df["Undulation"]
ellipsoid = []
for i in range(73670):
  e = a[i] + u[i]
  ellipsoid.append(round(e,3))
df.insert(10,"Water Depth",waterDepth)
df.insert(11,"EH",ellipsoid)

# REMOVE Water Depth outliers
# Computing IQR
Q1 = df['Water Depth'].quantile(0.25)
Q3 = df['Water Depth'].quantile(0.75)
IQR = Q3 - Q1
print(IQR,Q3,Q1,Q1 - 1.5*IQR,Q3+1.5*IQR )
# Filtering Values between Q1-1.5IQR and Q3+1.5IQR
filter = df[(df["Water Depth"] >= (Q1 - 1.5*IQR)) & (df["Water Depth"] <= 0)]

# REMOVE EH outliers
Q1 = filter['Antenna Height'].quantile(0.25)
Q3 = filter['Antenna Height'].quantile(0.75)
IQR = Q3 - Q1
print(IQR,Q3,Q1,Q1 - 1.5*IQR,Q3+1.5*IQR )
# Filtering Values between Q1-1.5IQR and Q3+1.5IQR
filter_new = filter[(filter["Antenna Height"] >= (Q1 - 1.5*IQR)) & (filter["Antenna Height"] <= Q3 + 1.5*IQR)]

filter_new.to_csv("filepath/hydroFinalData.csv",index=False)
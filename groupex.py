#1: Import Data 
from matplotlib.dates import num2date
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm

pd.options.mode.chained_assignment = None 

df=pd.read_csv('https://raw.githubusercontent.com/jivizcaino/PWT_10.0/main/pwt100.csv', encoding='latin-1')

print(df)

#2: Choose a Year to perform Developing Accounting Analysis

# Subset with variables of interest
subset= df[['country','countrycode', 'year','cgdpo', 'emp', 'avh','hc', 'cn','labsh','ctfp','pop']] 
subset.set_index('country')
print(subset)

subset.to_csv('pwt_subset.csv', index=False)

# Descriptive Statistics for years 2010-2019
print(subset[subset['year']==2010].describe())
print(subset[subset['year']==2011].describe())
print(subset[subset['year']==2012].describe())
print(subset[subset['year']==2013].describe())
print(subset[subset['year']==2014].describe())
print(subset[subset['year']==2015].describe())
print(subset[subset['year']==2016].describe())
print(subset[subset['year']==2017].describe())
print(subset[subset['year']==2018].describe())
print(subset[subset['year']==2019].describe())

# Choice of Year = 2019  (latest avaliable with max observations)
subset_2019=subset[subset['year']==2019]
print(subset_2019)

# Clean database discarding countries with NaN values
df1= subset_2019.dropna()
print(df1)



#3: Descriptive Statistics 

#Generate Variables 
df1['gdppw']=df1['cgdpo']/df1['emp']                                #Income per worker
df1['gdpph']=(df1['cgdpo'])/(df1['avh']*df1['emp'])                 #Income per hour worker
df1['gdpphc']=(df1['cgdpo'])/(df1['emp']*df1['hc'])                 #Income per unit of Human Capital
df1['gdpphch']=(df1['cgdpo'])/(df1['emp']*df1['avh']*df1['hc'])     #Income per hour of Human Capital


#Descriptive Statistics 
stats_gdppw=df1['gdppw'].describe()
print(stats_gdppw)

stats_gdpph=df1['gdpph'].describe()
print(stats_gdpph)

stats_gdpphc=df1['gdpphc'].describe()
print(stats_gdpphc)

stats_gdpphch=df1['gdpphch'].describe()
print(stats_gdpphch)


#Richest and Poorest Countries 
max_gdppw=df1.loc[df1['gdppw']==df1['gdppw'].max()]
print(max_gdppw)
min_gdppw=df1.loc[df1['gdppw']==df1['gdppw'].min()] 
print(min_gdppw)

#Percentiles for GDP per worker (gdppw)
df1['gdppwpct']=df1.gdppw.rank(pct=True)
print(df1.query("gdppwpct<=0.05"))                      #5th Percentile
print(df1.query("gdppwpct<=0.1"))                       #10th Percentile
print(df1.query("gdppwpct>=0.9"))                       #90th Percentile
print(df1.query("gdppwpct>=0.95"))                      #95th Percentile

#Percentiles for GDP per hour worked (gdpph)
df1['gdpphpct']=df1.gdpph.rank(pct=True)
print(df1.query("gdpphpct<=0.05"))                      #5th Percentile
print(df1.query("gdpphpct<=0.1"))                       #10th Percentile
print(df1.query("gdpphpct>=0.9"))                       #90th Percentile
print(df1.query("gdpphpct>=0.95"))                      #95th Percentile

#Percentiles for GDP per unit of Human Capital (gdpphc)
df1['gdpphcpct']=df1.gdpph.rank(pct=True)
print(df1.query("gdpphcpct<=0.05"))                     #5th Percentile
print(df1.query("gdpphcpct<=0.1"))                      #10th Percentile
print(df1.query("gdpphcpct>=0.9"))                      #90th Percentile
print(df1.query("gdpphcpct>=0.95"))                     #95th Percentile

#Percentiles for GDP per hour of Human Capital (gdpphch)
df1['gdpphchpct']=df1.gdpph.rank(pct=True)
print(df1.query("gdpphchpct<=0.05"))                    #5th Percentile
print(df1.query("gdpphchpct<=0.1"))                     #10th Percentile
print(df1.query("gdpphchpct>=0.9"))                     #90th Percentile
print(df1.query("gdpphchpct>=0.95"))                    #95th Percentile



#Log Variance GDP per worker
var_gdppw=df1['gdppw'].var()
logvar_gdppw=np.log(var_gdppw)
print('Log Variance of GDP per worker= ',logvar_gdppw)


#Log Variance (other measures)          # not sure if needed? Maybe later ****
var_gdpph=df1['gdpph'].var()
logvar_gdpph=np.log(var_gdpph)
print('Log Variance of GDP per Hour worked= ',logvar_gdpph)

var_gdpphc=df1['gdpphc'].var()
logvar_gdpphc=np.log(var_gdpphc)
print('Log Variance of GDP per unit of Human Capital= ',logvar_gdpphc)

var_gdpphch=df1['gdpphch'].var()
logvar_gdpphch=np.log(var_gdpphch)
print('Log Variance of GDP per hour of Human Capital= ',logvar_gdpphch)


#Ratio between Percentiles GDP per worker

# 90th and 10th Percentile
percentile_90 = df1['gdppw'].quantile(0.90)
percentile_10= df1['gdppw'].quantile(0.10)
ratio_90_to_10 = percentile_90 / percentile_10
print(ratio_90_to_10)

# 95th and 5th Percentile
percentile_95 = df1['gdppw'].quantile(0.95)
percentile_5= df1['gdppw'].quantile(0.05)
ratio_95_to_5 = percentile_95 / percentile_5
print(ratio_95_to_5)

# Richest and Poorest 
ratio_max_to_min = max_gdppw / min_gdppw
print(ratio_max_to_min)



#4: Can differences in human capital and hours worked help to explain differences in standard of living across countries? If so, by what magnitude?

result=sm.ols("gdppw ~ hc + avh", data=df1).fit()
print(result.params)

#A unitary increase in the human capital index is positively correlated with GDP per worker by a magnitude of $38,705.396
#A unitary increase in average hours worked is negatively correlated with GDP per worker by a magnitude of $37.8


#5: Produce Scatterplots

# Produce scatterplots for 𝑘, ℎ, 𝑎𝑣ℎ, 𝛼, and 𝐴 (using cftp) against:
# log gdp per capita, per worker, per hour worked, and per unit of human capital. 
# Label the axis accordingly.
# Label your observations using the variable countrycode.


df1['gdppc']=df1['cgdpo']/df1['pop']        #Generate GDP per capita
df1['a']= 1-df1['labsh']                    #Generate alpha

#Generate Log Variables 
log_gdppc=np.log(df1['gdppc'])
df1['log_gdppc']=np.log(df1['gdppc'])
print(log_gdppc)

log_gdppw=np.log(df1['gdppw'])
df1['log_gdppw']=np.log(df1['gdppw'])
print(log_gdppw)

log_gdpph=np.log(df1['gdpph'])
df1['log_gdpph']=np.log(df1['gdpph'])
print(log_gdpph)

log_gdpphc=np.log(df1['gdpphc'])
df1['log_gdpphc']=np.log(df1['gdpphc'])
print(log_gdpphc)

print(df1)


#Scatterplots against GDP per worker
#Capital vs GDP per worker
x_axis = df1['cn']
y_axis = df1['log_gdppw']

plt.scatter(x_axis, y_axis)
plt.title("Capital vs Log GDP per worker")
plt.xlabel("Capital")
plt.ylabel("Log GDP per Worker")
#plt.show()


#Human Capital vs GDP per worker
x_axis = df1['hc']
y_axis = df1['log_gdppw']

plt.scatter(x_axis, y_axis)
plt.title("Human Capital vs Log GDP per worker")
plt.xlabel("Human Capital")
plt.ylabel("Log GDP per Worker")
#plt.show()


#Average Annual Hours vs GDP per worker
x_axis = df1['avh']
y_axis = df1['log_gdppw']

plt.scatter(x_axis, y_axis)
plt.title("Av Annual Hours vs Log GDP per worker")
plt.xlabel("Av Annual Hours")
plt.ylabel("Log GDP per Worker")
#plt.show()

#'a' vs GDP per worker
x_axis = df1['a']
y_axis = df1['log_gdppw']

plt.scatter(x_axis, y_axis)
plt.title("a vs Log GDP per worker")
plt.xlabel("a")
plt.ylabel("Log GDP per Worker")
#plt.show()

# TFP level at current PPPs vs GDP per worker
x_axis = df1['ctfp']
y_axis = df1['log_gdppw']

plt.scatter(x_axis, y_axis)
plt.title("TFP level at Current PPS vs Log GDP per worker")
plt.xlabel("ctfp")
plt.ylabel("Log GDP per Worker")
#plt.show()


#Scatterplots against GDP per capita
#Capital vs GDP per capita
x_axis = df1['cn']
y_axis = df1['log_gdppc']

plt.scatter(x_axis, y_axis)
plt.title("Capital vs Log GDP per Capita")
plt.xlabel("Capital")
plt.ylabel("Log GDP per Capita")
#plt.show()


#Human Capital vs GDP per Capita
x_axis = df1['hc']
y_axis = df1['log_gdppc']

plt.scatter(x_axis, y_axis)
plt.title("Human Capital vs Log GDP per Capita")
plt.xlabel("Human Capital")
plt.ylabel("Log GDP Capita")
#plt.show()


#Average Annual Hours vs GDP per Capita
x_axis = df1['avh']
y_axis = df1['log_gdppc']

plt.scatter(x_axis, y_axis)
plt.title("Av Annual Hours vs Log GDP per Capita")
plt.xlabel("Av Annual Hours")
plt.ylabel("Log GDP per Capita")
#plt.show()

#'a' vs GDP per Capita
x_axis = df1['a']
y_axis = df1['log_gdppc']

plt.scatter(x_axis, y_axis)
plt.title("a vs Log GDP per Capita")
plt.xlabel("a")
plt.ylabel("Log GDP per Capita")
#plt.show()

# TFP level at current PPPs vs GDP per Capita
x_axis = df1['ctfp']
y_axis = df1['log_gdppc']

plt.scatter(x_axis, y_axis)
plt.title("TFP level at Current PPS vs Log GDP per Capita")
plt.xlabel("ctfp")
plt.ylabel("Log GDP per Capita")
#plt.show()


#Scatterplots against GDP per hour worked
#Capital vs GDP per hour worked
x_axis = df1['cn']
y_axis = df1['log_gdpph']

plt.scatter(x_axis, y_axis)
plt.title("Capital vs Log GDP per Hour Worked")
plt.xlabel("Capital")
plt.ylabel("Log GDP per Hour Worked")
#plt.show()


#Human Capital vs GDP per hour worked
x_axis = df1['hc']
y_axis = df1['log_gdpph']

plt.scatter(x_axis, y_axis)
plt.title("Human Capital vs Log GDP per Hour Worked")
plt.xlabel("Human Capital")
plt.ylabel("Log GDP per Hour Worked")
#plt.show()


#Average Annual Hours vs GDP per hour worked
x_axis = df1['avh']
y_axis = df1['log_gdpph']

plt.scatter(x_axis, y_axis)
plt.title("Av Annual Hours vs Log GDP per Hour Worked")
plt.xlabel("Av Annual Hours")
plt.ylabel("Log GDP per Hour Worked")
#plt.show()

#'a' vs GDP per hour worked
x_axis = df1['a']
y_axis = df1['log_gdpph']

plt.scatter(x_axis, y_axis)
plt.title("a vs Log GDP per Hour Worked")
plt.xlabel("a")
plt.ylabel("Log GDP per Hour Worked")
#plt.show()

# TFP level at current PPPs vs GDP per hour worked
x_axis = df1['ctfp']
y_axis = df1['log_gdpph']

plt.scatter(x_axis, y_axis)
plt.title("TFP level at Current PPS vs Log GDP per Hour Worked")
plt.xlabel("ctfp")
plt.ylabel("Log GDP per Hour Worked")
#plt.show()


#Scatterplots against GDP per unit of Human Capital
#Capital vs GDP unit of Human Capital
x_axis = df1['cn']
y_axis = df1['log_gdpphc']

plt.scatter(x_axis, y_axis)
plt.title("Capital vs Log GDP per unit of Human Capital")
plt.xlabel("Capital")
plt.ylabel("Log GDP per unit of Human Capital")
#plt.show()


#Human Capital vs GDP per unit of Human Capital
x_axis = df1['hc']
y_axis = df1['log_gdpphc']

plt.scatter(x_axis, y_axis)
plt.title("Human Capital vs Log GDP per unit of Human Capital")
plt.xlabel("Human Capital")
plt.ylabel("Log GDP per unit of Human Capital")
#plt.show()


#Average Annual Hours vs GDP per unit of Human Capital
x_axis = df1['avh']
y_axis = df1['log_gdpphc']

plt.scatter(x_axis, y_axis)
plt.title("Av Annual Hours vs Log GDP per unit of Human Capital")
plt.xlabel("Av Annual Hours")
plt.ylabel("Log GDP per unit of Human Capital")
#plt.show()

#'a' vs GDP per unit of Human Capital
x_axis = df1['a']
y_axis = df1['log_gdpphc']

plt.scatter(x_axis, y_axis)
plt.title("a vs Log GDP per unit of Human Capital")
plt.xlabel("a")
plt.ylabel("Log GDP per unit of Human Capital")
#plt.show()

# TFP level at current PPPs vs GDP per unit of Human Capital
x_axis = df1['ctfp']
y_axis = df1['log_gdpphc']

plt.scatter(x_axis, y_axis)
plt.title("TFP level at Current PPS vs Log GDP per unit of Human Capital")
plt.xlabel("ctfp")
plt.ylabel("Log GDP per unit of Human Capital")
plt.show()









#6 Measures of Success

df1['ykh']=(df1['cn']**(1-df1['labsh']))*(df1['hc']**(df1['labsh']))              #trying to get formula for this
stats_ykh=df1['ykh'].describe()
print(stats_ykh)

df1['y']=df1['ctfp']*df1['ykh']
stats_y=df1['y'].describe()
print(stats_y)

#Success1: var[log(ykh)/var[log(y)]]

df1['log_ykh']=np.log(df1['ykh'])
var_log_ykh=df1['log_ykh'].var()

df1['log_y']=np.log(df1['y'])
var_log_y=df1['log_y'].var()

success1=var_log_ykh / var_log_y
print('Success Measure 1: ', success1)

#Success2: [(ykh90/ykh10)/(y90/y10)]  (e.g. 90th & 10th percentiles)
# 99th and 1st Percentile
# ykh ratios
ykh_percentile_99 = df1['ykh'].quantile(0.99)
ykh_percentile_1 = df1['ykh'].quantile(0.01)
ykh_99_to_1 = ykh_percentile_99 / ykh_percentile_1
#print(ykh_99_to_1)

#'y' ratios
y_percentile_99 = df1['y'].quantile(0.99)
y_percentile_1 = df1['y'].quantile(0.01)
y_99_to_1 = y_percentile_99 / y_percentile_1
#print(y_99_to_1)

success2_99_to_1 = ykh_99_to_1 / y_99_to_1
print('Sucess Measure 2 for 99th and 1st percentiles: ', success2_99_to_1)

# 95th and 5th Percentile
# ykh ratios
ykh_percentile_95 = df1['ykh'].quantile(0.95)
ykh_percentile_5 = df1['ykh'].quantile(0.05)
ykh_95_to_5 = ykh_percentile_95 / ykh_percentile_5
#print(ykh_95_to_5)

#'y' ratios
y_percentile_95 = df1['y'].quantile(0.95)
y_percentile_5 = df1['y'].quantile(0.05)
y_95_to_5 = y_percentile_95 / y_percentile_5
#print(y_95_to_5)

success2_95_to_5 = ykh_95_to_5 / y_95_to_5
print('Sucess Measure 2 for 95th and 5th percentiles: ', success2_95_to_5)

# 90th and 10th Percentile
# ykh ratios
ykh_percentile_90 = df1['ykh'].quantile(0.90)
ykh_percentile_10 = df1['ykh'].quantile(0.1)
ykh_90_to_10= ykh_percentile_90/ ykh_percentile_10
#print(ykh_90_to_10)

#'y' ratios
y_percentile_90 = df1['y'].quantile(0.9)
y_percentile_10 = df1['y'].quantile(0.1)
y_90_to_10 = y_percentile_90 / y_percentile_10
#print(y_90_to_10)

success2_90_to_10 = ykh_90_to_10 / y_90_to_10
print('Sucess Measure 2 for 90th and 10th percentiles: ', success2_90_to_10)

# 75th and 25th Percentile
#'ykh' ratios
ykh_percentile_75 = df1['ykh'].quantile(0.75)
ykh_percentile_25 = df1['ykh'].quantile(0.25)
ykh_75_to_25 = ykh_percentile_75 / ykh_percentile_25
#print(ykh_75_to_25)

#'y' ratios
y_percentile_75 = df1['y'].quantile(0.75)
y_percentile_25 = df1['y'].quantile(0.25)
y_75_to_25 = y_percentile_75 / y_percentile_25
#print(y_75_to_25)

success2_75_to_25 = ykh_75_to_25 / y_75_to_25
print('Sucess Measure 2 for 75th and 25th percentiles: ', success2_75_to_25)



# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 10:44:53 2020

@author: bruno
"""

import requests

import json

import pandas as pd


import matplotlib.pyplot as plt

import seaborn as sns


url = 'https://covid-tracker-us.herokuapp.com/v2/locations/'

#%%
# =============================================================================
# EXPLORATORY ANALYSIS
# =============================================================================

# =============================================================================
# 3 lockdown strategies
# =============================================================================
cod_pais_str = ['AR','SE','KR']

paises = []
data = {}
for pais in cod_pais_str:
    params = {'country_code':pais,'timelines':'true'}
    
    r = requests.get(url,params = params)
    
    dataj = json.loads(r.text)
    

    confirmed = (dataj['locations'][0]['timelines']['confirmed']['timeline'])
    #recovered = (dataj['locations'][0]['timelines']['recovered']['timeline'])
    deaths = (dataj['locations'][0]['timelines']['deaths']['timeline'])
    fechas = pd.to_datetime(list(confirmed.keys()))
    
    pop = dataj['locations'][0]['country_population'] 
    
    df = pd.DataFrame(data = {'Confirmed': list(confirmed.values()),
                             #'Recovered': list(recovered.values()),
                             'Deaths'    : list(deaths.values())},
                             index = fechas) 
    df = (df/pop)*100000
    data[pais] = df
    paises.append(dataj['locations'][0]['country'])

# =============================================================================
# Confirmados
# =============================================================================
# for pais in cod_pais_str:
#     data[pais]['Confirmed'].plot.area(stacked = False)
# plt.title('Confirmados')
# plt.legend(paises)
# plt.ylabel('Casos cada 100000 habitantes')
# plt.show()

# =============================================================================
# Fallecidos 
# =============================================================================
sns.set_theme()
for pais in cod_pais_str:
    data[pais]['Deaths'].plot(stacked = False)
plt.title('Fallecidos')
plt.legend(paises)
plt.ylabel('Casos cada 100000 habitantes')
#plt.show()
plt.savefig('3_lockdown.svg')
#%%
# =============================================================================
# Europa
# =============================================================================

cod_pais_eu = ['ES','SE','FR','IT']

paises = []
data = {}
for pais in cod_pais_eu:
    params = {'country_code':pais,'timelines':'true'}
    
    r = requests.get(url,params = params)
    
    dataj = json.loads(r.text)
    

    confirmed = (dataj['locations'][0]['timelines']['confirmed']['timeline'])
    #recovered = (dataj['locations'][0]['timelines']['recovered']['timeline'])
    deaths = (dataj['locations'][0]['timelines']['deaths']['timeline'])
    fechas = pd.to_datetime(list(confirmed.keys()))
    
    pop = dataj['locations'][0]['country_population'] 
    
    df = pd.DataFrame(data = {'Confirmed': list(confirmed.values()),
                             #'Recovered': list(recovered.values()),
                             'Deaths'    : list(deaths.values())},
                             index = fechas) 
    df = (df/pop)*100000
    data[pais] = df
    paises.append(dataj['locations'][0]['country'])


#Confirmados
# =============================================================================
# for pais in cod_pais_eu:
#     data[pais]['Confirmed'].plot.area(stacked = False)
# plt.title('Confirmados')
# plt.legend(paises)
# plt.ylabel('Casos cada 100000 habitantes')
# plt.show()
# =============================================================================

# =============================================================================
#Fallecidos Europa
# =============================================================================
sns.set_theme()
for pais in cod_pais_eu:
    data[pais]['Deaths'].plot(stacked = False)
plt.title('Fallecidos')
plt.legend(paises)
plt.ylabel('Casos cada 100000 habitantes')
#plt.show()
plt.savefig('Europa.svg')

#%%
# =============================================================================
# Latinoamerica
# =============================================================================


cod_pais_lat = ['AR','BR','UY','CL']

paises = []
data = {}
for pais in cod_pais_lat:
    params = {'country_code':pais,'timelines':'true'}
    
    r = requests.get(url,params = params)
    
    dataj = json.loads(r.text)

    confirmed = (dataj['locations'][0]['timelines']['confirmed']['timeline'])
    #recovered = (dataj['locations'][0]['timelines']['recovered']['timeline'])
    deaths = (dataj['locations'][0]['timelines']['deaths']['timeline'])
    fechas = pd.to_datetime(list(confirmed.keys()))
    
    pop = dataj['locations'][0]['country_population'] 
    
    df = pd.DataFrame(data = {'Confirmed': list(confirmed.values()),
                             #'Recovered': list(recovered.values()),
                             'Deaths'    : list(deaths.values())},
                             index = fechas) 
    df = (df/pop)*100000
    data[pais] = df
    paises.append(dataj['locations'][0]['country'])

sns.set_theme()
# =============================================================================
# #Confirmados Latinoamerica
# =============================================================================
# for pais in cod_pais_lat:
#     data[pais]['Confirmed'].plot.area(stacked = False)
# plt.title('Confirmados')
# plt.legend(paises)
# plt.ylabel('Casos cada 100000 habitantes')
# plt.show()

# =============================================================================
# Fallecidos 
# =============================================================================

for pais in cod_pais_lat:
    data[pais]['Deaths'].plot(stacked = False)
plt.title('Fallecidos')
plt.legend(paises)
plt.ylabel('Casos cada 100000 habitantes')
#plt.show()
plt.savefig('LAT.svg')
#%%
# =============================================================================
# Asia
# =============================================================================
cod_pais_asia = ['JP','KR','TW','VN']
paises = []
data = {}
for pais in cod_pais_asia:
    params = {'country_code':pais,'timelines':'true'}
    
    r = requests.get(url,params = params)
    
    dataj = json.loads(r.text)
    

    confirmed = (dataj['locations'][0]['timelines']['confirmed']['timeline'])
    #recovered = (dataj['locations'][0]['timelines']['recovered']['timeline'])
    deaths = (dataj['locations'][0]['timelines']['deaths']['timeline'])
    fechas = pd.to_datetime(list(confirmed.keys()))
    
    pop = dataj['locations'][0]['country_population'] 
    
    df = pd.DataFrame(data = {'Confirmed': list(confirmed.values()),
                             #'Recovered': list(recovered.values()),
                             'Deaths'    : list(deaths.values())},
                             index = fechas) 
    df = (df/pop)*100000
    data[pais] = df
    paises.append(dataj['locations'][0]['country'])


# =============================================================================
# #Confirmados
# =============================================================================
# for pais in cod_pais_asia:
#     data[pais]['Confirmed'].plot(stacked = False)
# plt.title('Confirmados')
# plt.legend(paises)
# plt.ylabel('Casos cada 100000 habitantes')
# plt.show()
# =============================================================================
# Fallecidos
# =============================================================================
sns.set_theme()
for pais in cod_pais_asia:
    data[pais]['Deaths'].plot(stacked = False)
plt.title('Fallecidos')
plt.legend(paises)
plt.ylabel('Casos cada 100000 habitantes')
#plt.show()
plt.savefig('Asia.svg')
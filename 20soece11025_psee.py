# -*- coding: utf-8 -*-
"""20SOECE11025_PSEE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nZ8aR_Cjupj2JbKzv9ia0FBkZ1UerUuO
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import folium

df = pd.read_csv('COVID-19 Coronavirus.csv')
df.head()

from google.colab import drive
drive.mount('/content/drive')

df.isnull().sum()

df.info()

pip install plotly==5.7.0

import plotly.graph_objects as go
import pandas as pd


fig = go.Figure(data=go.Choropleth(
    locations = df['ISO 3166-1 alpha-3 CODE'],
    z = df['Population'],
    text = df['Country'],
    colorscale = 'viridis',
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    #colorbar_tickprefix = '$',
    colorbar_title = 'Population in Billions',
))

fig.update_layout(
    title_text='The current world population by countries',
    title_x = 0.50,
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        text="Source: Worldometer's global COVID-19 statistics",
        showarrow = False
    )]
)
fig.show()

"""Visualizing Total COVID 19 Coronavirus cases"""

fig = go.Figure(data=go.Choropleth(
    locations = df['ISO 3166-1 alpha-3 CODE'],
    z = df['Total Cases'],
    text = df['Country'],
    colorscale = 'plasma',
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    #colorbar_tickprefix = '$',
    colorbar_title = 'COVID 19 cases in Millions',
))

fig.update_layout(
    title_text='Total COVID 19 Coronavirus cases',
    title_x = 0.50,
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        text="Source: Worldometer's global COVID-19 statistics",
        showarrow = False
    )]
)
fig.show()

"""Visualizing COVID 19 Coronavirus Most Affected Continents"""

df['Continent'] = df['Continent'].replace({'Africa':'africa', 'Asia': 'asia', 'Europe': 'europe', 
                                           'Latin America and the Caribbean': 'southAmerica',
                                           'Northern America':'northAmerica','Oceania':'oceania'})

df_cont = df[["Country", "Total Cases", "Continent"]]
df_cont = df_cont.groupby("Continent").sum()
df_cont = df_cont.reset_index()
df_cont

# import json
# world_geo = os.path.join('world.geojson') # geojson file

# # create a plain world map
# world_map = folium.Map(location=[40, 0], zoom_start=2)

# # generate choropleth map using the total immigration of each country to Australia from 1980 to 2008
# folium.Choropleth(
#     geo_data=world_geo,
#     data=df_cont,
#     columns=['Continent', 'Total Cases'],
#     key_on='feature.properties.continent',
#     fill_color='YlOrRd', 
#     fill_opacity=0.7, 
#     line_opacity=0.2,
#     legend_name='COVID 19 Coronavirus Most Affected Continents'
# ).add_to(world_map)

# # display map
# world_map

"""Visualizing Continents with most deaths related to COVID 19 Coronavirus reported"""

df_cont = df[["Country", "Total Deaths", "Continent"]]
df_cont = df_cont.groupby("Continent").sum()
df_cont = df_cont.reset_index()
df_cont

"""Visualizing Deaths per total cases among five continents"""

df_cont = df[["Country", "Death percentage", "Continent"]]
df_cont = df_cont.groupby("Continent").sum()
df_cont = df_cont.reset_index()
df_cont = df_cont.sort_values(by = "Death percentage", ascending = False)
df_cont

plt.figure(figsize = (12,7))
color = ["#00FF00","#0000FF", '#FF0000', "#5cb85c", "#5bc0de", "#FF6600"]
ax = sns.barplot(x=df_cont['Continent'], y=df_cont['Death percentage'].round(2), palette = color)
ax.set_title ("Number of deaths / Total cases",fontsize= 16)
ax.legend (fontsize= 10, bbox_to_anchor=(1.1, 0.5))
ax.xaxis.set_tick_params(labelsize=10)
ax.axes.get_yaxis().set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
for rect in ax.patches:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height + 1, 
                str(height), ha='center', va='bottom', fontsize = 10)

"""Visualizing Country wise deaths /total cases"""

import plotly.express as px

fig = px.choropleth(df, locations="ISO 3166-1 alpha-3 CODE",
                    color="Death percentage", # Total is a column of df
                    hover_name="Country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plotly3)
fig.show()

import matplotlib.pyplot as plt
import numpy as np

df_cont = df[["Country", "Death percentage", "Continent"]]
df_cont = df_cont.groupby("Continent").sum()
df_cont = df_cont.reset_index()
df_cont = df_cont.sort_values(by = "Death percentage", ascending = False)
df_cont

df_cont = df[["Country", "Death percentage", "Continent"]]

import pandas as pd
from matplotlib import pyplot as plt

data=pd.read_csv(r"COVID-19 Coronavirus.csv")
data

data.head()
df=pd.DataFrame(data)

data=df.sort_values(by="Death percentage",ascending=False)

data.Country.head(5)

name=data.Country.head(5)
D_percentage=df['Death percentage'].head(5)

fig=plt.figure(figsize=(10,7))
plt.bar(name,D_percentage,color='lightgreen')
plt.title('TOP 5 COUNTRYS WITH DEATH PERCENTAGES')
plt.show()

plt.title('TOP 5 COUNTRY WITH DEATH PERCENTAGES')
plt.pie(D_percentage,labels=name)
plt.legend(D_percentage,name,
          title ="Name",
          loc ="center left",
          bbox_to_anchor =(1, 0, 0.5, 1))
plt.show()

data

data.head(5)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Y=data.iloc[158:,5].values
R=data.iloc[158:,5].values
D=data.iloc[158:,5].values
X=data.iloc[158:,5]
plt.figure(figsize=(25,11))

ax = plt.axes()
ax.grid(linewidth=0.4, color='#8f8f8f')
 
ax.set_facecolor("black")
ax.set_xlabel('\nPopulation',size=25,color='#4bb4f2')
ax.set_ylabel('Confirmed Cases\n',
              size=25,color='#4bb4f2')
 
ax.plot(X,Y,
        color='#1F77B4',
        marker='o',
        linewidth=4,
        markersize=15,
        markeredgecolor='#035E9B')

data.head(5)

data1=data.head(5)

data1

from matplotlib import style
data=data1['Total Cases']
plt.style.use('dark_background')
plt.plot(data)
plt.show()

from matplotlib import style
data=data1['Population']
plt.style.use('dark_background')
plt.plot(data)
plt.show()

from matplotlib import style
data=data1['Population']
plt.style.use('ggplot')
plt.plot(data)
plt.show()


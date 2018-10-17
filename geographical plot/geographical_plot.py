# Ref: https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf

import pandas as pd
import plotly as py
import plotly.graph_objs as go 


'''
type = 'choropleth',
locations = list of states
locationmode = 'USA-states'
colorscale= 'pairs' | 'Greys' | 'Greens' | 'Bluered' | 'Hot' | 'Picnic' | 'Portland' | 'Jet' | 'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'
https://plot.ly/python/heatmap-and-contour-colorscales/
text= list or array of text to display per point
z= array of values on z axis (color of state)
colorbar = {'title':'Colorbar Title'})
'''

data = dict(type = 'choropleth',
            locations = ['AZ','CA','NY'],
            locationmode = 'USA-states',
            colorscale= 'Portland',
            text= ['text1','text2','text3'],
            z=[1.0,2.0,3.0],
            colorbar = {'title':'Colorbar Title'})

layout = dict(geo = {'scope':'usa'})

choromap = go.Figure(data = [data],layout = layout)

py.offline.plot(choromap)


### Real Data US Map Choropleth

df = pd.read_csv('2011_US_AGRI_Exports')
print df.head()

data = dict(type='choropleth',
            colorscale = 'YlOrRd',
            locations = df['code'],
            z = df['total exports'],
            locationmode = 'USA-states',
            text = df['text'],
            marker = dict(line = dict(color = 'rgb(255,255,255)',width = 2)),
            colorbar = {'title':"Millions USD"}
            ) 

layout = dict(title = '2011 US Agriculture Exports by State',
              geo = dict(scope='usa',
                         showlakes = True,
                         lakecolor = 'rgb(85,173,240)')
             )

choromap = go.Figure(data = [data],layout = layout)

py.offline.plot(choromap)


# World Choropleth Map
df = pd.read_csv('2014_World_GDP')
print df.head()

data = dict(
        type = 'choropleth',
        locations = df['CODE'],
        z = df['GDP (BILLIONS)'],
        text = df['COUNTRY'],
        colorbar = {'title' : 'GDP Billions US'},
      ) 

layout = dict(
    title = '2014 Global GDP',
    geo = dict(
        showframe = False,
        projection = {'type':'mercator'}
    )
)

choromap = go.Figure(data = [data],layout = layout)

py.offline.plot(choromap)

import pandas as pd
import plotly as py
import plotly.graph_objs as go 


df = pd.read_csv('2014_World_Power_Consumption') 
print df.head()

data = dict(
        type = 'choropleth',
        colorscale = 'Viridis',
        reversescale = True,
        locations = df['Country'],
        locationmode = "country names",
        z = df['Power Consumption KWH'],
        text = df['Country'],
        colorbar = {'title' : 'Power Consumption KWH'},
      ) 

layout = dict(title = '2014 Power Consumption KWH',
                geo = dict(showframe = False,projection = {'type':'mercator'})
             )

choromap = go.Figure(data = [data],layout = layout)
py.offline.plot(choromap,validate=False)

# USA Choropleth
usdf = pd.read_csv('2012_Election_Data')
print usdf.head()

data = dict(type='choropleth',
            colorscale = 'Viridis',
            reversescale = True,
            locations = usdf['State Abv'],
            z = usdf['Voting-Age Population (VAP)'],
            locationmode = 'USA-states',
            text = usdf['State'],
            marker = dict(line = dict(color = 'rgb(255,255,255)',width = 1)),
            colorbar = {'title':"Voting-Age Population (VAP)"}
            ) 

layout = dict(title = '2012 General Election Voting Data',
              geo = dict(scope='usa',
                         showlakes = True,
                         lakecolor = 'rgb(85,173,240)')
             )

choromap = go.Figure(data = [data],layout = layout)
py.offline.plot(choromap,validate=False)

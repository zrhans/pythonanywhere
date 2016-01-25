"""
DATA,Chuva,Chuva_min,Chuva_max,VVE,VVE_min,VVE_max,DVE,DVE_min,DVE_max,Temp.,Temp._min,Temp._max,Umidade,Umidade_min,Umidade_max,Rad.,Rad._min,Rad._max,Pres.Atm.,Pres.Atm._min,Pres.Atm._max,Temp.Int.,Temp.Int._min,Temp.Int._max,CH4,CH4_min,CH4_max,HCnM,HCnM_min,HCnM_max,HCT,HCT_min,HCT_max,SO2,SO2_min,SO2_max,O3,O3_min,O3_max,NO,NO_min,NO_max,NO2,NO2_min,NO2_max,NOx,NOx_min,NOx_max,CO,CO_min,CO_max,MP10,MP10_min,MP10_max,MPT,MPT_min,MPT_max,Fin,Fin_min,Fin_max,Vin,Vin_min,Vin_max,Vout,Vout_min,Vout_max
"""
import plotly.plotly as py      # Every function in this module will communicate with an external plotly server
import plotly.graph_objs as go
import pandas as pd

DATAFILE = r'/home/zrhans/w3/bns/bns_2016-1.csv'

df = pd.read_csv(DATAFILE, parse_dates=True, sep=',', header=0, index_col='DATA')
x = df.index
y = df['Temp.']
y0 = df['Temp._min']
y1 = df['Temp._max']
#print(y)

# Definindo as series dedados
trace1 = go.Scatter(
  x = x,#["2015-12-01","2015-12-01 01:00:00","2015-12-01 02:00:00","2015-12-01 03:00:00","2015-12-01 04:00:00","2015-12-01 05:00:00"],
  y = y0,#[74.73,76.59,76.5,79.03,77.89,81.9,],
  name = 'T min',
  #hoverinfo='value+name',
  line=dict(
        shape='spline'
  )
)

trace2 = go.Scatter(
  x = x,#["2015-12-01","2015-12-01 01:00:00","2015-12-01 02:00:00","2015-12-01 03:00:00","2015-12-01 04:00:00","2015-12-01 05:00:00"],
  y = y,#[74.73,76.59,76.5,79.03,77.89,81.9,],
  name = 'T',
  fill='tonexty',
  #hoverinfo='value+name',
  line=dict(
        shape='spline'
  )
)

trace3 = go.Scatter(
  x = x,#["2015-12-01","2015-12-01 01:00:00","2015-12-01 02:00:00","2015-12-01 03:00:00","2015-12-01 04:00:00","2015-12-01 05:00:00"],
  y = y1,#[74.73,76.59,76.5,79.03,77.89,81.9,],
  fill='tonexty',
  name = 'T max',
  #hoverinfo='value+name',
  line=dict(
        shape='spline'
  )
)

# Edit the layout
layout = dict(
              font=dict(family='Courier New, monospace',),
              title = 'BNS01 - Temperatura do Ar - Medias horárias',
              xaxis = dict(title = 'Data'),
              yaxis = dict(title = 'Temperatura  - Celcius'),
              legend=dict(
                  y=0.5,
                  traceorder='reversed',
                  font=dict(
                      size=16
                  )
              )
         )

data = [trace1, trace2, trace3]

fig = dict(data=data, layout=layout)

# Tracando o objeto
py.plot(
  fig,
  filename='hans/oi_mundis',      # name of the file as saved in your plotly account
  sharing='public'
)                            # 'public' | 'private' | 'secret': Learn more: https://plot.ly/python/privacy


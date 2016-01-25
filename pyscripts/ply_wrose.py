"""
DATA,Chuva,Chuva_min,Chuva_max,VVE,VVE_min,VVE_max,DVE,DVE_min,DVE_max,Temp.,Temp._min,Temp._max,Umidade,Umidade_min,Umidade_max,Rad.,Rad._min,Rad._max,Pres.Atm.,Pres.Atm._min,Pres.Atm._max,Temp.Int.,Temp.Int._min,Temp.Int._max,CH4,CH4_min,CH4_max,HCnM,HCnM_min,HCnM_max,HCT,HCT_min,HCT_max,SO2,SO2_min,SO2_max,O3,O3_min,O3_max,NO,NO_min,NO_max,NO2,NO2_min,NO2_max,NOx,NOx_min,NOx_max,CO,CO_min,CO_max,MP10,MP10_min,MP10_max,MPT,MPT_min,MPT_max,Fin,Fin_min,Fin_max,Vin,Vin_min,Vin_max,Vout,Vout_min,Vout_max
"""
import plotly.plotly as py      # Every function in this module will communicate with an external plotly server
import plotly.graph_objs as go
import pandas as pd

DATAFILE = r'/home/zrhans/w3/bns/bns_2016-1.csv'

df = pd.read_csv(DATAFILE, parse_dates=True, sep=',', header=0, index_col='DATA')
x = df.DVE
y = df.VVE

#print(y)

# Definindo as series dedados
trace1 = go.Area(
  r = y,#["2015-12-01","2015-12-01 01:00:00","2015-12-01 02:00:00","2015-12-01 03:00:00","2015-12-01 04:00:00","2015-12-01 05:00:00"],
  t = x,#[74.73,76.59,76.5,79.03,77.89,81.9,],
    name='Vento m/s',
    marker=dict(
        color='rgb(158,154,200)'
    )

)



# Edit the layout
layout = go.Layout(
    title='Distribuição da Velocidade do Vento no diagrama Laurel',
    font = dict(size=16),
    radialaxis=dict(
        ticksuffix='m/s'
    ),
    orientation=270
)


data = [trace1]

fig = go.Figure(data=data, layout=layout)

# Tracando o objeto
py.plot(
  fig,
  filename='hans/oi_wrose',      # name of the file as saved in your plotly account
  sharing='public'
)                            # 'public' | 'private' | 'secret': Learn more: https://plot.ly/python/privacy


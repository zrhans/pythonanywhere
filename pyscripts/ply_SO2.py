"""
DATA,Chuva,Chuva_min,Chuva_max,VVE,VVE_min,VVE_max,DVE,DVE_min,DVE_max,
Temp.,Temp._min,Temp._max,Umidade,Umidade_min,Umidade_max,Rad.,Rad._min,Rad._max,
Pres.Atm.,Pres.Atm._min,Pres.Atm._max,
Temp.Int.,Temp.Int._min,Temp.Int._max,
CH4,CH4_min,CH4_max,HCnM,HCnM_min,HCnM_max,HCT,HCT_min,HCT_max,
SO2,SO2_min,SO2_max,
O3,O3_min,O3_max,
NO,NO_min,NO_max,NO2,NO2_min,NO2_max,NOx,NOx_min,NOx_max,
CO,CO_min,CO_max,
MP10,MP10_min,MP10_max,MPT,MPT_min,MPT_max,
Fin,Fin_min,Fin_max,Vin,Vin_min,Vin_max,Vout,Vout_min,Vout_max
"""
import plotly.plotly as py      # Every function in this module will communicate with an external plotly server
import plotly.graph_objs as go
import pandas as pd

DATAFILE = r'/home/zrhans/w3/bns/bns_2016-1.csv'

df = pd.read_csv(DATAFILE, parse_dates=True, sep=',', header=0, index_col='DATA')
r0 = df.SO2
t0 = df.DVE

#print(y)

# Definindo as series dedados
trace1 = go.Scatter(
    r=r0,#[6.804985785265978, 3.389596010612268, 5.3814721107464445, 8.059540219420184, 5.318229227868589, 2.9850999356273773, 1.9665870023752283, 6.769265408206589, 4.073401898721205, 6.50437182526841, 7.556369818996649, 4.047456094066775, 7.386662496070009, 5.413624736983931, 7.470716531163242, 7.982110216939738, 4.737814080093381, 4.206453042929911, 5.478604804594065, 4.824520280697772, 5.599600609899737, 6.8667952170824735, 3.0856713662561464, 7.771810943227382, 3.6877944350967193, 5.360356685192225, 5.140446739300986, 6.045445680928888, 6.833920940193708, 3.6207694625408364, 3.9894305834039687, 5.3118244995018, 4.608213480282062, 6.640584716151912, 3.055188854482986, 7.492564163752965, 5.4850781777896715, 3.8977949966209358, 5.976245114026165, 5.447061560910957, 5.37703411681004, 4.690805787731301, 4.711640491184845, 3.629919329394875, 5.957668076372498, 5.357121284391151, 3.849235282821748, 6.250507136319218, 7.122243357145468, 3.399404233835391, 3.5105566722713313, 4.100997603660974, 4.096382100199779, 6.233583074805102, 3.939488526772935, 3.9254450773976983, 6.118132501462698, 3.9404503462852323, 7.583015573261159, 3.513202145338516],
    t=t0,#[-30.352944361883697, -25.611459854524096, -12.425227452676078, 13.96138051872652, -4.9509328406707445, -25.692274190905437, 12.46876416157031, -4.913764107032951, -10.967380287631935, 30.814194054910676, 2.4749594311442737, 17.97554375239156, 0.7711305933623585, 6.137488485631386, -14.451963574013497, 28.184534112915948, 12.538680065954864, -8.983230337131154, 5.231285164762417, -64.48900253584051, 11.357486681772649, 3.4540747915125176, 13.924346613092862, -25.364002046782343, -16.81800638602268, -10.260051030559755, -13.212134125591882, 2.5793388653025744, 8.717574965852519, -10.675498719239487, -2.926366012522306, 25.195880754767717, 40.59032932155964, -9.121433630189772, -24.297362381339184, -3.1769445056889345, 10.85049841917252, -31.33205974736701, 4.849567462214266, 15.048276954124187, 3.2951046992599635, -6.197091873129837, -8.77857413578066, 29.549174119407287, -5.1374487928814645, 23.02686048794348, -6.634816578371129, 2.7550149918614695, 21.733250113653973, -24.816994960101756, -7.83054706253201, 28.325796210205855, 12.300977467795988, -21.563157240034112, -19.335516283813288, 26.146443170846787, -1.7060712026841085, 16.071723694996702, 2.053266302846965, -5.097911612332572],
    mode='markers',
    name='CH4',
    marker=dict(
        color='rgb(230,171,2)',
        size=110,
        line=dict(
            color='white'
        ),
        opacity=0.7
    )
)

layout = go.Layout(
    title='BSE01 - Dióxido de Enxôfre',
    font=dict(
        size=15
    ),
    plot_bgcolor='rgb(223, 223, 223)',
    angularaxis=dict(
        tickcolor='rgb(253,253,253)'
    ),
    orientation=270,
    radialaxis=dict(
        ticksuffix='ppm'
    ),
)

#Gerando multiplos diagramas ld
data = [trace1]
fig = go.Figure(data=data, layout=layout)
# Tracando o objeto
py.plot(
  fig,
  filename='hans/BSE01/2016/ld_SO2',      # name of the file as saved in your plotly account
  sharing='public'
)

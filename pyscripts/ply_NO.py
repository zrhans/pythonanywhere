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
r0 = df.NO
r1 = df.NO2
r2 = df.NOx
t0 = df.DVE

#print(y)

# Definindo as series dedados
trace1 = go.Scatter(
    r=r0,#[5.3724709243191295, 7.096355572040467, 4.883823903200083, 2.9201354412366496, 4.723963045684014, 7.423693950928521, 8.090946075397593, 3.3068445913715996, 6.050828482522597, 5.530232074438094, 2.47230695264053, 6.275670536862141, 2.6158961737877817, 4.653539944582694, 3.3354400138758, 4.795883604868761, 5.472711346482787, 5.881930490947868, 4.5715870720453795, 9.039861169796675, 4.6429075998956915, 3.1727677357988284, 7.044248138818528, 4.466336514107385, 6.557330289803022, 4.8208494372533615, 5.131915515212963, 3.9700122370488873, 3.4063238128284303, 6.476722963998372, 6.019218509330762, 5.664501534954291, 7.1587585225456705, 3.6007126616736462, 7.324127168758531, 2.552946156245396, 4.727133860387479, 6.971755207182515, 4.076578361066991, 4.946223407006624, 4.642155449043171, 5.3605748644110855, 5.391719067363011, 7.072524305096543, 4.101111570277392, 5.485732621016895, 6.192535286114146, 3.7687113918423396, 4.290311389760529, 7.060195369692179, 6.539691844176445, 6.679744406490943, 6.060825358695814, 4.786574040927106, 6.416686529666599, 6.70328133338789, 3.8888478104797555, 6.308591081194454, 2.4370447709043273, 6.508186347897975],
    t=t0,#[-140.20332764140605, -168.084245433406, -166.2851413292181, 138.24886675310003, -174.4243864364084, -169.96048275947723, 176.9918226866201, -169.90141624864253, -172.64158159443713, 142.9516688139347, 172.4157463673128, 168.5193591959272, 177.82205369393654, 172.85519034865231, -146.01452170111628, 128.1772930242011, 169.16707278067625, -173.58857378893256, 173.72699270456877, -151.20610477226074, 166.26047716274937, 172.50756608236046, 173.9491839042747, -131.80684093766672, -170.63527383147678, -168.57708548315375, -166.76550342128579, 176.07048734819648, 162.29750149829133, -174.05574631254976, -178.06092985664986, 156.47126885027095, 155.23914214477145, -163.00052639405448, -170.116713265192, -170.63927248749107, 167.38314369359566, -163.0988170562564, 172.8807370063752, 163.38600768186703, 176.1825419773446, -174.579680173718, -172.33584488196067, 165.33802569398378, -172.52566426066147, 157.54287773943665, -175.88151109326037, 175.42764399370765, 142.06967472256432, -168.3407340189972, -175.8058311226083, 163.06374541935153, 171.72097499708474, -151.40390456860604, -168.2713690903466, 165.04532787828478, -177.3153366647533, 170.04241289697416, 173.59919660957283, -177.25065674571294],
    mode='markers',
    name='NO',
    marker=dict(
        color='rgb(231,41,138)',
        size=110,
        line=dict(
            color='white'
        ),
        opacity=0.7
    )
)
trace2 = go.Scatter(
    r=r1,#[7.937557871379145, 7.302746491515634, 5.929302221442996, 2.407178713166243, 5.27092188705965, 7.400596127535688, 6.810820338360006, 4.967759034422344, 6.190229370454795, 2.158518657950606, 4.00412589386977, 4.776617321633007, 4.232250451808441, 4.30765487269422, 6.200275172864116, 0.7275138485344722, 4.378006803811767, 6.004964939443091, 4.341931702915758, 10.237982935327496, 3.8021588886978415, 3.96928117013756, 5.7589801424664335, 7.674179069144705, 6.699953533011802, 5.7343103881346, 6.044275915297742, 4.3129430660866035, 3.3775452824133043, 6.367666727269062, 5.737244181549697, 3.3963514719893415, 4.216467481387725, 5.464885016717265, 7.311135577533859, 4.745400769362272, 3.9164685318876504, 7.6029729903258385, 4.125204829441439, 3.6767949496501635, 4.551235788519779, 5.606960531523096, 5.794844257485189, 5.030528155694793, 5.109586240991219, 3.4054402079637396, 6.02630612538526, 4.2211092636354195, 1.9097829365788486, 7.254669393921678, 6.268875872033599, 4.56258056659493, 4.9180579654382806, 6.83656096252698, 6.78648654914422, 4.751014334485786, 4.719926347642004, 4.9278052151809675, 4.059190587394083, 6.128338984290388],
    t=t0,#[-101.83378577584543, -127.47839157875458, -112.2442849973417, -82.32591087119675, -114.6888556206928, -130.53786336160334, -145.0102649759552, -98.7488450072409, -124.44174882126121, -152.45411926998403, -89.29423655225057, -139.83245171792495, -91.54359518437012, -119.44216300369413, -92.45583852737828, -129.6599243163198, -131.0512350992248, -123.85291745359059, -118.08673900439605, -121.97921713765797, -121.91502996793754, -99.36184757774758, -141.46770199726927, -93.5662631891479, -126.33690140499776, -112.8349441777883, -114.38647992914663, -109.79607232724634, -102.74326471243563, -128.2467289067651, -127.79209264323043, -142.47362974536523, -161.58729418706835, -99.94061077957295, -130.16311732570668, -90.22881200957039, -122.65049121443685, -123.26775057177692, -111.99730880084306, -127.52831680551732, -117.93129533779559, -120.39163424547179, -119.38687147866949, -149.6746954924951, -107.85051750555007, -138.98993134073962, -127.5954702142739, -107.32083544041386, -117.5738074233824, -127.48166096847307, -129.91203316621693, -148.49521167061027, -135.33164137019145, -104.42165927641673, -123.87544021115426, -146.81682661802307, -107.0584854241401, -138.9025648732907, -88.89688251951031, -130.75446735589105],
    mode='markers',
    name='NO2',
    marker=dict(
        color='rgb(102,166,30)',
        size=110,
        line=dict(
            color='white'
        ),
        opacity=0.6
    )
)
trace3 = go.Scatter(
    r=r2,#[8.46918052789063, 5.821997567373959, 6.1409183282181425, 5.831724284786043, 5.546754471857236, 5.62748770920125, 3.94832897601986, 6.490184614609525, 5.320618245151644, 3.2435930414929843, 6.444085331576761, 3.363778100648707, 6.463116810505407, 4.730944925781221, 7.796578411114142, 4.570127829915901, 3.926206816002813, 5.254348139870139, 4.8384111066133375, 8.694523998982934, 4.39953181821818, 5.8564839051788535, 3.62157703921442, 8.894912373110186, 5.494542836078211, 5.968980890853802, 6.047899573604184, 5.384671396722035, 5.381220018196653, 5.11157462273727, 4.7705611050578, 3.0983308826347407, 1.665083171936659, 6.740258533332946, 5.5944949288820025, 6.879630825669177, 4.382792466280775, 6.410843616485085, 5.154204317772818, 4.01515851865648, 4.9391488682598155, 5.298297314485713, 5.490417176946796, 2.6237512593812404, 5.9535886616652665, 3.3014793719195046, 4.954889001100974, 5.500053669614178, 4.4505123495497285, 5.786624513349857, 4.906834424064605, 2.6299694734469274, 3.769703608047238, 7.396735715500286, 5.7644819019579545, 2.794585195883112, 5.782033269824353, 3.4853519176219963, 6.500653598620165, 4.748640710129176],
    t=t0,#[-66.53583632728323, -84.514422676922, -63.339741699567846, -24.146812744223833, -59.70124532256676, -88.06537267996578, -98.44420453532204, -49.15839681719936, -73.63622331202959, -17.923874678608904, -38.41239945460549, -66.34036237792131, -40.88883873919996, -52.46063321002169, -52.61046255912479, -7.039351050913894, -57.23545869215697, -71.64220350197985, -52.345396169095466, -92.78303867354904, -47.18716305503351, -41.969208462875166, -82.14422824993427, -59.43916560317718, -79.19482259319774, -62.29990853531319, -65.53790403937941, -48.9060554475786, -37.74831103800929, -78.05333345828834, -71.87311766307504, -41.891092825900685, -53.11545548549721, -52.997628097314845, -87.0843610179252, -43.61190483837573, -48.79799840560851, -82.56680315713163, -47.90996299570176, -46.57048558531105, -54.5004832176089, -65.90072712679752, -66.87331746360131, -75.48080725209734, -54.777693866880114, -42.5983345913628, -74.50816626907293, -47.11021844342552, -22.356873183328428, -84.19298674498425, -78.50528475620209, -65.0363717923471, -66.51373368133282, -63.52677656175937, -77.80907855131592, -68.51017974013602, -51.296869310885135, -68.33991302765452, -38.631733068443026, -77.85184858511114],
    mode='markers',
    name='NOx',
    marker=dict(
        color='rgb(230,171,2)',
        size=110,
        line=dict(
            color='white'
        ),
        opacity=0.5
    )
)



layout = go.Layout(
    title='BSE01 - Óxidos de Nitrogênio - Média horária',
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
data = [trace1,trace2,trace3]
fig = go.Figure(data=data, layout=layout)
# Tracando o objeto
py.plot(
  fig,
  filename='hans/BSE01/2016/ld_NO',      # name of the file as saved in your plotly account
  sharing='public'
)


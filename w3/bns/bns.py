#!/usr/bin/python3
#-*- coding:utf-8 -*-
"""
Created on Sat May 30 14:34:56 2015

@author: hans
"""

import os
import subprocess
import pandas as pd

import matplotlib
matplotlib.use('Agg')
#matplotlib.rcParams['font.family'] = 'sans-serif'
#matplotlib.rcParams['font.sans-serif'] = ['Tahoma']#,'Bitstream Vera Sans','Lucida Grande','Verdana']
#matplotlib.rcParams['lines.linewidth'] = 2
#matplotlib.rcParams['figure.max_num_figures'] = 30
import matplotlib.pyplot as plt

import time
import datetime


#print(matplotlib.__version__ )


#print(plt.style.available)
#matplotlib.style.use('ggplot')
matplotlib.style.use('ggplot')

#print(plt.__file__)

version =  datetime.datetime.now()
data = datetime.date.today()

ano = data.year
mes = data.month
dia = data.day
odatafile = "bns_%s-%s.csv" % (ano, mes)
osvdatafile = "bns_%s-%s-osvaldo.csv" % (ano, mes)
#DATAFILE = "bns01_%s-%s.csv" % (ano, mes) #Arquivo gerado no ecologger
DATAFILE = 'bns01.csv'
#df = pd.read_csv('ftp://fortran-zrhans.c9.io/csdapy/sr311-2014.csv')

#os.chdir(r'/home/zrhans/Web/py/bns')
os.chdir(r'/home/zrhans/w3/bns')
#os.system("wget -c micrometeorologia.org/incomming/bns01.csv")

#P2 var = commands.getoutput("wget -c micrometeorologia.org/incomming/"+DATAFILE)
#var = subprocess.check_output(["wget -c micrometeorologia.org/incomming/"+DATAFILE, shell=True])
cmdout = subprocess.call("wget -c micrometeorologia.org/incomming/bns01.csv", shell=True)
f  = open('bns.log','a')
f.write('\n UTC\n '+50*'-'+'\n %s | em %s\n' % (cmdout, version))
f.close()
"""
Lendo arquivos de entrada
"""
df = pd.read_csv(DATAFILE, parse_dates=True, sep=',', header=0, index_col='DATA')

print("\n Datafile Carregado...\n")
#print(df.head())

#print("\n Listando indices\n")
#print("df.index")
#print("\nOK\n")

"""
datafile = 'http://zrhans.koding.io/py/bns/bns01.csv'
df = pd.read_csv(datafile, sep=',', index_col='DATA',parse_dates=True, engine='python')

colunas = list(df.PA[:38].unique()) #padrao de saida eh array, entao tranformo para lista para iterar
for var in colunas:
    #Remove o ponto do nome das variaveis#
    cols.append(var.replace('.',''))

for var in colunas:
    #Gerando DataFrame para cada Parametro e Mudando o nome das colunas
         de acordo com o parametro
    #
    daf = "df_%s"%(var.replace('.',''))
    print "%s = df[df.PA == '%s']; %s.rename(columns={'MEDIA':'%s','QT_MEVAL_MIN':'%s_min','QT_MEVAL_MAX':'%s_max'}, inplace=True);" % (daf,var,daf,var,var,var)


"""
colunas = list(df.PA.unique()) #padrao de saida eh array, entao tranformo para lista para iterar
# Comandos para criar um dataframe para cada parametro como nome das colunas jah renomeadas

#print("\n Lista de Colunas...\n")
#print(colunas)

print("\n Criando DataFrames...\n")
df_Chuva = [[]]


df_Chuva = df[df.PA == 'Chuva']
cols = {'MEDIA':'Chuva','QT_MEVAL_MIN':'Chuva_min','QT_MEVAL_MAX':'Chuva_max'}

new_df = df_Chuva.rename(columns=cols);

df_Chuva = new_df.copy()
#df_Chuva.rename(columns={'QT_MEVAL_MAX':'C----'}, inplace=True)

df_VVE = df[df.PA == 'VVE']
df_VVE.rename(columns={'MEDIA':'VVE','QT_MEVAL_MIN':'VVE_min',r'QT_MEVAL_MAX':u'VVE_max'}, inplace=True);

df_DVE = df[df.PA == 'DVE']
df_DVE.rename(columns={'MEDIA':'DVE','QT_MEVAL_MIN':'DVE_min','QT_MEVAL_MAX':'DVE_max'}, inplace=True);

df_Temp = df[df.PA == 'Temp.']
df_Temp.rename(columns={'MEDIA':'Temp.','QT_MEVAL_MIN':'Temp._min','QT_MEVAL_MAX':'Temp._max'}, inplace=True)

df_Umidade = df[df.PA == 'Umidade']
df_Umidade.rename(columns={'MEDIA':'Umidade','QT_MEVAL_MIN':'Umidade_min','QT_MEVAL_MAX':'Umidade_max'}, inplace=True)

df_Rad = df[df.PA == 'Rad.'];
df_Rad.rename(columns={'MEDIA':'Rad.','QT_MEVAL_MIN':'Rad._min','QT_MEVAL_MAX':'Rad._max'}, inplace=True);

df_PresAtm = df[df.PA == 'Pres.Atm.'];
df_PresAtm.rename(columns={'MEDIA':'Pres.Atm.','QT_MEVAL_MIN':'Pres.Atm._min','QT_MEVAL_MAX':'Pres.Atm._max'}, inplace=True);

df_TempInt = df[df.PA == 'Temp.Int.'];
df_TempInt.rename(columns={'MEDIA':'Temp.Int.','QT_MEVAL_MIN':'Temp.Int._min','QT_MEVAL_MAX':'Temp.Int._max'}, inplace=True);

df_CH4 = df[df.PA == 'CH4']; df_CH4.rename(columns={'MEDIA':'CH4','QT_MEVAL_MIN':'CH4_min','QT_MEVAL_MAX':'CH4_max'}, inplace=True);

df_HCnM = df[df.PA == 'HCnM']; df_HCnM.rename(columns={'MEDIA':'HCnM','QT_MEVAL_MIN':'HCnM_min','QT_MEVAL_MAX':'HCnM_max'}, inplace=True);

df_HCT = df[df.PA == 'HCT']; df_HCT.rename(columns={'MEDIA':'HCT','QT_MEVAL_MIN':'HCT_min','QT_MEVAL_MAX':'HCT_max'}, inplace=True);

df_SO2 = df[df.PA == 'SO2']; df_SO2.rename(columns={'MEDIA':'SO2','QT_MEVAL_MIN':'SO2_min','QT_MEVAL_MAX':'SO2_max'}, inplace=True);

df_O3 = df[df.PA == 'O3']; df_O3.rename(columns={'MEDIA':'O3','QT_MEVAL_MIN':'O3_min','QT_MEVAL_MAX':'O3_max'}, inplace=True);

df_NO = df[df.PA == 'NO']; df_NO.rename(columns={'MEDIA':'NO','QT_MEVAL_MIN':'NO_min','QT_MEVAL_MAX':'NO_max'}, inplace=True);

df_NO2 = df[df.PA == 'NO2']; df_NO2.rename(columns={'MEDIA':'NO2','QT_MEVAL_MIN':'NO2_min','QT_MEVAL_MAX':'NO2_max'}, inplace=True);

df_NOx = df[df.PA == 'NOx']; df_NOx.rename(columns={'MEDIA':'NOx','QT_MEVAL_MIN':'NOx_min','QT_MEVAL_MAX':'NOx_max'}, inplace=True);

df_CO = df[df.PA == 'CO']; df_CO.rename(columns={'MEDIA':'CO','QT_MEVAL_MIN':'CO_min','QT_MEVAL_MAX':'CO_max'}, inplace=True);

df_MP10 = df[df.PA == 'MP10']; df_MP10.rename(columns={'MEDIA':'MP10','QT_MEVAL_MIN':'MP10_min','QT_MEVAL_MAX':'MP10_max'}, inplace=True);

df_MPT = df[df.PA == 'MPT']; df_MPT.rename(columns={'MEDIA':'MPT','QT_MEVAL_MIN':'MPT_min','QT_MEVAL_MAX':'MPT_max'}, inplace=True);

df_Fin = df[df.PA == 'Fin'];
df_Fin.rename(columns={'MEDIA':'Fin','QT_MEVAL_MIN':'Fin_min','QT_MEVAL_MAX':'Fin_max'}, inplace=True);

df_Vin = df[df.PA == 'Vin'];
df_Vin.rename(columns={'MEDIA':'Vin','QT_MEVAL_MIN':'Vin_min','QT_MEVAL_MAX':'Vin_max'}, inplace=True);

df_Vout = df[df.PA == 'Vout'];
df_Vout.rename(columns={'MEDIA':'Vout','QT_MEVAL_MIN':'Vout_min','QT_MEVAL_MAX':'Vout_max'}, inplace=True);


print("OK\n")
"""
for var in colunas:
    # Gera comandos de execucao de joins para criar a tabela final
    daf = "df_%s"%(var.replace('.',''))
    print "df = df.join(%s[['%s','%s_min','%s_max']])" % (daf,var,var,var)
"""
print("Limpando DataFrame...\n")
df = df[[]]
print( "Pronto!\n")
print( "\nExecutando join...")

""" Criando coluna do Dia do Ano par ao Prof. Osvaldo"""
#for i in df.index:
    #df['DJ'] = i.strftime('%j')
    #df['HHMM'] = i.strftime('%H')+i.strftime('%M')
    #print(i,i.strftime('%j'),i.strftime('%H')+i.strftime('%M'))


#print("\nconferindo Colunas de Data...")
#print(df.tail(5))

print( "\nExecutando joins...")
df = df.join(df_Chuva[['Chuva','Chuva_min','Chuva_max']])

#print( "\nExecutando join VVE...")
df = df.join(df_VVE[['VVE','VVE_min','VVE_max']])

#print( "\nExecutando join DVE...")
df = df.join(df_DVE[['DVE','DVE_min','DVE_max']])

#print( "\nExecutando join Temp...")
df = df.join(df_Temp[['Temp.','Temp._min','Temp._max']])

#print( "\nExecutando join Umidade...")
df = df.join(df_Umidade[['Umidade','Umidade_min','Umidade_max']])

#print( "\nExecutando join Rad...")
df = df.join(df_Rad[['Rad.','Rad._min','Rad._max']])

#print( "\nExecutando join Pres.Atm...")
df = df.join(df_PresAtm[['Pres.Atm.','Pres.Atm._min','Pres.Atm._max']])

#print( "\nExecutando join Temp.Int...")
df = df.join(df_TempInt[['Temp.Int.','Temp.Int._min','Temp.Int._max']])

#print( "\nExecutando join Gases...")
df = df.join(df_CH4[['CH4','CH4_min','CH4_max']])
df = df.join(df_HCnM[['HCnM','HCnM_min','HCnM_max']])
df = df.join(df_HCT[['HCT','HCT_min','HCT_max']])
df = df.join(df_SO2[['SO2','SO2_min','SO2_max']])
df = df.join(df_O3[['O3','O3_min','O3_max']])
df = df.join(df_NO[['NO','NO_min','NO_max']])
df = df.join(df_NO2[['NO2','NO2_min','NO2_max']])
df = df.join(df_NOx[['NOx','NOx_min','NOx_max']])
df = df.join(df_CO[['CO','CO_min','CO_max']])
df = df.join(df_MP10[['MP10','MP10_min','MP10_max']])
df = df.join(df_MPT[['MPT','MPT_min','MPT_max']])
df = df.join(df_Fin[['Fin','Fin_min','Fin_max']])
df = df.join(df_Vin[['Vin','Vin_min','Vin_max']])
df = df.join(df_Vout[['Vout','Vout_min','Vout_max']])
print( "OK\n")

#print(df.columns.tolist())
print( "\n Exportando DataFrame para .csv ...")
df.to_csv(odatafile, parse_dates=True)
dfo = df.copy()
#del(dfo['index'])
dfo.index = df.index.dayofyear + df.index.hour + df.index.minute
dfo.to_csv(osvdatafile,parse_dates=True)
print( "OK\n")

#print( "\n Exportando DataFrame para .xlsx ...")
#DataFrame.to_excel(excel_writer, sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, encoding=None, inf_rep='inf', verbose=True)¶

outputxlsx = "bns_%s-%s.xlsx" % (ano, mes)
Sheet1 = "bns_%s-%s" % (ano, mes)

##Demora  df.to_excel(outputxlsx, sheet_name=Sheet1, header=True)
#print( "OK\n")


#df.rename(columns={'MEDIA':'%s','QT_MEVAL_MIN':'%s_min','QT_MEVAL_MAX':'%s_max'}, inplace=True);" % (daf,

#pandas.read_excel(io, sheetname=0, header=0, skiprows=None, skip_footer=0,
#index_col=None, parse_cols=None, parse_dates=False, date_parser=None,
# na_values=None, thousands=None, convert_float=True, has_index_names=None,
# converters=None, engine=None, **kwds)
#print(df.head())


def graficos(prefix,var,namevar,varunit):
    ## Grafico do DataFrame Inteiro
    #plt.plot(df[['Valor.20','Valor.21']])

    if var == 'Chuva':

        rainD = df['Chuva'].resample('1D', how='sum')
        rainD['ACUM'] = df[['Chuva']].cumsum()
        #print(rainD)
        df[[var]].plot(title=namevar)
        #rainD['ACUM'].plot(title='Acumulado')

        #plt.bar(df.index, df['Chuva'], align='center', width=0.04, alpha=0.5 )
        plt.ylabel('mm')

        namefig = "graf/%s_%s.png" % (prefix,var)
        plt.savefig(namefig)

    else:
        #print("Gerando grafico: %s | %s | %s | %s" %(prefix,var,namevar,varunit))
        plt.figure(figsize=(18,12))

        namevar = "BNS01 - %s" % (namevar)

        df[[var]].plot(title=namevar)

        plt.ylabel(varunit)

        namefig = "graf/%s_%s.png" % (prefix,var)
        plt.savefig(namefig)

    return

#@todo Criar dicionario com o Parametro sendo a chave


param = {'MPT':('Analisador de Partículas Totais','MPT','mg/m³'), 'MP10':('Analisador de Particulas Inalaveis','MP10','mg/m³'),'CO':('Analisador de Monóxido de Carbono','CO','ppm'), 'NO':('Analisador de Óxidos de Nitrogênio','NO','ppm'),'NO2':('Analisador de Óxidos de Nitrogênio','NO2','ppm'),'NOx':('Analisador de Óxidos de Nitrogênio','NOx','ppm'),'O3':('Analisador de Ozônio','O3','ppm'),'SO2':('Analisador de Dióxido de Enxofre','SO2','ppm'),'CH4':('Analisador de Hidrocarbonetos','CH4','ppm'),'HCT':('Analisador de Hidrocarbonetos','HCT','ppm'),'HCnM':('Analisador de Hidrocarbonetos','HCnM','ppm'),'DVE':('Direção do Vento','DVE','Graus'), 'Pres.Atm.':('Pressão Atmosférica','Pres.Atm.','mbar'),'Rad.':('Radiação Solar','Rad.','W/m²'),'Temp.':('Temperatura do Ar','Temp.','°C'), 'Temp.Int.':('Temperatura Interna Estação','Temp.Int.','°C'),'Umidade':('Umidade Relativa','Umidade','%'),'VVE':('Velocidade do Vento','VVE','m/s'), 'Chuva':("Precipitação Pluviométrica",'Chuva','mm'),'Fin':('Suprimento de Energia','Fin','Hz'),'Vin':('Suprimento de Energia','Vin','V'),'Vout':('Suprimento de Energia ','Vout','V')}

for i, c in enumerate (colunas):
    # c e param[c][1] representam a mesma cisa (sigla da variável) [var]
    graficos(Sheet1,param[c][1],param[c][0],param[c][2])
    #print("graficos(Sheet1,'%s','%s'" % (i,param[i]))
    #print("item:%s -> %s \t Desc: %s" %(i,c,param[c][0]))
"""
         ,{'CO':'Analisador de Monóxido de Carbono - CO'}
         ,{'NO':'Analisador de Óxidos de Nitrogênio - NO'}
         ,{'NO2':'Analisador de Óxidos de Nitrogênio - NO2'}
         ,{'NOx':'Analisador de Óxidos de Nitrogênio - NOx'}
         ,{'O3':'Analisador de Ozônio - O3'}
         ,{'SO2':'Analisador de Dióxido de Enxofre - SO2'}
         ,{'CH4':'Analisador de Hidrocarbonetos - CH4'}
         ,{'HCT':'Analisador de Hidrocarbonetos - HCT'}
         ,{'HCnM':'Analisador de Hidrocarbonetos - HCnM'}
         ,{'DVE':'Entradas Analógicas - DVE'}
         ,{'Pres.Atm.':'Entradas Analógicas - Pres.Atm.'}
         ,{'Rad.':'Entradas Analógicas - Rad.'}
         ,{'Temp.':'Entradas Analógicas - Temp.'}
         ,{'Temp.Int.':'Entradas Analógicas - Temp.Int.'}
         ,{'Umidade':'Entradas Analógicas - Umidade'}
         ,{'VVE':'Entradas Analógicas - VVE'}
         ,{'Chuva':'Entradas Digitais - Chuva'}
         ,{'Fin':'Suprimento de Energia - Fin'}
         ,{'Vin':'Suprimento de Energia - Vin'}
         ,{'Vout':'Suprimento de Energia - Vout'}}
"""

version =  datetime.date.today().strftime("%Y-%m")
version = data
os.chdir(r'/home/zrhans/w3/bns/graf/')
cwd = os.getcwd()

def gera_html():
    versao = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    last_line = subprocess.getoutput('tail -1 /home/zrhans/w3/bns/bns01.csv | cut -d"," -f1')

    vnpath = 'http://www.qualidadedoar.com/static/images/graf/'
    HTML = ('index.html')
    owl = ('owl.html')
    thb = ('thb.html')
    title = "Graficos - BNS01 - UTERG" # Alterar para o titulo do site

    ficheiro = open(HTML,"w")
    ficheiro.write("<html><head><title>"+title+"</title></head><body>")
    ficheiro.write("<h1>%s </h1><i class='fi-loop'> </i><small> Versão atualizada em - <i>%s</i> UTC" % (title,versao))
    ficheiro.write("<br><i class='fi-rss'> </i>Ultimo envio do dados - <i> %s </i> LTC</small><hr> <center>" % last_line)

    fowl = open(owl,"w")
    fthb = open(thb,"w")

    for arquivo in os.listdir(cwd):
       if arquivo.endswith('.png'):
          #print('<a href="%s"><img src="%s"/></a><br/>' % (arquivo,arquivo))
          ficheiro.write('<img src="%s%s"/><hr>' % (vnpath, arquivo))
          fowl.write('<div class="item"><img src="http://www.qualidadedoar.com/static/images/graf/%s" /></div>' % arquivo)
          fthb.write('<div class="column"><a data-toggle="%s"><img class="thumbnail s550" src="http://www.qualidadedoar.com/static/images/graf/%s"></a>' % (arquivo[:-5],arquivo))


          fthb.write('<div class="full reveal" id="%s" data-reveal><p>%s</p><img src="http://www.qualidadedoar.com/static/images/graf/%s" alt="%s">  <button class="close-button" data-close aria-label="Close reveal" type="button"><span aria-hidden="true">&times;</span></button></div></div>' % (arquivo[:-5],arquivo,arquivo,arquivo))



    ficheiro.write("</center></body></html>")
    ficheiro.close()
    fowl.close()
    fthb.close()


gera_html()

cmdout = subprocess.call("mv index.html /home/zrhans/csda/templates/bns_graficos.html", shell=True)
cmdout = subprocess.call("mv owl.html /home/zrhans/csda/templates/bns_owl.html", shell=True)
cmdout = subprocess.call("mv thb.html /home/zrhans/csda/templates/thb_uterg.html", shell=True)
cmdout = subprocess.call("mv *.png /home/zrhans/csda/static/images/graf/", shell=True)

  #graficos(Sheet1,'MPT','Material Particulado Total')

print(10*'=' + ' Completo \n')
from flask import Flask, render_template, request, redirect
import sqlite3
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
from decimal import Decimal
 

app = Flask(__name__)
db_path = 'BD/BaseDatos2.db'
mapa = dash.Dash(__name__,server=app,routes_pathname_prefix='/mapa/')
df = pd.read_excel('BaseDeDatosValleDeAburra100%realNoFake.xls')
cnx = sqlite3.connect(db_path)
database = pd.read_sql_query("SELECT * FROM covidpositivo", cnx)
data = pd.concat([database,df],axis=0)
vectorLat = data['latitud']
vectorLon = data['longitud']
cnx.commit()
cnx.close()

 

@app.route('/usuario', methods=["POST", "GET"])
def home():
   if request.method=="POST":
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellidos")
        correo = request.form.get("correo")
        edad = request.form.get("edad")
        sexo = request.form.get("sexo")
        corona = request.form.get("corona")
        latitud = request.form.get("latitud")
        longitud = request.form.get("longitud")
        if corona == "SI":
            con = sqlite3.connect(db_path)
            cur = con.cursor()
            cur.execute("INSERT INTO covidpositivo VALUES(" +latitud + "," + longitud+ ")")
            con.commit()
            con.close()
        return redirect('/mapa')

 

@app.route('/mapa')
def graficar():
    df = pd.read_excel('BaseDeDatosValleDeAburra100%realNoFake.xls')
    cnx = sqlite3.connect(db_path)
    database = pd.read_sql_query("SELECT * FROM covidpositivo", cnx)
    cnx.commit()
    cnx.close()
    data = pd.concat([database,df],axis=0)
    vectorLat = data['latitud']
    vectorLon = data['longitud']
    mapa.layout = html.Div([
            html.H1('Covid 19 en el valle de Aburra'),
        html.Button('Analizar Zonas', id='submit-val', n_clicks=0),
        html.H1(id='test'),
            html.Div(id='text-content'),
           dcc.Graph(id='map', figure={
                'data': [{
                'lat': vectorLat,
                        'lon': vectorLon,
                'marker': {
                            'color': 'blue',
                            'size': 20,
                            'opacity': 0.6
                        },
                        'customdata': 2,
                        'type': 'scattermapbox'
                   }],
                'layout': {
                        'mapbox': {
                            'accesstoken': 'pk.eyJ1IjoibGVvbmFyZG9iZXRhbmN1ciIsImEiOiJjazlybGNiZWcwYjZ6M2dwNGY4MmY2eGpwIn0.EJjpR4klZpOHSfdm7Tsfkw',
                    'center' :{
                        'lat' : 6.242095,
                        'lon' : -75.589626
                    },
                    'zoom' : 10,
                    'style' : 'dark'
                        },
                        'hovermode': 'closest',
                        'margin': {'l': 0, 'r': 0, 'b': 0, 't': 0}
                }
            })
    ])
@mapa.callback(
    dash.dependencies.Output('map', 'figure'),
    [dash.dependencies.Input('submit-val', 'n_clicks')])
def actualizar(clicks):
    df = pd.read_excel('BaseDeDatosValleDeAburra100%realNoFake.xls')
    cnx = sqlite3.connect(db_path)
    database = pd.read_sql_query("SELECT * FROM covidpositivo", cnx)
    cnx.commit()
    cnx.close()
    data = pd.concat([database,df],axis=0)
    vectorLat = data['latitud']
    vectorLon = data['longitud']
    nororiental=0
    noroccidental=0
    suroriental=0
    suroccidental=0
    color = []
    for x in range(0,len(df['latitud'])):
        if (Decimal(df['longitud'][x])>Decimal(-75.565780) and Decimal(df['latitud'][x])>Decimal(6.269979)):
            nororiental = nororiental + 1
        elif df['longitud'][x]>(-75.633870) and df['longitud'][x]<(-75.565780) and df['latitud'][x]>(6.269979) and df['latitud'][x]<(6.347253):
            noroccidental = noroccidental + 1
        elif df['longitud'][x]>(-75.565780) and df['longitud'][x]<(-75.495771) and df['latitud'][x]>(6.139561) and df['latitud'][x]<(6.269979):
            suroriental = suroriental + 1
        elif df['longitud'][x]>(-75.633870) and df['longitud'][x]<(-75.565780) and df['latitud'][x]>(6.139561) and df['latitud'][x]<(6.269979):
            suroccidental = suroccidental + 1
    for x in range(0,len(database['latitud'])):
        if (Decimal(database['longitud'][x])>Decimal(-75.565780) and Decimal(database['latitud'][x])>Decimal(6.269979)):
            nororiental = nororiental + 1
        elif database['longitud'][x]>-75.633870 and database['longitud'][x]<-75.565780 and database['latitud'][x]>6.269979 and database['latitud'][x]<6.347253:
            noroccidental = noroccidental + 1
        elif database['longitud'][x]>-75.565780 and database['longitud'][x]<-75.495771 and database['latitud'][x]>6.139561 and database['latitud'][x]<6.269979:
            suroriental = suroriental + 1
        elif database['longitud'][x]>-75.633870 and database['longitud'][x]<-75.565780 and database['latitud'][x]>6.139561 and database['latitud'][x]<6.269979:
            suroccidental = suroccidental + 1
        #print(nororiental,"-",noroccidental,"-",suroriental,"-",suroccidental)
    figure={
                'data': [{
                'lat': vectorLat,
                        'lon': vectorLon,
                'marker': {
                            'color': 'green',
                            'size': 20,
                            'opacity': 0.6
                        },
                        'customdata': 2,
                        'type': 'scattermapbox'
                }],
                'layout': {
                        'mapbox': {
                            'accesstoken': 'pk.eyJ1IjoibGVvbmFyZG9iZXRhbmN1ciIsImEiOiJjazlybGNiZWcwYjZ6M2dwNGY4MmY2eGpwIn0.EJjpR4klZpOHSfdm7Tsfkw',
                    'center' :{
                        'lat' : 6.242095,
                        'lon' : -75.589626
                    },
                    'zoom' : 10,
                    'style' : 'dark'
                        },
                        'hovermode': 'closest',
                        'margin': {'l': 0, 'r': 0, 'b': 0, 't': 0}
                }
            }
    return figure
@mapa.callback(
    dash.dependencies.Output('test', 'children'),
    [dash.dependencies.Input('submit-val', 'n_clicks')])
def sendata(clicks):
    df = pd.read_excel('BaseDeDatosValleDeAburra100%realNoFake.xls')
    cnx = sqlite3.connect(db_path)
    database = pd.read_sql_query("SELECT * FROM covidpositivo", cnx)
    cnx.commit()
    cnx.close()
    nororiental=0
    noroccidental=0
    suroriental=0
    suroccidental=0
    color = []
    for x in range(0,len(df['latitud'])):
        if (Decimal(df['longitud'][x])>Decimal(-75.565780) and Decimal(df['latitud'][x])>Decimal(6.269979)):
            nororiental = nororiental + 1
        elif df['longitud'][x]<(-75.565780) and df['latitud'][x]>(6.269979):
            noroccidental = noroccidental + 1
        elif df['longitud'][x]>(-75.565780) and df['latitud'][x]<(6.269979):
            suroriental = suroriental + 1
        elif df['longitud'][x]<(-75.565780) and df['latitud'][x]<(6.269979):
            suroccidental = suroccidental + 1
    for x in range(0,len(database['latitud'])):
        if (Decimal(database['longitud'][x])>Decimal(-75.565780) and Decimal(database['latitud'][x])>Decimal(6.269979)):
            nororiental = nororiental + 1
        elif database['longitud'][x]<-75.565780 and database['latitud'][x]>6.269979:
            noroccidental = noroccidental + 1
        elif database['longitud'][x]>-75.565780 and database['latitud'][x]<6.269979:
            suroriental = suroriental + 1
        elif database['longitud'][x]<-75.565780 and database['latitud'][x]<6.269979:
            suroccidental = suroccidental + 1
    return "Zona nororiental: ",nororiental," ||Zona noroccidental: ",noroccidental," ||Zona suroriental: ",suroriental," ||Zona suroccidental: ",suroccidental
@app.route('/', methods =["GET"])
def logueo():
    """con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS data")
    cur.execute("CREATE TABLE covidpositivo (latitud DOUBLE, longitud DOUBLE)")
    con.commit()
    con.close()"""
    data = pd.concat([database,df],axis=0)
    vectorLat = data['latitud']
    vectorLon = data['longitud']
    return render_template("index.html")

 

if __name__ == '__main__':
    graficar()
    mapa.run_server(debug = True, host = '0.0.0.0', port = 80)
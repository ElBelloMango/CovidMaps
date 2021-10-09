from flask import Flask, render_template, request, redirect
import sqlite3
import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import numpy as np
from decimal import Decimal
import json

app = Flask(__name__)
db_path = 'ProyectoFinalTele/BD/CovidMaps.db'
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We',
        'crossorigin': 'anonymous'
    },
    {
        'href': 'templates/css/style.css',
        'rel': 'stylesheet'
    }
]
mapa = dash.Dash(__name__, server=app, routes_pathname_prefix='/mapa/',
                 external_stylesheets=external_stylesheets, title="CovidMaps")
cnx = sqlite3.connect(db_path)
database = pd.read_sql_query("SELECT * FROM contagiados", cnx)
cnx.commit()
cnx.close()


@app.route('/usuario', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellidos")
        sexo = request.form.get("sexo")
        edad = request.form.get("edad")
        correo = request.form.get("email")
        localidad = request.form.get("localidad")
        corona = request.form.get("corona")
        if corona == "SI":
            con = sqlite3.connect(db_path)
            cur = con.cursor()
            cur.execute("INSERT INTO contagiados(nombre,apellidos,sexo,edad,email,id_localidad) VALUES('{}','{}','{}','{}','{}','{}')".format(
                nombre, apellido, sexo, edad, correo, localidad))
            con.commit()
            con.close()
        return redirect('/mapa')


@app.route('/mapa')
def graficar():
    cnx = sqlite3.connect(db_path)
    database = pd.read_sql_query("SELECT * FROM contagiados", cnx)
    cnx.commit()
    cnx.close()
    mapa.layout = html.Div([
        html.H1('Covid 19 en el valle de Aburra'),
        html.Button('Actualizar datos', id='submit-val',
                    className="btn btn-outline-primary btn-lg btn-block", n_clicks=0),
        html.Button('Zoom', id='zoom',
                    className="btn btn-outline-warning btn-lg btn-block", n_clicks=0),
        html.Td(),
        html.Div(id='text-content'),
        dcc.Graph(id='map'),
    ], className="container")


@mapa.callback(
    dash.dependencies.Output('map', 'figure'),
    [dash.dependencies.Input('submit-val', 'n_clicks')])
def actualizar(n_clicks):
    cnx = sqlite3.connect(db_path)
    database = pd.read_sql_query("SELECT * FROM contagiados", cnx)
    cnx.commit()
    cnx.close()
    # figure = go.Scattermapbox(data=None,layout = None) Util para luego, clase plotly con dash
    # fig = go.Figure(go.Scatter(x=[0, 1, 2, 0], y=[0, 2, 0, 0], fill="toself"))
    # fig.show()

    #Lectura JSON y #Vectores
    coord = []
    long = []
    lat = []
    regiones = []
    contagiados=[]
    with open('ProyectoFinalTele/BD/localidades.json', encoding="utf8") as file:
        dataJSON = json.load(file)
        for i in range(331):
            coord.append(dataJSON['features'][i]['geometry']['rings'])
            long.append(dataJSON['features'][i]['geometry']['rings'][0][0][0])
            lat.append(dataJSON['features'][i]['geometry']['rings'][0][0][1])
            regiones.append(dataJSON['features'][i]['attributes']['NOMBRE'])

        # print(dataJSON['features'][0]['geometry']['rings'][0][0][0])

    figure = {
        'data': [{
            'lon': long,
            'lat': lat, # Datos de posiciones
            'marker': {
                'color': 'rgba(8, 0, 255,0.5)',
                'size': 20,
                'opacity': 0.6
            },
            'customdata': 2,
            'type': 'scattermapbox',
            'hovertext':regiones
        }],
        'layout': {
            'mapbox': {
                'style': "stamen-terrain",
                'center': {'lon': -75.579114, 'lat': 6.251166},
                'zoom': 12, 'layers': [{
                    'source': {
                        'type': "FeatureCollection",
                        'features': [{
                            'type': "Feature",
                            'geometry': {
                                'type': "MultiPolygon",
                                'coordinates': coord
                            }
                        }]
                    },
                    'type': "fill", 'below': "traces", 'color': "rgba(255,255,255,0.5)"}]},
            'showlegend': 'true',
            'margin': {'l': 0, 'r': 0, 'b': 0, 't': 0}
            
        }
    }
    return figure


# @mapa.callback(
#     dash.dependencies.Output('test', 'children'),
#     [dash.dependencies.Input('submit-val', 'n_clicks')])

# def sendata(clicks):
#     return "Zona nororiental: ", nororiental, " ||Zona noroccidental: ", noroccidental, " ||Zona suroriental: ", suroriental, " ||Zona suroccidental: ", suroccidental


@app.route('/', methods=["GET"])
def logueo():
    cnx = sqlite3.connect('ProyectoFinalTele/BD/CovidMaps.db')
    localidades = pd.read_sql_query("SELECT * FROM localidades", cnx)
    cnx.commit()
    cnx.close()
    localidades = localidades.to_dict(orient='records')
    return render_template("Rework.html", localidades=localidades)


if __name__ == '__main__':
    graficar()
    mapa.run_server(debug=True, host='0.0.0.0', port=80)

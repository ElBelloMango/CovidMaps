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
    with open('ProyectoFinalTele/BD/localidades.json', encoding="utf8") as file:
        dataJSON = json.load(file)
        print(dataJSON['features'][0]['geometry']['rings'][0])

    figure = {
        'data': [{
            'lon': [-73.606352888],
            'lat': [45.507489991], # Datos de posiciones
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
                'style': "stamen-terrain",
                'center': {'lon': -73.6, 'lat': 45.5},
                'zoom': 12, 'layers': [{
                    'source': {
                        'type': "FeatureCollection",
                        'features': [{
                            'type': "Feature",
                            'geometry': {
                                'type': "MultiPolygon",
                                'coordinates': [[[
                                    [-73.606352888,
                                        45.507489991], [-73.606133883, 45.50687600],
                                    [-73.605905904, 45.506773980], [-73.603533905,
                                                                    45.505698946],
                                    [-73.602475870, 45.506856969], [-73.600031904,
                                                                    45.505696003],
                                    [-73.599379992, 45.505389066], [-73.599119902,
                                                                    45.505632008],
                                    [-73.598896977, 45.505514039], [-73.598783894,
                                                                    45.505617001],
                                    [-73.591308727, 45.516246185], [-73.591380782,
                                                                    45.516280145],
                                    [-73.596778656, 45.518690062], [-73.602796770,
                                                                    45.521348046],
                                    [-73.612239983, 45.525564037], [-73.612422919,
                                                                    45.525642061],
                                    [-73.617229085, 45.527751983], [-73.617279234,
                                                                    45.527774160],
                                    [-73.617304713, 45.527741334], [-73.617492052,
                                                                    45.527498362],
                                    [-73.617533258, 45.527512253], [-73.618074188,
                                                                    45.526759105],
                                    [-73.618271651, 45.526500673], [-73.618446320,
                                                                    45.526287943],
                                    [-73.618968507, 45.525698560], [-73.619388002,
                                                                    45.525216750],
                                    [-73.619532966, 45.525064183], [-73.619686662,
                                                                    45.524889290],
                                    [-73.619787038, 45.524770086], [-73.619925742,
                                                                    45.524584939],
                                    [-73.619954486, 45.524557690], [-73.620122362,
                                                                    45.524377961],
                                    [-73.620201713,
                                        45.524298907], [-73.620775593, 45.523650879]
                                ]]]
                            }
                        }]
                    },
                    'type': "fill", 'below': "traces", 'color': "royalblue"}]},
            'showlegend': 'true',
            'margin': {'l': 0, 'r': 0, 'b': 0, 't': 0},
            'hoverinfo':'Hola'
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

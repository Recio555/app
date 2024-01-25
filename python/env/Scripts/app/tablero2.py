import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Diseño del dashboard
app.layout = html.Div(
    children=[
        html.H1(children='Mi Dashboard'),
        dcc.Graph(
            id='mi-grafico',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Grupo 1'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Grupo 2'},
                ],
                'layout': {
                    'title': 'Gráfico de Barras'
                }
            }
        ),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
import dash
#import dash_core_components as dcc
#import dash_html_components as html
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos de ejemplo (reemplázalo con tus propios datos)
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
df = pd.read_csv(url)

# Configurar el estilo de seaborn para mejorar la apariencia de los gráficos
sns.set()

# Crear gráfico de dispersión
def scatter_plot(x_column, y_column):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x_column, y=y_column, hue='species', palette='viridis')
    plt.title(f'{x_column} vs {y_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.legend(title='Species')
    plt.tight_layout()
    return plt

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Diseño del dashboard
app.layout = html.Div(
    children=[
        html.H1(children='Análisis de Datos con Pandas y Dash'),

        dcc.Dropdown(
            id='x-column',
            options=[{'label': col, 'value': col} for col in df.columns],
            value='sepal_length',
            multi=False,
            style={'width': '50%'}
        ),

        dcc.Dropdown(
            id='y-column',
            options=[{'label': col, 'value': col} for col in df.columns],
            value='sepal_width',
            multi=False,
            style={'width': '50%'}
        ),

        dcc.Graph(
            id='scatter-plot'
        ),
    ]
)

# Definir la interactividad
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('x-column', 'value'),
     Input('y-column', 'value')]
)
def update_scatter_plot(x_column, y_column):
    plt = scatter_plot(x_column, y_column)
    return plt

if __name__ == '__main__':
    app.run_server(debug=True)
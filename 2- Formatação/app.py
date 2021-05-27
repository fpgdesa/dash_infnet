# -*- coding: utf-8 -*-


"""
2 - App "Formatação"
"""


import dash
import dash_html_components as html


app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1('Estamos no Rio de Janeiro',
    style={'color': 'blue', 
           'fontSize': '40px'}),
           
    html.H1('Cidade Maravilha'),
    
    html.P('E...'),
    
    html.Ul([
    	html.Li('Purgatório'),
    	html.Li('da Beleza'),
    	html.Li('e do Caos...')    
    ]),
           
])


if __name__ == '__main__':
	app.run_server(debug=True)
	
	
	

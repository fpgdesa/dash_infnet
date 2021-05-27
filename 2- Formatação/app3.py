# -*- coding: utf-8 -*-


"""
2 - App "Formatação"
"""


import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div([

dbc.Row([dbc.Col( width=2, children=[
        	html.H1('Estamos no Rio de Janeiro',
		style={'color': 'blue', 
               'fontSize': '40px'}),	
		]),    
	
	 dbc.Col(width=5,children = [
	     html.H1('Cidade Maravilha')
	     ]),    
	     
	     
	     dbc.Col(width=4,children = [
	     	html.Ul([
		    	html.Li('Purgatório'),
		    	html.Li('da Beleza'),
		    	html.Li('e do Caos...')    
		    ])]
	     )]),
 


dbc.Tabs([
dbc.Tab([
	html.P('Uma Foto Bonita'),
	html.A(
               html.Img(
                        src=app.get_asset_url("riodejaneiro1.jpg"),
                        style={'float': 'center', 'height': '300px', 'margin-top': '10px'}
                       ),
               href="https://www.rio.com.br/"
              )                
       ], label = 'Foto 1'),
dbc.Tab([
	html.P('Outra Foto Bonita'),
	html.A(
               html.Img(
                        src=app.get_asset_url("riodejaneiro2.jpg"),
                        style={'float': 'center', 'height': '300px', 'margin-top': '10px'}
                       ),
               href="https://www.rio.com.br/"
              )                
       ], label = 'Foto 2')
])


])


if __name__ == '__main__':
	app.run_server(debug=True)
	
	
	

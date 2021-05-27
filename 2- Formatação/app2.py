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
	     )])
])




if __name__ == '__main__':
	app.run_server(debug=True)
	
	
	

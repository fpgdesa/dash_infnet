# -*- coding: utf-8 -*-


"""
2 - App "Formatação"
"""


import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash_core_components as dcc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])



infnet_image = 'https://www.infnet.edu.br/infnet/wp-content/uploads/sites/6/2018/01/logotipo.png'

button_group = dbc.ButtonGroup(
    [
        dbc.Button("Opção 1",style= {'color':'black'}),
        dbc.Button("Opção 2"),
        dbc.DropdownMenu(
            [dbc.DropdownMenuItem("Item 1"), dbc.DropdownMenuItem("Item 2")],
            label="Dropdown",
            group=True,
        ),
    ],
    className="ml-auto flex-nowrap mt-3 mt-md-0",  

)




navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=infnet_image, height="30px"))
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://plot.ly",
        ),   
     dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(button_group, id="navbar-collapse", navbar=True),],
       color="dark",
    dark=True,
)


def build_card(title, value, id_card):
    card = [
        dbc.CardHeader(title, className = "card-title-text"),
        dbc.CardBody(
            [
                html.H6(value, className="card-title", id = id_card ),
                
            ]
        ),]
    
    return card


card = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(build_card("Cidade", {}, "card_cidade"), color="#c38e0b", inverse= True)),                 
            ],
            className="mb-5",
        ),
        
    ]
)





app.layout = html.Div([

	navbar,
	
	html.Div(className="row", children=[
        html.Div(className="col-sm",children=[

        
            html.Label('Cidade'),
            dcc.Dropdown(id='menu_cidade',
                         placeholder='Selecione uma Cidade',
                         options=[{'label':'Rio de Janeiro', 'value':'Rio de Janeiro'}, 
                         	   {'label':'Niterói', 'value':'Niterói'}, 
                         	   {'label':'Nova Iguaçu', 'value':'Nova Iguaçu'}],
                         value= '',
                         multi=False,
                         searchable = False),
          
        ]),]),
        
   
      dbc.Col(width=4,children = [
	     	card
	     	],style={'margin-top': '10px'})
])


@app.callback(
Output('card_cidade', 'children'),
Input('menu_cidade','value'),
)

def title_card(name):
	return name



if __name__ == '__main__':
	app.run_server(debug=True)
	
	
	

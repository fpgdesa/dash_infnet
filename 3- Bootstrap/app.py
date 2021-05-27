# -*- coding: utf-8 -*-


"""
2 - App "Formatação"
"""


import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

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


card = dbc.Card(
    [
        dbc.CardImg(src="assets/riodejaneiro1.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Rio de Janeiro", className="card-title"),
                html.P(
                    "Um simples exemplo "
                    "do uso de cartões.",
                    className="card-text",
                ),
                dbc.Button("Ir", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
)



app.layout = html.Div([

	navbar,
	card





])


if __name__ == '__main__':
	app.run_server(debug=True)
	
	
	

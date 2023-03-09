# Inicia bloque de No editar
import dash
from dash.dependencies import Output, Input, State
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)
server = app.server

cantina_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("La Cantina", className="card-title"),
            html.P("Control de Pedidos"),
            html.P("Balance"),
            html.Div(0, id='balance'),
        ]
    )
)

clientes_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Visitas de Clientes", className="card-title"),
            dbc.Button("Juan hace pedido", color="primary", id='juan_boton', n_clicks=0, style={"margin-left": "15px"}),
            dbc.Button("Carlos hace pedido", color="primary", id='carlos_boton', n_clicks=0, style={"margin-left": "15px"}),
            dbc.Button("Andres hace pedido", color="primary", id='andres_boton', n_clicks=0, style={"margin-left": "15px"}),
            html.Div(id='contenedor_juan'),
            html.Div(id='contenedor_carlos'),
            html.Div(id='contenedor_andres'),
            html.Div(id='clientes'),
        ]
    )
)


pedidos_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Pedidos", className="card-title"),
            dbc.Button("Procesar pedido", color="primary", id='procesar_pedido', n_clicks=0, style={"margin-left": "15px"}),
            html.Div(id='pedidos')
        ]
    )
)


cards = dbc.Row([dbc.Col(clientes_card, width=4),
                 dbc.Col(pedidos_card, width=8)])

app.layout = html.Div([
    cantina_card,
    cards])


def formato_listas(collecion):
    return '\n'.join([str(elemento) for elemento in collecion])

# Finaliza bloque de No editar

# Escriba su codigo aqui

# Defina (Escriba el codigo) aqui el decorador con nombre 'tomar_tiempo'
# que capture la fecha y hora actual del sistema.

# Justo al final de la ejecucion de la funcion por decorar y escriba la fecha y hora
# en un archivo de texto llamado 'reporte.txt'. Hint: puede usar la biblioteca 'datetime' para leer la fecha y hora
# El archivo de texto debe acumular dicha informacion cada vez que la funcion por decorar se ejecute.

# Las funciones por decorar son los metodos 'ordenar_bebida' y 'ordernar_comida' para las clases
# ClienteJuan, ClienteCarlos y ClienteAndres que se describen a continuacion:

class ClienteJuan:      # No editar
    def __str__(self):  # No editar
        return 'Juan'   # No editar

    def __repr__(self): # No editar
        return 'Juan'   # No editar

    # Escriba aqui un metodo llamado 'ordenar_bebida' sin parametros que retorna la bebida preferida de Juan
    # decore este metodo. Usando el decorador 'tomar_tiempo'


    # Escriba aqui un metodo llamado 'ordenar_comida' sin parametros que retorna la comida preferida de Juan
    # decore este metodo. Usando el decorador 'tomar_tiempo'



class ClienteCarlos:    # No editar
    def __str__(self):  # No editar
        return 'Carlos' # No editar

    def __repr__(self): # No editar
        return 'Carlos' # No editar

    # Escriba aqui un metodo llamado 'ordenar_bebida' sin parametros que retorna la bebida preferida de Carlos
    # decore este metodo. Usando el decorador 'tomar_tiempo'


    # Escriba aqui un metodo llamado 'ordenar_comida' sin parametros que retorna la bebida preferida de Carlos
    # decore este metodo. Usando el decorador 'tomar_tiempo'



class ClienteAndres:    # No editar
    def __str__(self):  # No editar
        return 'Andres' # No editar

    def __repr__(self): # No editar
        return 'Andres' # No editar

    # Escriba aqui un metodo llamado 'ordenar_bebida' sin parametros que retorna la bebida preferida de Andres
    # decore este metodo. Usando el decorador 'tomar_tiempo'


    # Escriba aqui un metodo llamado 'ordenar_bebida' sin parametros que retorna la comida preferida de Andres
    # decore este metodo. Usando el decorador 'tomar_tiempo'


# Crear lista vacia llamada 'visitas_clientes'

# Crear lista vacia llamada 'pedidos_cocina'


# Menu de los productos que ofrece la cantina y su precio
# No editar
menu = {
    'whiskey': 1000,
    'ron': 1200,
    'vino': 2000,
    'taco': 2000,
    'hamburguesa': 2500,
    'chifrijo': 3000
}


@app.callback(Output('contenedor_juan', 'children'), Output('clientes', 'children'), Input('juan_boton', 'n_clicks')) # No editar
def juan_pide(n_clicks): # No editar
    if n_clicks: # No editar

        # Crear aqui variable 'cliente_juan' con el objeto creado con la clase 'ClienteJuan'

        # Agregar aqui la variable 'cliente_juan' al final de la lista 'visitas_clientes'

    return '', formato_listas(visitas_clientes) # No editar


@app.callback(Output('contenedor_carlos', 'children'), Output('clientes', 'children'), Input('carlos_boton', 'n_clicks')) # No editar
def carlos_pide(n_clicks): # No editar
    if n_clicks: # No editar
        # Crear aqui variable 'cliente_carlos' con el objeto creado con la clase 'ClienteCarlos'

        # Agregar aqui la variable 'cliente_carlos' al final de la lista 'visitas_clientes'

    return '', formato_listas(visitas_clientes) # No editar

@app.callback(Output('contenedor_andres', 'children'),Output('clientes', 'children'), Input('andres_boton', 'n_clicks')) # No editar
def andres_pide(n_clicks): # No editar
    if n_clicks: # No editar
        # Crear aqui variable 'cliente_andres' con el objeto creado con la clase 'ClienteAndres'

        # Agregar aqui la variable 'cliente_andres' al final de la lista 'visitas_clientes'

    return '', formato_listas(visitas_clientes) # No editar


@app.callback(Output('clientes', 'children'), Output('balance', 'children'), Output('pedidos', 'children'), Input('procesar_pedido', 'n_clicks'), State('balance', 'children')) # No editar
def procesar_pedido(n_clicks, balance_cocina): # No editar
    if (n_clicks>0) & (len(visitas_clientes)>0): # No editar

        # Crear aqui la variable 'atendiendo_cliente' usando el primer elemento de la lista 'visitas_clientes' luego elimine ese primer elemento de esa lista. Hint: puede usar la funcion pop(0)


        # El paso anterior obtiene el primer cliente en la lista de visitas. Ejecute aqui su metodo llamado 'ordenar_bebida()' para obtener su bebida. Crear variable 'bebida' para almacenar su resultado

        # Para el mismo cliente del paso anterior .Ejecute aqui su metodo llamado 'ordenar_comida()' para obtener su comida. Crear variable 'comida' para almacenar su resultado

        # Agregar aqui la bebida al final de la lista 'pedidos_cocina'

        # Agregar aqui la comida al final de la lista 'pedidos_cocina'
        

        # Usando la variable 'balance_cocina' actualice aqui su valor sumandole el precio de la bebida. Utilice el diccionario 'menu' para obtener el precio de la bebida


        # Usando la variable 'balance_cocina' actualice aqui su valor sumandole el precio de la comida. Utilice el diccionario 'menu' para obtener el precio de la comida


    return formato_listas(visitas_clientes), balance_cocina, formato_listas(pedidos_cocina) # No editar


if __name__ == "__main__":     # No editar
    app.run_server(debug=True) # No editar
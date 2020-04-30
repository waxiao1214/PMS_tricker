import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from flask import Flask
from flask_mysqldb import MySQL


# Defining the name of the app
app_name = "FluMeter"

LOGOTYPE = "/assets/logo-placeholder.png"

app = Flask(__name__)

app.config["MYSQL_USER"]
app.config["MYSQL_PASSWORD"]
app.config["MYSQL_HOST"]
app.config["MYSQL_DB"]
app.config["MYSQL_CURSORCLASS"]
mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connecion.cursor()
    cur.execute('''CREATE TABEL example (id INTEGER, name VARCHAR(20))''')
    return "Done!"

# Instantianting the Dash APP
dApp = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR,  # DARK OPTIONS: CYBORG, SOLAR, DARKLY, SLATE, SUPERHERO
                                     'https://use.fontawesome.com/releases/v5.8.1/css/all.css',
                                     'https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css'])



if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=int("8080"), debug=True)
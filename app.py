import dash
from flask import Flask

if __name__ == '__main__':
    #app.run_server(debug=True)
    app.run_server(host="0.0.0.0", port=int("8080"), debug=True)
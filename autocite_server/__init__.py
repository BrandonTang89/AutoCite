from flask import Flask

app = Flask(__name__)

from autocite_server import routes


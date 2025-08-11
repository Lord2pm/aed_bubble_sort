from flask import Flask

from routes import teams_routes

app = Flask(__name__)

app.register_blueprint(teams_routes.teams_blueprint)

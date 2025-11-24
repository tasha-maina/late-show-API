from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from models import db, Episode, Guest, Appearance  
from routes import Episodes, EpisodeById, Guests, Appearances

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    Migrate(app, db)

    api = Api(app)
    api.add_resource(Episodes, "/episodes")
    api.add_resource(EpisodeById, "/episodes/<int:id>")
    api.add_resource(Guests, "/guests")
    api.add_resource(Appearances, "/appearances")


    @app.route("/")
    def index():
        return {"message": "Late Show API running!"}, 200

    return app


app = create_app()

if __name__ == "__main__":
    app.run(port=5555, debug=True)

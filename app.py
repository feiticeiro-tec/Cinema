from flask import Flask
import core
import api

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["ALEMBIC"] = {
    "script_location": "core/migrations",
}
db = core.init_app(app)
api.init_app(app)
with app.app_context():
    if app.config["SQLALCHEMY_DATABASE_URI"].startswith("sqlite"):
        db.create_all()
    else:
        db.alembic.upgrade()

from flask_app import app
from flask_app.controllers import LR_controller
from flask_app.models.LR_model import User


if __name__ == "__main__":
    app.run(debug=True)
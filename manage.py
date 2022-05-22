from app import app
from flask.cli import FlaskGroup


manager = FlaskGroup(app)


if __name__ == '__main__':
    manager()
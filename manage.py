from flask import Flask
from app import create_app
    

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app = create_app()
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run()

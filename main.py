from flask import Flask
from app_init import init_app
from service import Service

app = Flask(__name__)
init_app() # Initialization of app

class MemoryLeak:
    d = []
    def get(self):
        return self.d
    def set(self, d):
        self.d = d

@app.route("/")
def hello_world():
    m = MemoryLeak()
    m.set('ola')    
    return m.get()

@app.route("/inject")
def injection():
    return Service().res

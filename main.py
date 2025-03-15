from flask import Flask

app = Flask(__name__)

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

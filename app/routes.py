from app import app

@app.route('/')
@app.route('/index')
def index():
    return "<h1>Hello, Timo</h1>"
from flask import Flask

app = Flask(__name__)

@app.route("/")
def details():
    items = ["<h1>Company Name: ABC Corporation</h1>","<h1>Location: India </h1>","<h1>Contact Detail: 999-999-9999</h1>"]
    items = "\n".join(items)
    return items

@app.route("/welcome")
def assignment():
    return "<h1>Welcome to ABC Corporation</h1>"

@app.route("/hello_world")
def hello():
    return"<h1>Hello, World!!</h1>"

from flask import url_for
@app.route("/login")
def login():
    details_url=url_for('details')
    welcome_url=url_for('assignment')  
    hello_world_url=url_for('hello')      
    return f'URL for details: {details_url}<br>' \
           f'URL for welcome: {welcome_url}<br>' \
           f'URL for hello: {hello_world_url}'    


if __name__=="__main__":
    app.run(host="0.0.0.0")

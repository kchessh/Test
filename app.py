from flask import Flask

app = Flask(__name__)

@app.route("/")
def initial_test():
  return "<p>This is the test alskdjflaskdja2 another test </p>"

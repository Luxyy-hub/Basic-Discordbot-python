from flask import Flask
from threading import Thread
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hi!'

app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

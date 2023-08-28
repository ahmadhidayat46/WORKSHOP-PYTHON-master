# import modul flask dari library Flask
from flask import Flask

# membuat instance dari kelas Flask
app = Flask(__name__)

# ketika web diakses akan merouting ke root dan menjalankan fungsi hello()
@app.route('/')
def hello():
    return 'Hello, World!'

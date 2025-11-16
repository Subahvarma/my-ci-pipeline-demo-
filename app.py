from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
<<<<<<< HEAD
    return "Hello Jenkins subha Pipeline!"
=======
    return "Hello Jenkins Pipeline! subha"
>>>>>>> 080de4554fb0585a893f218f688f5faeebb8385f

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


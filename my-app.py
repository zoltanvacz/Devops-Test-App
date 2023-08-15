from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
        version = "1.0"
        return 'Version: ' +version

if __name__ == '__main__':
        app.run()

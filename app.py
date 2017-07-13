from flask import Flask
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    return "LetyBot"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = bool(os.environ.get('DEBUG', True))
    print(port)
    print(debug)
    app.run(host='0.0.0.0', port=port, debug=True)


from flask import Flask
from modules.dataframes import generate_global_dataframe
app = Flask(__name__)

@app.route ("/")
def index():
    return generate_global_dataframe()


if __name__ == '__main__':
    app.run(debug=True)

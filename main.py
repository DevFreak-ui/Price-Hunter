from flask import Flask, render_template, request

# custom api's
from  api import jumia_api, tonaton_api


app = Flask(__name__)



@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/query")
def query():
    search_word = request.args.get('search_word')
    if (search_word == ""):
        return render_template('index.html')
    else:
        jumia_call = jumia_api.jumia(search_word)
        tonaton_call = tonaton_api.tonaton(search_word)
        return render_template('index.html', jumia_products=jumia_call, tonaton_products=tonaton_call, search_word=search_word)

if __name__ == '__main__':
    app.run(debug=True)
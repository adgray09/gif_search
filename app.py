from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract the query term from url using request.args.get()
    
    info = {
        "q": "search",
        "key": "H5WM0TFR6PJ8",
        "limit": 10,
    }
    r = request.args.get("https://api.tenor.com/v1/search?", params=info)
    # TODO: Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'

    # TODO: Make an API call to Tenor using the 'requests' library. For 
    # reference on how to use Tenor, see: 
    # https://tenor.com/gifapi/documentation
<<<<<<< HEAD
   # def get_gif():
   #     r = requests.get(
   # "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))
=======
>>>>>>> a5f16fd5e23f5bb3fa88d9815ed8cb212b7e3978

    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object

    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list

    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

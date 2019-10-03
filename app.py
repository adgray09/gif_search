#I would like to give credit to Ryan Smith for helping me with this project. 
#He helped me get the top 10 results for a websearch and much more. 


from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()

TENOR_API_KEY = os.getenv("TENOR_API_KEY")


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract the query term from url using request.args.get()
    name = request.args.get('search')


    # TODO: Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'
    params = {
        'q': name,
        'key': TENOR_API_KEY,
        'limit': 10,
    }

    r = requests.get("https://api.tenor.com/v1/search?", params = params)

    if r.status_code == 200:
        # json.loads returns a JSON OBJECT
        response_dict = json.loads(r.content)
        # Retrieve results from response dict
        top_ten = response_dict['results']
        print(top_ten[0])
        print("HERE__________________________")
        #print(len(top_ten['results']))
        # if 


    # TODO: Make an API call to Tenor using the 'requests' library. For 
    # reference on how to use Tenor, see: 
    # https://tenor.com/gifapi/documentation

    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object

    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list

    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'

    return render_template("index.html", gifs=top_ten)

    


if __name__ == '__main__':
    app.run(debug=True)

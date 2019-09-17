#I would like to give credit to Ryan Smith for helping me with this project. 
#He helped me get the top 10 results for a websearch and much more. 


from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

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
        'key': "H5WM0TFR6PJ8",
        'limit': 10,
    }

    r = requests.get("https://api.tenor.com/v1/search?", params = params)

    if r.status_code == 200:
        # json.loads returns a JSON OBJECT
        response_dict = json.loads(r.content)
        # Retrieve results from response dict
        top_ten = response_dict['results']
        print(top_ten)
        print("HERE__________________________")
        print(len(top_ten['results']))
        # if 


    # TODO: Make an API call to Tenor using the 'requests' library. For 
    # reference on how to use Tenor, see: 
    # https://tenor.com/gifapi/documentation
    # def get_gif():
    #     r = requests.get(
    # "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))
    #if r.status_code == 200:
        #top_10gifs = json.loads(r.content)
        #print(top_10gifs)
    #else:
        #top_10gifs = None

    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object

    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list

    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'

    return render_template("index.html")
    
<<<<<<< HEAD
    # index()
=======
index()
>>>>>>> 792efc259da9390a3559971ffd774204187b75e0

if __name__ == '__main__':
    app.run(debug=True)

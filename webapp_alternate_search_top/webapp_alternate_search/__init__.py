import os, sys
sys.path.append(".")
import webapp_alternate_search

from flask import Flask
import flask
import random
from webapp_alternate_search.db import get_db, init_app

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Landing page
    @app.route('/', methods=['GET', 'POST'])
    def hello():
        # return 'Hello, World!'
        
        # Return landing page
        if flask.request.method == 'GET':

            # Option 1: Get all listings
            db = get_db()
            listings = db.execute(
                    'SELECT listingid, city, name, neighbourhood, price, rating, score FROM listings ORDER BY score DESC'
                ).fetchall()
            filter_product_category = None
            return(flask.render_template('base.html', listings=listings, filter_product_category=filter_product_category))


        # Return prediction output
        if flask.request.method == 'POST':
            db = get_db()

            if ("filter_product_button" in flask.request.form):
                filter_product_category = flask.request.form["filter_product_button"]
                print(filter_product_category)

                if filter_product_category == "Random":
                    listings = db.execute(
                        'SELECT listingid, city, name, neighbourhood, price, rating, score FROM listings'
                    ).fetchall()
                    random.shuffle(listings)
                elif filter_product_category == "Image aesthetic: Low to High":
                    listings = db.execute(
                        'SELECT listingid, city, name, neighbourhood, price, rating, score FROM listings ORDER BY score ASC'
                    ).fetchall()
                elif filter_product_category == "Image aesthetic: High to Low":
                    listings = db.execute(
                        'SELECT listingid, city, name, neighbourhood, price, rating, score FROM listings ORDER BY score DESC'
                    ).fetchall()
                elif filter_product_category == "Listing Vibe: Family":
                    listings = db.execute(
                        'SELECT listingid, city, name, neighbourhood, price, rating, score, vibe FROM listings l WHERE l.vibe = 1'
                    ).fetchall()
                elif filter_product_category == "Listing Vibe: Friends":
                    listings = db.execute(
                        'SELECT listingid, city, name, neighbourhood, price, rating, score, vibe FROM listings l WHERE l.vibe = 0'
                    ).fetchall()
                elif filter_product_category == "Listing Vibe: Solo,Business":
                    listings = db.execute(
                        'SELECT listingid, city, name, neighbourhood, price, rating, score, vibe FROM listings l WHERE l.vibe = 2'
                    ).fetchall()
                else:
                    filter_product_category = "Image aesthetic: High to Low"
                    listings = db.execute(
                        'SELECT listingid, city, name, neighbourhood, price, rating, score FROM listings ORDER BY score DESC'
                    ).fetchall()


            return(flask.render_template('base.html', listings=listings, filter_product_category=filter_product_category))


            """
            # Read variables from form
            temperature = flask.request.form['temperature']
            humidity = flask.request.form['humidity']
            windspeed = flask.request.form['windspeed']

            # Create input to Model from form data
            input_variables = pd.DataFrame([[temperature, humidity, windspeed]],
                                           columns=['temperature', 'humidity', 'windspeed'],
                                           dtype=float)

            # Inference: Get prediction from Model
            prediction = model.predict(input_variables)[0]

            # Return Model output
            return flask.render_template('main.html',
                                         original_input={'Temperature':temperature,
                                                         'Humidity':humidity,
                                                         'Windspeed':windspeed},
                                         result=prediction,
                                         )
            """

    #Bootstrap(app)

    return app

# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    print(("* Flask starting server..."
        "please wait until server has fully started"))
    app = create_app()
    app.run(host='0.0.0.0', port=5002)
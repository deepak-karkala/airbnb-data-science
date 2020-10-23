import os
import pickle
from flask import Flask
import flask
from flask_bootstrap import Bootstrap
import sklearn
import joblib
import pandas as pd

# Load pre-trained machine learning model.
base_path = "/Users/nesara/Documents/aim/cs/projects/airbnb-data-science/webapp/";
#with open(base_path + 'static/model/decision_tree.pkl', 'rb') as f:
#    model = pickle.load(f)
model = joblib.load(base_path + "static/model/fullpipeline_linearregression.pkl")


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        #DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
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
            return(flask.render_template('base.html'))


        # Return prediction output
        if flask.request.method == 'POST':

            # Dropdowns
            country = flask.request.form.get('combobox_country')
            city = flask.request.form.get('combobox_city')
            neighbourhood = flask.request.form.get('combobox_neighbourhood')
            propertytype = flask.request.form.get('combobox_propertytype')
            roomtype = flask.request.form.get('combobox_roomtype')
            bedtype = flask.request.form.get('combobox_bedtype')
            cancellationpolicy = flask.request.form.get('combobox_cancellationpolicy')
            hostresponsetime = flask.request.form.get('combobox_hostresponsetime')


            # Text input
            accommodates = flask.request.form['accommodates']
            num_bedrooms = flask.request.form['num_bedrooms']
            num_beds = flask.request.form['num_beds']
            min_nights = flask.request.form['min_nights']
            availability_30 = flask.request.form['availability_30']
            availability_60 = 12
            availability_90 = 12
            availability_365 = flask.request.form['availability_365']
            num_reviews = flask.request.form['num_reviews']
            reviews_per_month = 0.22
            review_scores_rating = flask.request.form['review_scores_rating']
            review_scores_accuracy = flask.request.form['review_scores_accuracy']
            review_scores_cleanliness = flask.request.form['review_scores_cleanliness']
            review_scores_checkin = flask.request.form['review_scores_checkin']
            review_scores_communication = flask.request.form['review_scores_communication']
            review_scores_location = flask.request.form['review_scores_location']
            review_scores_value = flask.request.form['review_scores_value']
            host_since = flask.request.form['host_since']
            host_response_rate = flask.request.form['host_response_rate']
            host_num_listings = flask.request.form['host_num_listings']



            # Create input to Model from form data
            df_input = pd.DataFrame([[country, city, neighbourhood, propertytype, roomtype, bedtype,
                                    cancellationpolicy, hostresponsetime, accommodates, num_bedrooms, num_beds,
                                    min_nights, availability_30, availability_60, availability_90, availability_365,
                                    num_reviews, reviews_per_month, review_scores_rating, review_scores_accuracy, 
                                    review_scores_cleanliness, review_scores_checkin, review_scores_communication,
                                    review_scores_location, review_scores_value, host_response_rate,
                                    ]],
                                   columns=['Country', 'City', 'Neighbourhood Cleansed', 'Property Type',
                                           'Room Type', 'Bed Type', 'Cancellation Policy', 'Host Response Time',
                                           'Accommodates', 'Bedrooms', 'Beds', 'Minimum Nights', 'Availability 30',
                                           'Availability 60', 'Availability 90', 'Availability 365',
                                           'Number of Reviews', 'Reviews per Month', 'Review Scores Rating',
                                           'Review Scores Accuracy', 'Review Scores Cleanliness',
                                           'Review Scores Checkin', 'Review Scores Communication',
                                           'Review Scores Location', 'Review Scores Value', 'Host Response Rate'],
                                   dtype=float)

            # Inference: Get prediction from Model
            prediction_price = model.predict(df_input)[0]




            return(flask.render_template('base.html',   original_input={    'country': country,
                                                                            'city': city,
                                                                            'neighbourhood': neighbourhood,
                                                                            'propertytype': propertytype,
                                                                            'roomtype': roomtype,
                                                                            'bedtype': bedtype,
                                                                            'cancellationpolicy': cancellationpolicy,
                                                                            'hostresponsetime': hostresponsetime,
                                                                            'accommodates': accommodates,
                                                                            'num_bedrooms': num_bedrooms,
                                                                            'num_beds': num_beds,
                                                                            'min_nights': min_nights,
                                                                            'availability_30': availability_30,
                                                                            'availability_365': availability_365,
                                                                            'num_reviews': num_reviews,
                                                                            'review_scores_rating': review_scores_rating,
                                                                            'review_scores_accuracy': review_scores_accuracy,
                                                                            'review_scores_cleanliness': review_scores_cleanliness,
                                                                            'review_scores_checkin': review_scores_checkin,
                                                                            'review_scores_communication': review_scores_communication,
                                                                            'review_scores_location': review_scores_location,
                                                                            'review_scores_value': review_scores_value,
                                                                            'host_since': host_since,
                                                                            'host_response_rate': host_response_rate,
                                                                            'host_num_listings': host_num_listings,
                                                                        },
                                                        result=prediction_price))

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

    Bootstrap(app)

    return app
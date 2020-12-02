import os, sys
sys.path.append(".")
import webapp_predict_price

import pickle
from flask import Flask
import flask
import sklearn
import joblib
import pandas as pd

# Load pre-trained machine learning model.
BASE_PATH = "webapp_predict_price/"
#with open(base_path + 'static/model/decision_tree.pkl', 'rb') as f:
#    model = pickle.load(f)
model = joblib.load(BASE_PATH + "static/model/fullpipeline_linearregression.pkl")


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
            if country == "":
                country = "United States"
            city = flask.request.form.get('combobox_city')
            if city == "":
                city = "New York"
            neighbourhood = flask.request.form.get('combobox_neighbourhood')
            if neighbourhood == "":
                neighbourhood = "Downtown Brooklyn"
            propertytype = flask.request.form.get('combobox_propertytype')
            if propertytype == "":
                propertytype = "House"
            roomtype = flask.request.form.get('combobox_roomtype')
            if roomtype == "":
                roomtype = "Entire home/apt"
            bedtype = flask.request.form.get('combobox_bedtype')
            if bedtype == "":
                bedtype = "Real Bed"
            cancellationpolicy = flask.request.form.get('combobox_cancellationpolicy')
            if cancellationpolicy == "":
                cancellationpolicy = "moderate"
            hostresponsetime = flask.request.form.get('combobox_hostresponsetime')
            if hostresponsetime == "":
                hostresponsetime = "within a day"

            # Text input
            accommodates = flask.request.form['accommodates']
            if accommodates == "":
                accommodates = 2
            num_bedrooms = flask.request.form['num_bedrooms']
            if num_bedrooms == "":
                num_bedrooms = 1
            num_beds = flask.request.form['num_beds']
            if num_beds == "":
                num_beds = 1
            min_nights = flask.request.form['min_nights']
            if min_nights == "":
                min_nights = 1
            availability_30 = flask.request.form['availability_30']
            if availability_30 == "":
                availability_30 = 15
            availability_60 = 12
            availability_90 = 12
            availability_365 = flask.request.form['availability_365']
            if availability_365 == "":
                availability_365 = 150
            num_reviews = flask.request.form['num_reviews']
            if num_reviews == "":
                num_reviews = 50
            reviews_per_month = 0.22
            review_scores_rating = flask.request.form['review_scores_rating']
            if review_scores_rating == "":
                review_scores_rating = 80
            review_scores_accuracy = flask.request.form['review_scores_accuracy']
            if review_scores_accuracy == "":
                review_scores_accuracy = 8
            review_scores_cleanliness = flask.request.form['review_scores_cleanliness']
            if review_scores_cleanliness == "":
                review_scores_cleanliness = 8
            review_scores_checkin = flask.request.form['review_scores_checkin']
            if review_scores_checkin == "":
                review_scores_checkin = 8
            review_scores_communication = flask.request.form['review_scores_communication']
            if review_scores_communication == "":
                review_scores_communication = 8
            review_scores_location = flask.request.form['review_scores_location']
            if review_scores_location == "":
                review_scores_location = 8
            review_scores_value = flask.request.form['review_scores_value']
            if review_scores_value == "":
                review_scores_value = 8
            host_since = flask.request.form['host_since']
            if host_since == "":
                host_since = 100
            host_response_rate = flask.request.form['host_response_rate']
            if host_response_rate == "":
                host_response_rate = 90
            host_num_listings = flask.request.form['host_num_listings']
            if host_num_listings == "":
                host_num_listings = 1



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
            prediction_price = round(prediction_price)



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

    #Bootstrap(app)

    return app


# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    print(("* Loading Scikit-learn model and Flask starting server..."
        "please wait until server has fully started"))
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
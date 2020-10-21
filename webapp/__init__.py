import os
import pickle
from flask import Flask
import flask
from flask_bootstrap import Bootstrap
import sklearn
import joblib

# Load pre-trained machine learning model.
base_path = "/Users/nesara/Documents/aim/cs/projects/airbnb-data-science/webapp/";
#with open(base_path + 'static/model/decision_tree.pkl', 'rb') as f:
#    model = pickle.load(f)
model = joblib.load(base_path + "static/model/decision_tree.pkl")


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
            if neighbourhood == "":
                neighbourhood = "Downtown Brooklyn"


            propertytype = flask.request.form.get('combobox_propertytype')
            roomtype = flask.request.form.get('combobox_roomtype')
            bedtype = flask.request.form.get('combobox_bedtype')
            cancellationpolicy = flask.request.form.get('combobox_cancellationpolicy')
            hostresponsetime = flask.request.form.get('combobox_hostresponsetime')


            # Text input
            accommodates = flask.request.form['accommodates']


            return(flask.render_template('base.html',   original_input={    'country': country,
                                                                            'city': city,
                                                                            'neighbourhood': neighbourhood,
                                                                            'propertytype': propertytype,
                                                                            'roomtype': roomtype,
                                                                            'bedtype': bedtype,
                                                                            'cancellationpolicy': cancellationpolicy,
                                                                            'hostresponsetime': hostresponsetime,
                                                                            'accommodates': accommodates,
                                                                        },
                                                        result=5))

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
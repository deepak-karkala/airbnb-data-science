# Predictive Price Modeling for Airbnb listings
The project aimed at predicting the price of an Airbnb listing given a number of features. The project involved exploratory data analysis, data pre-processing, feature selection, Model Fitting, Model Comparison and deploying the containerised Webapp on AWS using CI/CD Pipeline.

## Project Resources
<div class="row">
	<div class="col-lg-8 col-md-10 col-sm-10 col-12 mx-auto">
	  <ul>
	    <li><a href="http://ec2-65-0-106-104.ap-south-1.compute.amazonaws.com:5000/">AWS Webapp</a> for this project</li>
	    <li>View Project <a href="http://deepakkarkala.com/docs/articles/machine_learning/airbnb_price_modeling/about/index.html">Report</a></li>
	    <li><a href="https://public.opendatasoft.com/explore/dataset/airbnb-listings/information/?disjunctive.host_verifications&disjunctive.amenities&disjunctive.features&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiQ09VTlQiLCJ5QXhpcyI6Imhvc3RfbGlzdGluZ3NfY291bnQiLCJzY2llbnRpZmljRGlzcGxheSI6dHJ1ZSwiY29sb3IiOiJyYW5nZS1jdXN0b20ifV0sInhBeGlzIjoiY2l0eSIsIm1heHBvaW50cyI6IiIsInRpbWVzY2FsZSI6IiIsInNvcnQiOiIiLCJzZXJpZXNCcmVha2Rvd24iOiJyb29tX3R5cGUiLCJjb25maWciOnsiZGF0YXNldCI6ImFpcmJuYi1saXN0aW5ncyIsIm9wdGlvbnMiOnsiZGlzanVuY3RpdmUuaG9zdF92ZXJpZmljYXRpb25zIjp0cnVlLCJkaXNqdW5jdGl2ZS5hbWVuaXRpZXMiOnRydWUsImRpc2p1bmN0aXZlLmZlYXR1cmVzIjp0cnVlfX19XSwidGltZXNjYWxlIjoiIiwiZGlzcGxheUxlZ2VuZCI6dHJ1ZSwiYWxpZ25Nb250aCI6dHJ1ZX0%3D">Airbnb Dataset</a> used in the project</li>
	    <li>Run this code on <a href="https://colab.research.google.com/drive/1IBYyAjdGXzAeNPSdNbfIyzgu-lG6Hvlp?usp=sharing">Google Colab</a></li>
	    <li>View Source on <a href="https://github.com/deepak-karkala/airbnb-data-science/tree/master/webapp_predict_price">Github</a></li>
	    <li>Docker Container for the project: dkarkala01/airbnb-predict</li>
	  </ul>
	</div>
</div>

## Project Goals and Objectives
<div class="row">
    <div class="col-lg-8 col-md-10 col-sm-10 col-12 mx-auto">
      <p style="margin-top:0px;">The Short Answer: Assisting Airbnb hosts to set appropriate price for their listings</p>
      <p class="p_no_top_gap">
        <b>The Problem</b>: Currently there is no convenient way for a new Airbnb host to decide the price of his or her listing. New hosts must often rely on the price of neighbouring listings when deciding on the price of their own listing.
      </p>
      <p class="p_no_top_gap">
        <b>The Solution</b>: A Predictive Price Modelling tool whereby a new host can enter all the relevant details such as location of the listing, listing properties, available amenities etc and the Machine Learning Model will suggest the Price for the listing. The Model would have previously been trained on similar data from already existing Airbnb listings.
      </p>
    </div>
 </div>

  <div class="row">
    <div class="col-lg-8 col-md-10 col-sm-10 col-12 mx-auto">
      <h3 class="sub-title">Project Overview</h3>
    </div>
  </div>

  <div class="row">
    <div class="col-lg-8 col-md-10 col-sm-10 col-12 mx-auto">
      <p class="p_no_top_gap">
        The project involved the following steps,
        <ul>
          <li><b>Exploratory Data Analysis</b>: Explore the various features, their distributions using Histograms and Box-plots</li>
          <li><b>Pre-processing and Data Cleaning</b>: Normalisation, filling missing values, encoding categorical values</li>
          <li><b>Feature Selection</b>: Study the correlation with response variable (Listing Price) and determine which features are most useful in predicting the price.</li>
          <li><b>Model Fitting and Selection</b>: Training different models, tuning hyper-parameters and studying Model performance using Learning Curve.</li>
          <li><b>Model Serving</b>: Using FLASK to deploy and serve Model predictions using REST API</li>
          <li><b>Container</b>: Using Docker to containerise the Web Application</li>
          <li><b>Production</b>: Using AWS CI/CD Pipeline for continuous integration and deployment.</li>
        </ul>
      </p>
    </div>
  </div>


  <div class="row">
    <div class="col-lg-6 col-md-10 col-sm-10 col-10 mx-auto image_top">
      <img src="images/predict_overview.png">
    </div>
  </div>

  <div class="row">
    <div class="col-lg-8 col-md-10 col-sm-10 col-12 mx-auto">
      <h3 class="sub-title">End Result</h3>
    </div>
  </div>

  <div class="row">
    <div class="col-lg-8 col-md-10 col-sm-10 col-12 mx-auto">
      <p class="p_no_top_gap">
        The screen capture of the entire application in use is shown below. Users can enter all the relevant details of their listings, the trained Predictive Model will then predict and return the price of the listing given all the features. 
      </p>
    </div>
  </div>

  <div class="row">
    <div class="col-lg-6 col-md-10 col-sm-10 col-10 mx-auto image_top">
      <img src="images/airbnb_predict_demo.gif">
    </div>
  </div>

  <div class="row">
        <div class="col-lg-8 col-md-10 col-sm-10 col-12 mx-auto">
          <h3>About Dataset</h3>
        </div>
      </div>

  <div class="row">
    <div class="col-lg-8 col-md-10 col-sm-10 col-12 mx-auto">
      <p class="p_no_top_gap">
        The Dataset used in this project was obtained from <a href="https://public.opendatasoft.com/explore/dataset/airbnb-listings/table/?disjunctive.host_verifications&disjunctive.amenities&disjunctive.features&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiQ09VTlQiLCJ5QXhpcyI6Imhvc3RfbGlzdGluZ3NfY291bnQiLCJzY2llbnRpZmljRGlzcGxheSI6dHJ1ZSwiY29sb3IiOiJyYW5nZS1jdXN0b20ifV0sInhBeGlzIjoiY2l0eSIsIm1heHBvaW50cyI6IiIsInRpbWVzY2FsZSI6IiIsInNvcnQiOiIiLCJzZXJpZXNCcmVha2Rvd24iOiJyb29tX3R5cGUiLCJjb25maWciOnsiZGF0YXNldCI6ImFpcmJuYi1saXN0aW5ncyIsIm9wdGlvbnMiOnsiZGlzanVuY3RpdmUuaG9zdF92ZXJpZmljYXRpb25zIjp0cnVlLCJkaXNqdW5jdGl2ZS5hbWVuaXRpZXMiOnRydWUsImRpc2p1bmN0aXZlLmZlYXR1cmVzIjp0cnVlfX19XSwidGltZXNjYWxlIjoiIiwiZGlzcGxheUxlZ2VuZCI6dHJ1ZSwiYWxpZ25Nb250aCI6dHJ1ZX0%3D">public.opendatasoft.com</a>. There are a total of 494,954 records each of which contains details of one Airbnb listing. The total size of dataset is 1.89 GB. 
      </p>
      <p class="p_no_top_gap">
        The dataset has a large number of features which can be categorised into following types,
        <ul>
          <li>
            <b>Location related</b>: Country, City, Neighbourhood
          </li>
          <li>
            <b>Property related</b>: Property Type, Room Type, Accommodates, Bedrooms, Beds, Bed Type, Cancellation Policy, Minimum Nights
          </li>
          <li>
            <b>Booking Availability</b>: Availability 30, Availability 60, Availability 90, Availability 365
          </li>
          <li>
            <b>Reviews related</b>: Number of Reviews, Reviews per Month, Review Scores Rating, Review Scores Accuracy, Review Scores Cleanliness, Review Scores Checkin, Review Scores Communication, Review Scores Location, Review Scores Value
          </li>
          <li>
            <b>Host related</b>: Host Since, Host Response Time, Host Response Rate, Calculated host listings count, Host Since Days, Host Has Profile Pic, Host Identity Verified, Is Location Exact, Instant Bookable, Host Is Superhost, Require Guest Phone Verification, Require Guest Profile Picture, Requires License
          </li>
          <li>
            <b>Amenities</b>: TV, Wireless Internet, Kitchen, Heating,
             Family/kid friendly, Washer, Smoke detector, Fire extinguisher,
             Essentials, Cable TV, Internet, Dryer, First aid kit,
             Safety card, Shampoo, Hangers, Laptop friendly workspace,
             Air conditioning, Breakfast, Free parking on premises,
             Elevator in building, Buzzer/wireless intercom, Hair dryer,
             Private living room, Iron, Wheelchair accessible, Hot tub,
             Carbon monoxide detector, 24-hour check-in,
             Pets live on this property, Dog(s), Gym, Lock on bedroom door,
             Private entrance, Indoor fireplace, Smoking allowed,
             Pets allowed, Cat(s), Self Check-In, Doorman Entry,
             Suitable for events, Pool, Lockbox, Bathtub,
             Room-darkening shades, Game console, Doorman, High chair,
             Pack ’n Play/travel crib, Keypad, Other pet(s), Smartlock
          </li>
        </ul>
      </p>
      <p class="p_no_top_gap">
        The price of the listing will serve as labels for the regression task. The goal of this project would be to predict these price of the listings.
      </p>
    </div>
  </div>
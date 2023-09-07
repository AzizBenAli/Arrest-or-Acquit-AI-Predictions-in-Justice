# Import the necessary libraries
from flask import Flask, request, render_template, jsonify
from BankNote import BankNote  # Import the BankNote class as needed
import numpy as np
import pickle

# Create the Flask app
app = Flask(__name__)

# Load your trained classifier
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

# Define the route to serve the HTML page
@app.route("/")
def index():
    return render_template("design.html")

# Define the route to handle predictions
@app.route("/predict", methods=["POST"])
def predict():
    # Get data from the form
    driver_gender = request.form.get("driver_gender")
    driver_age = request.form.get("driver_age")
    driver_race_raw = request.form.get("driver_race_raw")
    driver_race = request.form.get("driver_race")
    violation = request.form.get("violation")
    search_type = request.form.get("search_type")
    search_basis = request.form.get("search_basis")
    contraband_found = request.form.get("contraband_found")
    year = request.form.get("year")
    month = request.form.get("month")
    day_of_week = request.form.get("day_of_week")
    driver_gender_mapping = {'F': 0, 'M': 1}
    driver_race_raw_mapping = {'W N':0 ,'B N':1, 'U H':2, 'W H':3 ,'I N':4 ,'U N':5, 'A N':6 ,'A H':7, 'B H':8, 'I H':9}
    violation_mapping = {'Speeding': 6,                
    'DUI': 8,                      
    'Equipment': 2,                
    'Seat belt': 3,                
    'Other': 1,                    
    'Registration/plates': 7,      
    'Safe movement': 4,            
    'Stop sign/light': 5 }
    search_type_mapping = {'No Search Conducted': 6,                
    'Protective Frisk': 5,                      
    'Incident to Arrest': 4,                
    'Consent': 3,                
    'Probable Cause': 2,                    
    'Warrant': 1,      
           }
    search_basis_mapping={'No Search Conducted':0, 'Observation Suspected Contraband':1,
    'Erratic Suspicious Behaviour':2, 'Other Official Info':3,
    'Suspicious Movement':4, 'Witness Observation':5, 'Informant Tip':6,
    'Observation Suspected Contraband,Other Official Info':7,
    'Erratic Suspicious Behaviour,Witness Observation':8,
    'Erratic Suspicious Behaviour,Observation Suspected Contraband':9,
    'Erratic Suspicious Behaviour,Other Official Info':10,
    'Other Official Info,Witness Observation':11,
    'Observation Suspected Contraband,Witness Observation':12,
    'Erratic Suspicious Behaviour,Observation Suspected Contraband,Other Official Info':13,
    'Erratic Suspicious Behaviour,Observation Suspected Contraband,Other Official Info,Suspicious Movement':14,
    'Observation Suspected Contraband,Informant Tip':15,
    'Observation Suspected Contraband,Other Official Info,Suspicious Movement,Informant Tip,Witness Observation':16,
    'Erratic Suspicious Behaviour,Other Official Info,Informant Tip,Witness Observation':17,
    'Erratic Suspicious Behaviour,Informant Tip':18,
    'Other Official Info,Suspicious Movement':19,
    'Observation Suspected Contraband,Suspicious Movement':20,
    'Erratic Suspicious Behaviour,Other Official Info,Suspicious Movement':21,
    'Informant Tip,Witness Observation':22,
    'Erratic Suspicious Behaviour,Suspicious Movement':23,
    'Erratic Suspicious Behaviour,Observation Suspected Contraband,Suspicious Movement':24,
    'Erratic Suspicious Behaviour,Informant Tip,Suspicious Movement':25,
    'Other Official Info,Observation Suspected Contraband':26,
    'Erratic Suspicious Behaviour,Other Official Info,Observation Suspected Contraband':27,
    'Other Official Info,Observation Suspected Contraband,Suspicious Movement':28,
    'Erratic Suspicious Behaviour,Other Official Info,Informant Tip,Observation Suspected Contraband':29,
    'Other Official Info,Informant Tip':30,
    'Informant Tip,Observation Suspected Contraband':31,
    'Erratic Suspicious Behaviour,Other Official Info,Observation Suspected Contraband,Suspicious Movement':32}
   
    race_mapping = {
    'White': 0,
    'Black': 1,
    'Hispanic': 2,
    'Other': 3,
    'Asian': 4
}    
    driver_race = race_mapping.get(driver_race, -1)
    driver_gender = driver_gender_mapping.get(driver_gender, -1)
    driver_race_raw = driver_race_raw_mapping.get(driver_race_raw, -1)
    violation = violation_mapping.get(violation, -1)
    search_type = search_type_mapping.get(search_type, -1)
    search_basis = search_basis_mapping.get(search_basis, -1)

    # Perform the necessary data mappings and preprocessing as in your FastAPI code

    # Make predictions
    prediction = classifier.predict([[driver_gender, driver_age, driver_race_raw, driver_race, violation, search_type,False, search_basis, year, month, day_of_week]])
    
    # Map prediction result
    if prediction[0] == 1:
        prediction_result = "Arrest"
    else:
        prediction_result = "Don't Arrest"

    # Return the prediction result
    return jsonify({"prediction": prediction_result})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)

import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("disease_diagnosis_model.pkl")

# Load dataset and clean it
df = pd.read_csv("Training.csv")
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]  

# Extract feature names (excluding prognosis)
feature_names = df.drop(columns=["prognosis"]).columns.tolist()

# Define symptom groups
symptom_groups = {
    "General Symptoms": [
        "fatigue", "weight_gain", "weight_loss", "lethargy", "chills", "high_fever", "sweating",
        "dehydration", "malaise", "loss_of_appetite", "mild_fever", "shivering", "restlessness",
        "irregular_sugar_level", "cold_hands_and_feets"
    ],
    "Respiratory Symptoms": [
        "continuous_sneezing", "cough", "breathlessness", "chest_pain", "phlegm",
        "throat_irritation", "redness_of_eyes", "sinus_pressure", "runny_nose", "congestion",
        "blood_in_sputum", "mucoid_sputum", "rusty_sputum"
    ],
    "Gastrointestinal Symptoms": [
        "vomiting", "stomach_pain", "acidity", "ulcers_on_tongue", "nausea", "indigestion",
        "abdominal_pain", "diarrhoea", "constipation", "yellowish_skin", "dark_urine",
        "yellow_urine", "yellowing_of_eyes", "acute_liver_failure", "swelling_of_stomach",
        "distention_of_abdomen", "stomach_bleeding", "passage_of_gases", "sunken_eyes",
        "belly_pain"
    ],
    "Skin-Related Symptoms": [
        "itching", "skin_rash", "nodal_skin_eruptions", "dischromic _patches", "pus_filled_pimples",
        "blackheads", "scurring", "skin_peeling", "silver_like_dusting", "small_dents_in_nails",
        "inflammatory_nails", "blister", "red_sore_around_nose", "yellow_crust_ooze",
        "patches_in_throat"
    ],
    "Neurological Symptoms": [
        "headache", "dizziness", "cramps", "weakness_of_one_body_side", "loss_of_balance",
        "unsteadiness", "spinning_movements", "altered_sensorium", "lack_of_concentration",
        "visual_disturbances", "slurred_speech", "loss_of_smell"
    ],
    "Musculoskeletal Symptoms": [
        "joint_pain", "muscle_wasting", "muscle_weakness", "back_pain", "neck_pain",
        "knee_pain", "hip_joint_pain", "stiff_neck", "swelling_joints", "movement_stiffness",
        "painful_walking", "muscle_pain", "weakness_in_limbs"
    ],
    "Cardiovascular Symptoms": [
        "fast_heart_rate", "palpitations", "prominent_veins_on_calf", "bruising",
        "swollen_blood_vessels"
    ],
    "Endocrine & Metabolic Symptoms": [
        "excessive_hunger", "increased_appetite", "polyuria", "obesity", "enlarged_thyroid",
        "brittle_nails", "swollen_extremeties", "puffy_face_and_eyes", "drying_and_tingling_lips"
    ],
    "Mental Health Symptoms": [
        "anxiety", "mood_swings", "irritability", "depression"
    ],
    "Urogenital Symptoms": [
        "burning_micturition", "spotting_ urination", "bladder_discomfort", "foul_smell_of urine",
        "continuous_feel_of_urine"
    ],
    "Eye & Ear Symptoms": [
        "blurred_and_distorted_vision", "pain_behind_the_eyes", "watering_from_eyes"
    ],
    "Infectious Disease Indicators": [
        "swelled_lymph_nodes", "red_spots_over_body", "extra_marital_contacts",
        "receiving_blood_transfusion", "receiving_unsterile_injections", "toxic_look_(typhos)",
        "history_of_alcohol_consumption"
    ],
    "Other Symptoms": [
        "internal_itching", "family_history", "coma", "pain_during_bowel_movements",
        "pain_in_anal_region", "bloody_stool", "irritation_in_anus", "abnormal_menstruation",
        "swollen_legs", "fluid_overload", "fluid_overload.1"
    ]
}

# Streamlit UI
st.title("🩺 AI-Based Disease Diagnosis System")
st.write("Select your symptoms to get a predicted disease.")

# User input dictionary
user_input = {}

# Display grouped symptoms in expanders
for category, symptoms in symptom_groups.items():
    with st.expander(category):
        for symptom in symptoms:
            user_input[symptom] = st.checkbox(f"{symptom.replace('_', ' ').title()}", key=f"{category}_{symptom}")

user_input_df = pd.DataFrame([user_input]).astype(int)  # Convert True/False to 1/0

user_input_df = user_input_df.reindex(columns=feature_names, fill_value=0)

# Predict disease when the button is clicked
if st.button("🔍 Predict"):
    try:
        prediction = model.predict(user_input_df)[0]
        # If your model outputs encoded labels, uncomment and use the label encoder
        # prediction = label_encoder.inverse_transform([prediction])[0]
        st.success(f"**Predicted Disease:** {prediction} 🎯")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
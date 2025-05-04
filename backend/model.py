import joblib
import pandas as pd

def modelPredect(user_symptoms):

    model = joblib.load('mlsave/random_forest_model.pkl')
    le = joblib.load('mlsave/label_encoder.pkl')

    all_features = [
        'muscle_pain', 'itching', 'altered_sensorium', 'dark_urine', 'high_fever', 
        'mild_fever', 'family_history', 'nausea', 'yellowing_of_eyes', 'sweating', 
        'unsteadiness', 'chest_pain', 'fatigue', 'abdominal_pain', 'joint_pain', 'diarrhoea', 
        'lack_of_concentration', 'red_spots_over_body', 'loss_of_appetite', 'vomiting', 
        'chills', 'breathlessness', 'bladder_discomfort', 'rusty_sputum', 'headache', 
        'dischromic _patches', 'back_pain', 'cough', 'receiving_unsterile_injections', 
        'mucoid_sputum', 'red_sore_around_nose', 'stomach_bleeding', 'abnormal_menstruation', 
        'weight_loss', 'neck_pain', 'stomach_pain', 'internal_itching', 'muscle_weakness', 
        'coma', 'continuous_feel_of_urine', 'passage_of_gases', 'nodal_skin_eruptions', 
        'spotting_ urination', 'slurred_speech', 'polyuria', 'blister', 'movement_stiffness', 
        'blackheads', 'pain_behind_the_eyes', 'swelled_lymph_nodes'
    ]

   # user_symptoms = ['cough', 'muscle_pain']
    features = user_symptoms['symptoms']
    print(features)

    x_input = [1 if symptom in features else 0 for symptom in all_features]

    df_input = pd.DataFrame([x_input], columns=all_features)

    pred = model.predict(df_input)
    label = le.inverse_transform(pred)

    print("Predicted disease:", label[0])

    return label[0]


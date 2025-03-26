import joblib
import pandas as pd
import re
import string
import os

# Get absolute path for the files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the dataset with solutions
file_path = os.path.join(BASE_DIR, 'updated_banking_faq_with_solutions.csv')
df = pd.read_csv(file_path)

# Load the saved model and label encoder
model_path = os.path.join(BASE_DIR, 'svm_cat_a_model.pkl')
le_path = os.path.join(BASE_DIR, 'label_encoder.pkl')

model = joblib.load(model_path)
le = joblib.load(le_path)

# Text Preprocessing Function
def preprocess_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    return text

# Function to predict the solution based on user input
def predict_solution(user_input):
    cleaned_input = preprocess_text(user_input)
    prediction_encoded = model.predict([cleaned_input])[0]
    predicted_category = le.inverse_transform([prediction_encoded])[0]

    # Retrieve the corresponding solution
    solution = df.loc[df['CAT_A'] == predicted_category, 'solution'].values[0]
    return {"category": predicted_category, "solution": solution}


# AI-Disease-Diagnosis
📌 Overview
This project is an AI-based disease diagnosis system that predicts diseases based on user-selected symptoms. The model is trained using a machine learning algorithm on a medical symptoms dataset. The app is built with Streamlit for an interactive user interface. 

📂 Project Structure
bash
Copy
Edit
📦 AI-Disease-Diagnosis  
├── 📜 README.md                      # Project description  
├── 📜 requirements.txt               # List of dependencies  
├── 📜 .gitignore                     # Ignore unnecessary files  
├── 📜 disease_diagnosisLR.ipynb      # Jupyter Notebook for training the model  
├── 📜 disease_diagnosis_model.pkl    # Trained machine learning model  
├── 📜 app.py                         # Streamlit app for disease prediction  
📜 Model Training
The trained model (disease_diagnosis_model.pkl) is generated using disease_diagnosisLR.ipynb.
It was trained on a medical symptoms dataset from Kaggle:
🔗 Disease Prediction Dataset
The model uses Logistic Regression / Decision Tree / Random Forest / [your chosen algorithm] for prediction.
To retrain the model, run the Jupyter Notebook (disease_diagnosisLR.ipynb) and save a new .pkl file.
⚙️ Installation & Setup
1️⃣ Create Virtual Environment
bash
Copy
Edit
python3 -m venv myenv
source myenv/bin/activate  # On macOS/Linux
myenv\Scripts\activate     # On Windows
2️⃣ Install Dependencies
bash
Copy
Edit
pip install --upgrade pip
pip install -r requirements.txt
If you don’t have requirements.txt, install manually:

bash
Copy
Edit
pip install streamlit pandas numpy scikit-learn joblib
3️⃣ Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
📝 Usage
Open the Streamlit app (app.py).
Select symptoms from different categories.
Click on 🔍 Predict to get a disease diagnosis.
The system will display the predicted disease.
🚀 Deployment
This app can be deployed on:

Streamlit Cloud
Hugging Face Spaces
Heroku / Render
For Streamlit Cloud deployment, follow these steps:

Create a GitHub repository and push this project.
Go to Streamlit Cloud and connect your GitHub repo.
Set app.py as the main file and deploy.
📌 Author & Credits
Developed by: Miloni Patel
Dataset Source: Kaggle
Tech Stack: Python, Streamlit, Machine Learning

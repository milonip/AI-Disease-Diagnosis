# 🩺 AI-Based Disease Diagnosis System  

## 📌 Overview  
This project is an **AI-based disease diagnosis system** that predicts diseases based on user-selected symptoms.  
The model is trained using a machine learning algorithm on a **medical symptoms dataset**.  
The app is built with **Streamlit** for an interactive user interface.  

---

## 📂 Project Structure  

📦 AI-Disease-Diagnosis  
├── 📜 README.md                      # Project description  
├── 📜 requirements.txt               # List of dependencies  
├── 📜 .gitignore                     # Ignore unnecessary files  
├── 📜 disease_diagnosisLR.ipynb      # Jupyter Notebook for training the model  
├── 📜 disease_diagnosis_model.pkl    # Trained machine learning model  
├── 📜 app.py                         # Streamlit app for disease prediction  

---

## 📜 Model Training  
- The **trained model (\`disease_diagnosis_model.pkl\`)** is generated using \`disease_diagnosisLR.ipynb\`.  
- It was trained on a **medical symptoms dataset from Kaggle**:  
  🔗 [Disease Prediction Dataset](https://www.kaggle.com/datasets/kaushil268/disease-prediction-using-machine-learning?resource=download)  
- The model uses **Logistic Regression / Decision Tree / Random Forest / [your chosen algorithm]** for prediction.  
- To **retrain the model**, run the **Jupyter Notebook (\`disease_diagnosisLR.ipynb\`)** and save a new \`.pkl\` file.  

---

## ⚙️ Installation & Setup  

### 1️⃣ Create Virtual Environment  
```
python3 -m venv myenv
source myenv/bin/activate  # On macOS/Linux
myenv\Scripts\activate     # On Windows
```

### 2️⃣ Install Dependencies  
```
pip install --upgrade pip
pip install -r requirements.txt
```

> **If you want to install manually:**  
```
pip install streamlit pandas numpy scikit-learn joblib
```

### 3️⃣ Run the Streamlit App  
```
streamlit run app.py
```

---

## 📝 Usage  
1. Open the **Streamlit app** (\`app.py\`).  
2. Select symptoms from different categories.  
3. Click on **🔍 Predict** to get a disease diagnosis.  
4. The system will display the **predicted disease**.

---

## 📌 Author & Credits  
- **Developed by:** Miloni Patel 
- **Dataset Source:** Kaggle  
- **Tech Stack:** Python, Streamlit, Machine Learning  

---

📢 **Feel free to contribute or suggest improvements! 🚀**

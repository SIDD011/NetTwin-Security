# 🛡️ NetTwin Security — ML-Based Intrusion Detection System

A real-time **Machine Learning–based Intrusion Detection System (IDS)** that captures live network traffic, extracts packet features, and classifies traffic as **normal or malicious** using a trained ML model.

This project demonstrates practical understanding of **network traffic analysis, machine learning for cybersecurity, and backend API development** by integrating Wireshark/TShark with a Flask REST API.

---

## 🎯 Project Objective

- Capture live network traffic  
- Extract and analyze packet features  
- Train a Machine Learning model for intrusion detection  
- Classify traffic as Normal or Malicious  
- Provide predictions through a Flask REST API  
- Maintain a clean and modular project structure  

---

## 🧰 Tools & Technology

- Python 3.x  
- Scikit-learn  
- Pandas  
- NumPy  
- Flask  
- Wireshark  
- TShark  
- Git & GitHub  

---

## 🚀 Features

- Live packet capture using Wireshark & TShark  
- Network traffic feature extraction  
- Machine Learning model training (Random Forest)  
- Flask backend API for predictions  
- Real-time intrusion classification  
- Simple and modular project design  

---

## 📂 Project Structure

NetTwin-Security/
│
        
    ├── backend/
           │ └── app.py

     ├── ml_model/
         │ ├── train_model.py
         │ └── ids_model.pkl

     ├── dataset/
         │ └── data.csv

    ├── screenshots/

     └── README.md
     
---

## ⚙️ Installation & Setup

1️⃣ Clone Repository 

     git clone https://github.com/SIDD011/NetTwin-Security.git

2️⃣ Install Dependencies

    pip install flask pandas numpy scikit-learn joblib
    
3️⃣ Train the ML Model
     
    cd ml_model
    python train_model.py
    
4️⃣ Run Backend Server

    cd ../backend
    python app.py
   
5️⃣ Server will start at:
    
    http://127.0.0.1:5000

6️⃣ API Usage

    Endpoint
    bash
    Copy code
    POST /predict
    
7️⃣ Sample Request
 
     {
         "features": [83, 127001, 127001, 56499]
     }
     
8️⃣ Sample Response
    
    {
     "prediction": 0
    }
    
9️⃣ Prediction Meaning
      
    0 → Normal Traffic
    1 → Malicious Traffic
    
--- 

📸 Screenshots
Screenshots demonstrating:

    1.Wireshark live packet capture
    
    2.TShark terminal capture

    3.Flask backend running

    4.Model prediction response
    
---

🎓 Learning Outcomes 

    1.Understanding network traffic analysis

    2.Applying machine learning to cybersecurity

    3.Building REST APIs with Flask

    4.Integrating ML models into backend systems

----

🔮 Future Improvements

    1.Web-based dashboard frontend

    2.Multi-class attack detection

    3.Automated feature extraction

    4.Cloud deployment












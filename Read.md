# 🚀 NASA C-MAPSS: Predictive Modeling for Intelligent Maintenance  
🔬 **Machine Learning | Predictive Maintenance | Aerospace Engineering**

![GitHub Repo Size](https://img.shields.io/github/repo-size/seu-usuario/NASA-CMAPSS-Predictive-Maintenance?color=blue)  
![GitHub Contributors](https://img.shields.io/github/contributors/seu-usuario/NASA-CMAPSS-Predictive-Maintenance)  
![GitHub License](https://img.shields.io/github/license/seu-usuario/NASA-CMAPSS-Predictive-Maintenance)  
![GitHub Last Commit](https://img.shields.io/github/last-commit/seu-usuario/NASA-CMAPSS-Predictive-Maintenance)  

## 📌 Overview  
**This project aims to predict the Remaining Useful Life (RUL) of aircraft engines** using machine learning models trained on the **NASA C-MAPSS dataset**. The goal is to develop a predictive maintenance system that enhances reliability and reduces maintenance costs.  

✅ **Comparison of Machine Learning Models:**  
- **Random Forest Regressor (Optimized)**  
- **XGBoost Regressor (Optimized)**  
- **Model Performance Evaluation (MAE, MSE, RMSE)**  
- **Best Model: Random Forest**  

🚀 **Why this project matters?**  
Predictive maintenance is **crucial in aerospace engineering** to prevent catastrophic failures and optimize the lifecycle of engines.  

---

## 📊 Results: Model Performance Comparison  
| **Model**        | **MAE** | **MSE** | **RMSE** |
|-----------------|--------|--------|--------|
| **Random Forest** | **29.63** | **1717.07** | **41.44** |
| **XGBoost**       | 30.58  | 1841.14 | 42.91 |

📈 **Final Decision:** The **Random Forest model performed better** in predicting engine RUL.  

---

## 🏗️ Project Structure  
```
📂 NASA-CMAPSS-Predictive-Maintenance
│── 📂 data                 # Dataset files (optional)
│── 📂 models               # Trained models
│── 📂 notebooks            # Jupyter Notebooks
│── 📂 src                  # Source code
│   │── 📜 data_preprocessing.py  # Data cleaning and preparation
│   │── 📜 feature_engineering.py  # Feature selection and transformation
│   │── 📜 train_model.py          # Model training
│   │── 📜 evaluate_model.py       # Model evaluation
│   │── 📜 inference.py            # Predict RUL for new data
│── 📂 reports              # Documentation and reports
│── 📜 README.md            # Project documentation
│── 📜 requirements.txt      # Dependencies
│── 📜 LICENSE              # License
│── 📜 .gitignore           # Ignore unnecessary files
```

---

## 🖥️ How to Run  
Clone the repository and install dependencies:  
```bash
git clone https://github.com/seu-usuario/NASA-CMAPSS-Predictive-Maintenance.git
cd NASA-CMAPSS-Predictive-Maintenance
pip install -r requirements.txt
```

Run the **Jupyter Notebook**:  
```bash
jupyter notebook
```

To train the **Random Forest model**, execute:
```bash
python src/train_model.py
```

To evaluate the model:
```bash
python src/evaluate_model.py
```

---

## ⚙️ Technologies Used  
- **Python 3.9+**  
- **Pandas, NumPy, Matplotlib, Seaborn** (EDA)  
- **Scikit-Learn** (Machine Learning)  
- **XGBoost** (Gradient Boosting)  
- **Joblib** (Model Saving)  

---

## 📌 Key Insights  
✔ **Feature Engineering Improved Model Performance**  
✔ **Removing Redundant Sensors Helped Reduce Overfitting**  
✔ **Random Forest Performed Better Than XGBoost for This Dataset**  
✔ **Future Work: Implement LSTM for Time-Series Forecasting**  

---

## 🔮 Next Steps  
✅ **Experiment with Deep Learning (LSTM, CNNs)**  
✅ **Deploy the Model via API for Real-time Predictions**  
✅ **Test with Other NASA Datasets for Generalization**  

---

## 🤝 Contributing  
Contributions are welcome! If you want to improve the project, follow these steps:  
1. **Fork** the repository.  
2. Create a **new branch** (`git checkout -b feature-branch`).  
3. Make changes and **commit** (`git commit -m "New feature added"`).  
4. Push the changes (`git push origin feature-branch`).  
5. Open a **Pull Request**.  

---

## 📜 License  
This project is licensed under the **MIT License**.  

---

## 📬 Contact  
If you have any questions or suggestions, feel free to reach out:  
📧 **Email:** cesar.ronai@hotmail.com  
🔗 **LinkedIn:** [Cesar Ronai](https://linkedin.com/in/cesar-ronai)  

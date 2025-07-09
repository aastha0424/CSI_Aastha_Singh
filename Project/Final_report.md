# 🎓 Student Performance Prediction Using Regression

This project predicts students' final exam scores (G3) based on their previous academic records, study habits, and personal attributes. The goal is to help educators identify students who may need extra support before their final exams.

---

## 📊 Exploratory Data Analysis (EDA)

Extensive EDA was conducted on the dataset `student-por.csv`:

- ✅ Inspected data shape, structure, and column types.
- ✅ Checked for missing values and data imbalances.
- ✅ Visualized distributions of key numeric features like `G1`, `G2`, `studytime`, `absences`, and `failures`.
- ✅ Used correlation matrix and heatmaps to identify relationships.
- ✅ Detected outliers using boxplots.
- ✅ Evaluated impact of categorical features like `schoolsup`, `internet`, and `sex` on `G3`.

---

## 🔢 Regression Modeling

Six regression models were trained and evaluated:

| Model              | RMSE     | R² Score |
|-------------------|----------|----------|
| Linear Regression | 1.1557   | 0.8630   |
| Ridge Regression  | 1.1558   | 0.8630   |
| Random Forest     | 1.3009   | 0.8265   |
| Decision Tree     | 1.4060   | 0.7973   |
| Lasso Regression  | 1.4240   | 0.7920   |
| ElasticNet        | 1.4833   | 0.7744   |

- ✅ Feature selection included: `G1`, `G2`, `studytime`, `failures`, `absences`, `Medu`, `Fedu`, `sex`, `schoolsup`, `internet`.
- ✅ Preprocessing: Standard scaling + One-hot encoding.
- ✅ Performed 5-fold cross-validation on Linear Regression.
- ✅ Explored polynomial features to improve model performance.

---

## 🚀 Streamlit Web App

An interactive app was built using [Streamlit](https://streamlit.io/) that allows users to input student attributes and receive a predicted final grade instantly.

### 📷 App Screenshot:
![Streamlit UI Screenshot](Project\screenshots\streamlit_ui.png.png) 

---

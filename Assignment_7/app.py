import streamlit as st
import numpy as np
import pickle
import seaborn as sns
import matplotlib.pyplot as plt

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Class labels for iris
classes = ['Setosa', 'Versicolor', 'Virginica']

# App title
st.title("🌼 Iris Flower Classifier")
st.markdown("Use the sliders below to input flower measurements:")

# Input sliders
sepal_length = st.slider('Sepal Length (cm)', 4.0, 8.0, 5.8)
sepal_width = st.slider('Sepal Width (cm)', 2.0, 4.5, 3.0)
petal_length = st.slider('Petal Length (cm)', 1.0, 7.0, 4.0)
petal_width = st.slider('Petal Width (cm)', 0.1, 2.5, 1.2)

# Predict
input_features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = model.predict(input_features)[0]
probs = model.predict_proba(input_features)[0]

# Show prediction
st.subheader(f"🌟 Predicted Species: **{classes[prediction]}**")

# Show probabilities
st.write("🔍 Prediction Confidence:")
fig, ax = plt.subplots()
sns.barplot(x=classes, y=probs, palette="pastel", ax=ax)
ax.set_ylabel("Probability")
ax.set_ylim(0, 1)
st.pyplot(fig)

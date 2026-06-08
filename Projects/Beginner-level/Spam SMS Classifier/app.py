import streamlit as st
import pickle

model = pickle.load(open('model.pk1', 'rb'))
vectorizer = pickle.load(open('vectorizer.pk1', 'rb'))

st.title("SMS Spam Detector")

message = st.text_area("Enter SMS Message")

if st.button("Predict"):
    transformed = vectorizer.transform([message])
    result = model.predict(transformed)[0]

    if result == 1:
        st.error("Spam Message")
    else:
        st.success("Not Spam")
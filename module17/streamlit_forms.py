import streamlit as st


with st.form("my_form",clear_on_submit=True):
    name = st.text_input('Name')
    age = st.slider('age',min_value=0, max_value=100)
    email = st.text_input('Email')
    biography = st.text_area('Shor bio')
    terms = st.checkbox('i agree to the terms and conditions')

    submit_buton = st.form_submit_button(label='submit')

if submit_buton:
    st.write(f"Name: {name}")
    st.write(f"age: {age}")
    st.write(f"Emain: {email}")
    st.write(f"Short bio: {biography}")

    if terms:
        st.write('you agreed to the terms and conditions')
    else:
        st.write('you did not agree to the terms and conditions')
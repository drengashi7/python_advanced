import streamlit as st

def main():
    st.title("hello world")
    st.button("click hear")
    if st.button("click me"):
        st.write("button clicked")

    if st.checkbox("click"):
        st.write("jes")

    user_input = st.text_input("enter text","sample")
    st.write("you wrote:", user_input)
    age = st.number_input("enter yout age",min_value=0,max_value=100)
    st.write(f"your age is:{age}")
    message = st.text_area("enter a message")
    st.write(f"your message: {message}")
    choice = st.radio("pick one", ["choice 1","choice 2","choice 3"])
    if st.button("Success"):
        st.button("Operation was successful")

    try:
        1/0
    except Exception as e:
        st.expectation(e)


if __name__ == "__main__":
    main()
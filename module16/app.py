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


if __name__ == "__main__":
    main()
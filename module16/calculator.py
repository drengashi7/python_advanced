import streamlit as st

def calculator(num1, num2, operation):
    if operation == "Addition":
        result = num1 + num2

    elif operation == "Substration":
        result = num1 - num2

    elif operation == "Multiplication":
        result = num1  * num2

    elif operation == "Division":
        try:
            result = num1  / num2
        except ZeroDivisionError:
            result = "Cannot devide by zero"

    return result

def main():
    st.title("simple calculator")

    num1 = st.number_input("enter the first number",step=1)

    num2 = st.number_input("enter the second number",step=1)

    operation = st.radio("select operation",["Addition","Substraction","Multiplication","Division"])

    result = calculator(num1, num2, operation)

    st.write(f"result of the {operation} of {num1} is: {result}")

if __name__ == "__main__":
    main()
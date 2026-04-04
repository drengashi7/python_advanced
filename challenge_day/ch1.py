from abc import ABC, abstractmethod
import streamlit as st

class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        bmi = self.calculate_bmi()
        category = self.get_bmi_category()
        print(f"\nName: {self.name}")
        print(f"Age: {self.age}")
        print(f"BMI: {bmi:.2f}")
        print(f"Category: {category}")


class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 24.9:
            return "Normal weight"
        elif bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"


class Child(Person):
    def calculate_bmi(self):
        return (self.weight / (self.height ** 2)) * 1.3# adjustment

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 14:
            return "Underweight"
        elif bmi < 18.5:
            return "Normal weight"
        elif bmi < 24.9:
            return "Overweight"
        else:
            return "Obese"



# name = input("Enter name: ")
# age = int(input("Enter age: "))
# weight = float(input("Enter weight (kg): "))
# height = float(input("Enter height (m): "))
#
# if age >= 18:
#     person = Adult(name, age, weight, height)
# else:
#     person = Child(name, age, weight, height)
#
# person.print_info()

st.title("BMI Calculator")

name = st.text_input("Enter name")
age = st.number_input("Enter age", min_value=0)
weight = st.number_input("Enter weight (kg)", min_value=0.0)
height = st.number_input("Enter height (m)", min_value=0.0)

if st.button("Calculate BMI"):
    if age == 0 or weight == 0 or height == 0:
        st.warning("Please fill all fields with valid values.")
    else:
        if age >= 18:
            person = Adult(name, age, weight, height)
        else:
            person = Child(name, age, weight, height)

        bmi = person.calculate_bmi()
        category = person.get_bmi_category()

        st.subheader("Result")
        st.write(f"Name: {name}")
        st.write(f"Age: {age}")
        st.write(f"BMI: {bmi:.2f}")
        st.write(f"Category: {category}")
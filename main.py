# this is a mental health UI for predicting the depression scenario of the working professionals and students
# we will eventually make a page which will take multiple features(18 to be precise)

# Features for evaluation
'''
Gender	, Age	, City	,
Working Professional or Student,
Profession	,
Academic Pressure	,
Work Pressure	,
CGPA	,
Study Satisfaction	,
Job Satisfaction	,
Sleep Duration	,
Dietary Habits	,
Degree	,
Have you ever had suicidal thoughts ?	,
Work/Study Hours,	
Financial Stress	,
Family History of Mental Illness	,
---------------
| Depression  |--> output
---------------
'''

# importing necessary libraries
import pandas as pd
import streamlit as st


# background theme definition with css
mental_health_bg = '''
<style>
[data-testid="stAppViewContainer"]{
background-color: #005aff;
opacity: 0.8;
background-image: radial-gradient(circle at center center, #000000, #005aff), repeating-radial-gradient(circle at center center, #000000, #000000, 40px, transparent 80px, transparent 40px);
background-blend-mode: multiply;
}
</style>
'''


# here the user session handles the class and the login webpage
class UserSession:
    def __init__(self):
        self.is_logged_in = False

    def login(self, username, password):
        # Placeholder for actual login logic
        if username == "root" and password == "passwd":
            self.is_logged_in = True
            return True
        return False

# login page
def main():
    st.title(":blue[Evaluate] _Your_ :grey[Mental Health] ")

    # Initialize session state for login status
    if 'is_logged_in' not in st.session_state:
        st.session_state.is_logged_in = False

    session = UserSession()

    # User login input
    if not st.session_state.is_logged_in:
        username = st.text_input("Username",placeholder="root")
        password = st.text_input("Password", type="password", placeholder="passwd")

        # Login button
        if st.button("Login"):
            if session.login(username, password):
                st.session_state.is_logged_in = True
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Just copy the placeholder DumpSHIT!!")
    else:
        Main_Page()


# Parameters definition and compilation
def param_user_input():
    # Basic Info
    Name = st.text_input("Your Name : ")
    gender = st.selectbox("Your Gender : ",
                          ("Male","Female"))
    Age = st.text_input(f"Your Age : ",min_val=1, format="%d")
    City = st.text_input("Your City : ")

    # identifying whether a student or working professional ?
    Work_student = st.selectbox("Are you a Working Professional or a Student : ",
                                ("Working Professional","Student",))
    Profession = st.text_input("Your Profession : ")
    Academic_Pressure = st.text_input("Your Academic Pressure : ")
    Work_Pressure = st.text_input("Your Work Pressure : ")
    work_study_hours = st.text_input("How many hours do you work or study in a day on average : ")
    Degree = st.text_input("Your Degree : ")
    CGPA = st.text_input("Your CGPA : ")

    # personally satisfaction?
    Satisfaction = st.text_input("Your Satisfaction : ")
    Job_Satisfaction = st.text_input("Your Job Satisfaction : ")

    # maintaining your health or not?
    Dietary_Habits = st.text_input("Your Dietary Habits : ")
    Sleep_Duration = st.text_input("Your Sleep Duration : ")
    Suicidal_tendencies = st.text_input("Have you ever had Suicidal Thoughts Recently : ")
    financial_stress = st.text_input("Do You have financial Stress : ")
    family_history = st.text_input("Do you have family history of any kind of mental health related Issues: ")


# Main Page and all items
def Main_Page():

    # applying the bg to the webpage
    st.markdown(mental_health_bg, unsafe_allow_html=True)

    # Add more Streamlit functions below
    st.write("Mental Health Is a very important aspect in our life, \
    though it is just a thought all the imagination and wonders and the world \
    that we believe lies in our very head or it is better to say in our mind therefore it \
    is also important for us to take care of our mental health as we look after our \
    physical fitness.")







if __name__ == "__main__":
    main()




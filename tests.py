import streamlit as st

st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("This is a header with a divider", divider="gray")
st.header("These headers have rotating dividers", divider=True)
st.header("One", divider=True)
st.header("Two", divider=True)
st.header("Three", divider=True)
st.header("Four", divider=True)


# Initialize session state to store inputs
if 'responses' not in st.session_state:
    st.session_state['responses'] = []

# Function to display a set of questions and collect answers
def ask_questions(questions):
    responses = []
    for question in questions:
        q_type = question['type']
        q_text = question['text']
        if q_type == 'yes_no':
            response = st.radio(q_text, ['Yes', 'No'])
        elif q_type == 'text':
            response = st.text_input(q_text)
        elif q_type == 'level':
            response = st.selectbox(q_text, range(1, 6))
        elif q_type == 'float':
            response = st.slider(q_text, 0.0, 10.0, step=0.1)
        elif q_type == 'integer':
            response = st.number_input(q_text, format='%d', step=1)
        elif q_type == 'float_or_integer':
            response = st.number_input(q_text, format='%f')
        responses.append(response)
    return responses

# Define sets of questions
set1 = [
    {'type': 'yes_no', 'text': 'Do you like Python?'},
    {'type': 'text', 'text': 'What is your favorite programming language?'}
]

set2 = [
    {'type': 'level', 'text': 'Rate your satisfaction with our service (1-5)'},
    {'type': 'float', 'text': 'Enter a value between 0.0 to 10.0'}
]

# Display the first set of questions and store responses
if 'set1_completed' not in st.session_state:
    responses = ask_questions(set1)
    if st.button("Next"):
        st.session_state['responses'].extend(responses)
        st.session_state['set1_completed'] = True

# Display the second set of questions and store responses
if 'set1_completed' in st.session_state and 'set2_completed' not in st.session_state:
    responses = ask_questions(set2)
    if st.button("Finish"):
        st.session_state['responses'].extend(responses)
        st.session_state['set2_completed'] = True

# Display all stored responses
if 'set2_completed' in st.session_state:
    st.write("All responses:", st.session_state['responses'])

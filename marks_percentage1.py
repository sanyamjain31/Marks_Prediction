import streamlit as st

st.header("Welcome")
st.text("Please Enter Your Marks According To Your Subject Out of 100")

with st.form(key="marks_percentage1"):
    name = st.text_input(label="Enter Your Name ")
    clas = st.text_input(label="Enter Your Class ")
    age = st.slider(label="Enter Your Age ", min_value=0, max_value=21)
    roll_num = st.text_input(label="Enter Your Roll Number ")
    maths = st.slider(label="Enter The Marks Of Maths ", min_value=0, max_value=100)
    bio = st.slider(label="Enter The Marks Of Bio ", min_value=0, max_value=100)
    chemistry = st.slider(label="Enter The Marks OF Chemistry", min_value=0, max_value=100)
    physics = st.slider(label="Enter The Marks Of Physics", min_value=0, max_value=100)
    english = st.slider(label="Enter The Marks Of English", min_value=0, max_value=100)
    submit = st.form_submit_button(label="Submit")
    sum_all = maths + bio + chemistry + physics + english
    percentage = (sum_all / 500) * 100
    if percentage >= 35:
        result = " Pass "
    else:
        result = " Fail "
    if sum_all == 495:
        grade = " A+ "
        remark = "Excellent"
    elif sum_all >= 480:
        grade = " A1 "
        remark = "Excellent"
    elif sum_all >= 450:
        grade = " A2 "
        remark = "Very Nice"
    elif sum_all >= 400:
        grade = " B1 "
        remark = "Nice"
    elif sum_all >= 350:
        grade = " B2 "
        remark = "Good"
    elif sum_all >= 300:
        grade = " C "
        remark = "Need Improvement"
    else:
        grade = " D "
    st.write("Student's Name :  ", name)
    st.write("Student's Class :  ", clas)
    st.write("Student's Age :  ", age)
    st.write("Student's Roll Number :  ", roll_num)
    st.write("Total Marks Obtained By The Student :  ", sum_all)
    st.write("Total Percentage Of The Student :  ", percentage, " %")
    st.write("Your Overall Result :  ", result)
    st.write("Your Grade :  ", grade)
    st.write("Remark By Class Teacher :  ", remark)

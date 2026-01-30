import streamlit as st

st.set_page_config(page_title="Student Result Manager", page_icon="🎓")

st.title("🎓 Student Result Manager")
st.write("Enter student details to generate result")

name = st.text_input("Student Name")

col1, col2, col3 = st.columns(3)

with col1:
    math = st.number_input("Math Marks", min_value=0, max_value=100)
with col2:
    english = st.number_input("English Marks", min_value=0, max_value=100)
with col3:
    science = st.number_input("Science Marks", min_value=0, max_value=100)

if st.button("Generate Result"):
    if name == "":
        st.warning("Please enter student name")
    else:
        total = math + english + science
        percentage = total / 3

        if percentage >= 80:
            grade = "A+"
        elif percentage >= 70:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "Fail"

        st.success("Result Generated Successfully ✅")

        st.subheader("📄 Student Result")
        st.write(f"👤 **Name:** {name}")
        st.write(f"📊 **Total Marks:** {total}")
        st.write(f"📈 **Percentage:** {percentage:.2f}%")

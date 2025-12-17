import streamlit as st

st.title("📊 Student Percentage & Grade Calculator")

# Step 1: Ask for the number of subjects
num_subjects = st.number_input(
    "Enter the number of subjects", min_value=1, value=5, step=1
)

# Step 2: Collect marks for each subject
marks = []
for i in range(1, num_subjects + 1):
    mark = st.number_input(
        f"Marks for Subject {i}", min_value=0.0, max_value=100.0, step=0.1, key=f"m{i}"
    )
    marks.append(mark)

# Step 3: Calculate when user clicks the button
if st.button("Calculate Percentage & Grade"):

    if len(marks) != num_subjects:
        st.error("Please enter all marks.")
    else:
        total = sum(marks)
        max_total = num_subjects * 100
        percentage = (total / max_total) * 100

        # Determine grade
        if percentage >= 90:
            grade = "A"
        elif percentage >= 80:
            grade = "B"
        elif percentage >= 70:
            grade = "C"
        elif percentage >= 60:
            grade = "D"
        else:
            grade = "F"

        # Display results
        st.write(f"**Total Marks:** {total} / {max_total}")
        st.write(f"**Percentage:** {percentage:.2f}%")
        st.write(f"**Grade:** {grade}")

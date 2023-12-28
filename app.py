import streamlit as st

def main():
    st.image("https://sulookfoundationtst.blob.core.windows.net/sulook/My new creation.png", width=150)  
    st.title("Sulook Matrimonial | Pakistan")
    st.markdown("Please fill the form below to register your profile with Sulook Matrimonial Services. We will contact you shortly after reviewing your profile.")

    with st.form(key='my_form'):
        st.header("Matrimonial Profile")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Widowed"])
        name = st.text_input("Name")
        dob = st.date_input("DOB (Date of Birth)")
        age = st.number_input("Age", min_value=18, max_value=100)
        height = st.text_input("Height(Feet,Inches)")
        caste = st.text_input("Caste")
        sect = st.text_input("Sect")
        religion = st.text_input("Religion")
        nationality = st.text_input("Nationality")

        st.header("Qualifications")
        education = st.text_input("Education")
        job = st.text_input("Job")
        salary = st.number_input("Salary (Optional)", min_value=0)

        st.header("Family")
        father_info = st.text_input("Father’s Education ")
        mother_info = st.text_input("Mother’s Education ")
        father_profession = st.text_input("Father's Profession")
        mother_profession = st.text_input("Mother’s Profession")
        brothers = st.number_input("Brothers", min_value=0)
        sisters = st.number_input("Sisters", min_value=0)

        st.header("Residence")
        city = st.text_input("City")
        area = st.text_input("Area")
        residence_size = st.text_input("Size of residence(Marlas)")

        st.header("Requirements")
        age_limit = st.number_input("Age Limit", min_value=18, max_value=100)
        residence_type = st.selectbox("Residence (Owned/Rent)", ["Owned", "Rent"])
        req_city = st.text_input("City of Match")
        req_caste = st.text_input("Caste of Match")
        qualification = st.text_input("Qualification of Match")
        income = st.number_input("Income of Match", min_value=0)
        req_sect = st.text_input("Sect of Match")

        st.header("Contact Number")
        contact_person = st.text_input("Contact Number of Responsible Person")
        contact_person_relation = st.selectbox("Responsible Person", ["Father", "Mother", "Brother", "Sister", "Other"])

        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            # The form has been submitted, you can now use the variables to collect the data
            print(f"Age Limit: {age_limit}")
            print(f"Residence Type: {residence_type}")
            print(f"City of Match: {req_city}")
            print(f"Caste of Match: {req_caste}")
            print(f"Qualification of Match: {qualification}")
            print(f"Income of Match: {income}")
            print(f"Sect of Match: {req_sect}")
            print(f"Contact Person: {contact_person}")
            print(f"Contact Person Relation: {contact_person_relation}")
if __name__ == "__main__":
    main()
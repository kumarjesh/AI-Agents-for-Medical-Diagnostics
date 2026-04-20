import streamlit as st
from Utils.Agents import Cardiologist, Psychologist, Pulmonologist, MultidisciplinaryTeam

# Set up the page layout
st.set_page_config(page_title="AI Medical Diagnostics", page_icon="🩺", layout="wide")

st.title("🩺 AI Medical Diagnostics Team")
st.write("Enter patient data below to generate a comprehensive, multidisciplinary medical report.")

# Text area for patient data input
patient_data = st.text_area(
    "Patient Data / Symptoms / History:", 
    height=200, 
    placeholder="E.g., Patient is a 45-year-old male complaining of chest tightness, shortness of breath, and severe anxiety..."
)

# The action button
if st.button("Generate Diagnosis", type="primary"):
    if not patient_data.strip():
        st.warning("Please enter some patient data first.")
    else:
        # Create a visual loading container
        with st.status("Consulting the Medical Team...", expanded=True) as status:
            
            st.write("👨‍⚕️ Cardiologist is reviewing the case...")
            cardio_agent = Cardiologist(patient_data)
            cardio_report = cardio_agent.run()
            
            st.write("🧠 Psychologist is reviewing the case...")
            psych_agent = Psychologist(patient_data)
            psych_report = psych_agent.run()
            
            st.write("🫁 Pulmonologist is reviewing the case...")
            pulmo_agent = Pulmonologist(patient_data)
            pulmo_report = pulmo_agent.run()
            
            st.write("🏥 Multidisciplinary Team is synthesizing the final report...")
            team_agent = MultidisciplinaryTeam(
                cardiologist_report=cardio_report,
                psychologist_report=psych_report,
                pulmonologist_report=pulmo_report
            )
            final_diagnosis = team_agent.run()
            
            status.update(label="Diagnosis Complete!", state="complete", expanded=False)

        # Display the Final Diagnosis prominently at the top
        st.subheader("📋 Multidisciplinary Final Diagnosis")
        st.success(final_diagnosis)

        st.divider()

        # Display individual reports hidden inside tabs for a clean UI
        st.subheader("🔍 Individual Specialist Reports")
        tab1, tab2, tab3 = st.tabs(["Cardiology", "Psychology", "Pulmonology"])
        
        with tab1:
            st.write(cardio_report)
        with tab2:
            st.write(psych_report)
        with tab3:
            st.write(pulmo_report)
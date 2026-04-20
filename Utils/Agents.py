import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import streamlit as st

# Load local .env file if it exists
load_dotenv()

# Foolproof API Key Routing
try:
    # CLOUD: Try to grab the key directly from Streamlit Secrets
    groq_key = st.secrets["GROQ_API_KEY"]
except Exception:
    # LOCAL: Fallback to your computer's .env file
    groq_key = os.getenv("GROQ_API_KEY")

# Pass the key explicitly to LangChain
llm = ChatGroq(
    api_key=groq_key,
    model="llama-3.1-8b-instant",
    temperature=0.2
)

class Cardiologist:
    def __init__(self, patient_data: str):
        self.patient_data = patient_data
        
    def run(self) -> str:
        print("Cardiologist is running...")
        prompt = PromptTemplate(
            input_variables=["patient_data"],
            template="You are an expert Cardiologist. Review the following patient data and provide your cardiovascular diagnosis and recommendations:\n\n{patient_data}"
        )
        chain = prompt | llm
        try:
            response = chain.invoke({"patient_data": self.patient_data})
            return response.content
        except Exception as e:
            return f"Cardiologist API Error: {str(e)}"

class Psychologist:
    def __init__(self, patient_data: str):
        self.patient_data = patient_data
        
    def run(self) -> str:
        print("Psychologist is running...")
        prompt = PromptTemplate(
            input_variables=["patient_data"],
            template="You are an expert Psychologist. Review the following patient data and provide your psychological assessment and recommendations:\n\n{patient_data}"
        )
        chain = prompt | llm
        try:
            response = chain.invoke({"patient_data": self.patient_data})
            return response.content
        except Exception as e:
            return f"Psychologist API Error: {str(e)}"

class Pulmonologist:
    def __init__(self, patient_data: str):
        self.patient_data = patient_data
        
    def run(self) -> str:
        print("Pulmonologist is running...")
        prompt = PromptTemplate(
            input_variables=["patient_data"],
            template="You are an expert Pulmonologist. Review the following patient data and provide your respiratory diagnosis and recommendations:\n\n{patient_data}"
        )
        chain = prompt | llm
        try:
            response = chain.invoke({"patient_data": self.patient_data})
            return response.content
        except Exception as e:
            return f"Pulmonologist API Error: {str(e)}"

class MultidisciplinaryTeam:
    def __init__(self, cardiologist_report: str, psychologist_report: str, pulmonologist_report: str):
        self.cardio_report = cardiologist_report
        self.psych_report = psychologist_report
        self.pulmo_report = pulmonologist_report
        
    def run(self) -> str:
        print("MultidisciplinaryTeam is running...")
        prompt = PromptTemplate(
            input_variables=["cardio", "psych", "pulmo"],
            template="""You are the lead physician of a Multidisciplinary Medical Team. 
            Synthesize the following specialist reports into a single, cohesive final diagnosis and treatment plan.
            
            Cardiologist's Report:
            {cardio}
            
            Psychologist's Report:
            {psych}
            
            Pulmonologist's Report:
            {pulmo}
            
            Provide the final diagnosis and comprehensive treatment plan below:"""
        )
        chain = prompt | llm
        try:
            response = chain.invoke({
                "cardio": self.cardio_report,
                "psych": self.psych_report,
                "pulmo": self.pulmo_report
            })
            return response.content
        except Exception as e:
            return f"MultidisciplinaryTeam API Error: {str(e)}"

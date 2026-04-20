import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Swap Google for Groq's fast LLaMA 3 model
# Swap the decommissioned model for the active 3.1 version
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2
)

# ... (keep your Cardiologist, Psychologist, etc. classes exactly as they are below this)python -m pip install langchain-groq

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
            print(f"Cardiologist Error: {e}")
            return "Error generating Cardiology report."

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
            print(f"Psychologist Error: {e}")
            return "Error generating Psychology report."

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
            print(f"Pulmonologist Error: {e}")
            return "Error generating Pulmonology report."

class MultidisciplinaryTeam:
    # Fixed the initialization arguments to exactly match what main.py is passing
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
            print(f"MultidisciplinaryTeam Error: {e}")
            return "Error generating Final Diagnosis."

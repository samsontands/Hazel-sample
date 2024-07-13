import streamlit as st
import pandas as pd
import requests
import json

st.set_page_config(page_title="Hazel Tan - CV", page_icon="📊", layout="wide")

def load_cv_data():
    cv_data = {
        "name": "HAZEL TAN",
        "summary": "Student advisor with experience in guiding students to make decisions for their future study and career plans, especially for high school and college students. Excellent time management and professional written and interpersonal communication skills. A dynamic ability to build positive rapport with different populations. Seeking a role in an educational environment to empower individuals to discover their potentials.",
        "skills": [
            "Counselling skills (Individual and group counselling)",
            "Working with diverse population",
            "Team player",
            "Effective communication skills",
            "Relationship building",
            "Analytical and problem solving skills"
        ],
        "education": [
            {
                "degree": "Master of Professional Counselling",
                "institution": "Monash University Malaysia",
                "duration": "Feb 2017 - Nov 2019",
                "details": "Completed the course with CGPA3.6. Taken coursework in Counselling Practice and Theory, Group Counselling Skills and Psychotherapy, Personnel and Career Development Counselling, Cognitive Behaviour Therapy, Children and Adolescents Counselling."
            },
            {
                "degree": "Bachelor of Psychological Science and Business",
                "institution": "Monash University Malaysia",
                "duration": "Feb 2013 - Nov 2016",
                "details": "Majors: Psychology and Economics. Participated in Student Exchange Program to Monash Univeristy Clayton campus for one semester."
            }
        ],
        "experience": [
            {
                "title": "Student Advisor",
                "company": "JM Education, Subang Jaya",
                "duration": "Dec 2019 - present",
                "responsibilities": [
                    "Providing counselling service to prospective students on their further study options, guiding them through visa application to different countries.",
                    "Organized talks for secondary school students (Year 8 to 11) during school breaks.",
                    "Handle students' inquires on various platforms (e.g., WhatsApp, phone calls, Facebook).",
                    "Successfully organized virtual info sessions through online platform - Zoom.",
                    "Run online social media marketing campaigns to collect leads."
                ]
            },
            {
                "title": "Intern Counsellor",
                "company": "Community Health Care Clinic",
                "duration": "Sep 2018 - June 2019",
                "responsibilities": [
                    "Conducted face-to-face counselling sessions for clients who needed emotional support.",
                    "Conducted confidential HIV screening and supporting clients who were in crisis situations."
                ]
            },
            {
                "title": "Intern Counsellor",
                "company": "Segi College, Subang Jaya",
                "duration": "Oct 2018 - Nov 2018",
                "responsibilities": [
                    "Conducted workshop about self-discovery and self-acceptance for students around 18 to 25 years old by using Metaphoric OH-Cards and experiential activities."
                ]
            }
        ],
        "certifications": [
            "Licensed counsellor (KB08731, PA08335)",
            "Metaphoric OH-cards Series Workshop",
            "Certified instructor for Prevention & Relationship Education Program (PREP)"
        ],
        "contact": {
            "mobile": "016-2199 573",
            "email": "thx1108@gmail.com"
        }
    }
    return cv_data

def display_cv():
    cv_data = load_cv_data()
    
    st.title(cv_data["name"])
    st.write(cv_data["summary"])
    
    st.header("Skills")
    for skill in cv_data["skills"]:
        st.write(f"- {skill}")
    
    st.header("Education")
    for edu in cv_data["education"]:
        st.subheader(f"{edu['degree']} - {edu['institution']}")
        st.write(f"{edu['duration']}")
        st.write(edu['details'])
    
    st.header("Work Experience")
    for exp in cv_data["experience"]:
        st.subheader(f"{exp['title']} - {exp['company']}")
        st.write(f"{exp['duration']}")
        for resp in exp['responsibilities']:
            st.write(f"- {resp}")
    
    st.header("Certifications")
    for cert in cv_data["certifications"]:
        st.write(f"- {cert}")
    
    st.header("Contact Information")
    st.write(f"Mobile: {cv_data['contact']['mobile']}")
    st.write(f"Email: {cv_data['contact']['email']}")

def get_groq_response(prompt, system_prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {st.secrets['GROQ_API_KEY']}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 150
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()['choices'][0]['message']['content']

def ask_me_anything():
    st.title("Ask Me Anything")
    st.write("Ask a question to get a brief response about Hazel's background, skills, or experience.")
    
    system_prompt = """
    You are an AI assistant representing Hazel Tan. Answer questions about Hazel's background, skills, and experience based on her CV. Keep responses concise and professional. If you're unsure about any information, state that it's not specified in the CV.
    """
    
    user_question = st.text_input("What would you like to know about Hazel?")
    if user_question:
        with st.spinner('Getting a quick answer...'):
            response = get_groq_response(user_question, system_prompt)
        st.write(response)
    st.caption("Note: Responses are kept brief. For more detailed information, please refer to the CV page.")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["CV", "Ask Me Anything"])
    
    if page == "CV":
        display_cv()
    elif page == "Ask Me Anything":
        ask_me_anything()

if __name__ == "__main__":
    main()

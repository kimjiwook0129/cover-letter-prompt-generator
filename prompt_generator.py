import json
import time
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama
from prompts import *
from utils.data_process import load_data, save_data
from datetime import datetime



FILEDIR = "data.json"
DATA = load_data(FILEDIR)

st.set_page_config(page_title = "Cover Letter", page_icon = "📄")
st.markdown("""# Cover Letter Prompt Generator""", unsafe_allow_html = True)


with st.sidebar:
    with st.form(key='info_form'):

        name = st.text_input(label="Name:", value = DATA["name"] if "name" in DATA else "")
        email = st.text_input(label="Email:", value = DATA["email"] if "email" in DATA else "")
        address1 = st.text_input(label="Address (Street):", value = DATA["address1"] if "address1" in DATA else "")
        address2 = st.text_input(label="Address (City, Province, Postal):", value = DATA["address2"] if "address2" in DATA else "")
        phone = st.text_input(label="Phone:", value = DATA["phone"] if "phone" in DATA else "")
        
        
        info_submit_button = st.form_submit_button(label='Update & Save')

        if info_submit_button:
            message_container = st.empty()
            
            try:
                info_to_update = {
                    "name": name, "email": email, "address1": address1,
                    "address2": address2, "phone": phone, 
                }

                save_data(info_to_update, FILEDIR)
                message_container.success("Information Updated!")
            except:
                message_container.error("Failed to Update.")
            time.sleep(1.5)
            message_container.empty()
            
    



with st.form(key='pasting_text'):
    col1, col2, col3 = st.columns([5, 5, 3])
    
    with col1:
        position = st.text_input(
            label="Job Title:"
        )
    with col2:
        company = st.text_input(
            label="Company:"
        )
    with col3:
        selected_date = st.date_input(
            "Date Applying:",
            value=datetime.now(),
            min_value=datetime(2000, 1, 1),
            max_value=datetime(2100, 12, 31)
        )

    upload_resume = st.checkbox(
            label="Resumé?",
            value=True
        )

    job_description = st.text_area(
        label="Job Description:",
        height = 300
    )
    
    submit_button = st.form_submit_button(label='Submit')


if submit_button:
    if not (position and company and job_description):
        st.error("Provide position, company, and job description")
    else:
        position, company = position.title(), company.title()
        
        # llm = ChatOllama(model = "llama3", temperature = 0.1)
        # prompt = ChatPromptTemplate.from_template(COVER_LETTER_PROMPT)

        cover_letter_prompt = COVER_LETTER_PROMPT.format(
            position=position,
            company=company,
            email = email,
            phone = phone,
            date_applying = selected_date,
            applicant_name = name, 
            job_description = job_description,
            address_street = address1,
            address_city = address2,
            resume_attached = RESUME_ATTACHED_SUBPROMPT if upload_resume else ""
        )

        st.write(cover_letter_prompt)
    
    

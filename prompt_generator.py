import streamlit as st
from prompts import *
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="Cover Letter", page_icon="📄")
st.markdown("""# Cover Letter Prompt Generator""", unsafe_allow_html=True)

# Sidebar form for user information (no submit button here)
with st.sidebar:
    name = st.text_input(label="Name:")
    email = st.text_input(label="Email:")
    address1 = st.text_input(label="Address (Street):")
    address2 = st.text_input(label="Address (City, Province, Postal):")
    phone = st.text_input(label="Phone:")

# Form for job details
with st.form(key='pasting_text'):
    col1, col2, col3 = st.columns([5, 5, 3])
    
    with col1:
        position = st.text_input(label="Job Title:")
    with col2:
        company = st.text_input(label="Company:")
    with col3:
        selected_date = st.date_input(
            "Date Applying:", value=datetime.now(),
            min_value=datetime(2000, 1, 1), max_value=datetime(2100, 12, 31)
        )

    upload_resume = st.checkbox(label="Resumé? (Upload your resumé on GPT if checked along with the generated prompt.)", value=True)
    character_limit = st.number_input(
        label="Character limit for the cover letter? (Optional)", min_value=0, max_value=10000, value=0
    )
    job_description = st.text_area(label="Job Description:", height=300)
    
    submit_button = st.form_submit_button(label='Submit')

# Generate cover letter prompt
if submit_button:
    if not (position and company and job_description):
        st.error("Provide position, company, and job description")
    else:
        cover_letter_prompt = COVER_LETTER_PROMPT.format(
            position=position.title(),
            company=company.title(),
            email=email,
            phone=phone,
            date_applying=selected_date,
            applicant_name=name,
            job_description=job_description,
            address_street=address1,
            address_city=address2,
            resume_attached=RESUME_ATTACHED_SUBPROMPT if upload_resume else "",
            character_limit_statement=CHARACTER_LIMIT_SUBPROMPT.format(character_limit=character_limit) if character_limit > 0 else ""
        )
        st.write(cover_letter_prompt)

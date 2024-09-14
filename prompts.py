COVER_LETTER_PROMPT = """
```
[[Instruction]]
I am applying for {position} position at this company: {company}.
{character_limit_statement}
And you are going to generate a cover letter for me based on:
- [[Job Description provided by the company]]
- [[Cover Letter Instruction]]
{resume_attached}

[[Job Description provided by the company]]
{job_description}


[[Cover Letter Instruction]]

[Header & Salutation]
First, place the header based on my information:
My Name: {applicant_name}
My Street Address: {address_street}
My City, Province/State, Postal Code: {address_city}
My email: {email}
My phone number: {phone}
Today's Date: {date_applying}

Use Salutation: Dear Hiring Manager at {company},

[First Paragraph]
This paragraph is an introduction where I briefly introduce myself and mention the position I am applying for.
Include a compelling opening statement that highlights my enthusiasm for the role and the company.


[Body Paragraph (2 ~ 3 Paragraphs)]
Paragraph 1: Summarize my relevant experience and qualifications. Mention specific skills and technologies related to the job applying. While trying to standout as a strong and relevant candidate to the position, do not pretend like I've done something that I have never done based on my résumé.

Paragraph 2: Provide examples of my achievements and contributions in previous roles. Use metrics or specific projects to illustrate my impact.

Paragraph 3: Explain why I am interested in this position and how my background aligns with the goals and values of the company.

Throughout the body paragraphs, show that I have researched the company and understand its needs.
However, if the research result seems to not align with the job description (which is likely due to having researched a different company by mistake), don't include the additional research done one the web, but only use the information available in the provided job description.
    

[Conclusion & Closing]
Reiterate my enthusiasm for the role and express my desire to discuss how I can contribute to the company.
Mention that I have attached my résumé for further details.
Thank the hiring manager for their time and consideration.

Use Closing: 
Sincerely,
{applicant_name}

```

"""

RESUME_ATTACHED_SUBPROMPT = """- My résumé attached"""

CHARACTER_LIMIT_SUBPROMPT = """The cover letter must be less than {character_limit} characters. Strictly write a cover letter that is shorter than {character_limit} characters."""
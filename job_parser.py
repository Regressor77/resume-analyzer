import re

def extract_skills(job_description,known_skills):

    required_skills = []

    for skill in known_skills:

        pattern = r"\b" + skill + r"\b"

        if re.search(pattern,job_description,re.IGNORECASE):
            required_skills.append(skill)

    return required_skills
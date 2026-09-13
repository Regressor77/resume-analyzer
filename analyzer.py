import re

def analyze_resume(resume_text, required_skills):
    analysis = {
        "found": [],
        "missing": [],
        "score": 0
    }

    for skill in required_skills:

        pattern = r"\b" + skill + r"\b"

        if re.search(pattern, resume_text, re.IGNORECASE):
            analysis["found"].append(skill)
        else:
            analysis["missing"].append(skill)

    analysis["score"] = int(len(analysis["found"]) / len(required_skills) * 100)

    return analysis
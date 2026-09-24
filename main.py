from analyzer import analyze_resume
from job_parser import extract_skills
from skills import known_skills
from pathlib import Path

resume_path = Path(input("Enter resume file name/path : "))
job_description_path = Path(input("Enter job description file name/path : "))

resume_text = resume_path.read_text()
job_description = job_description_path.read_text()

required_skills = extract_skills(job_description,known_skills)

if not required_skills:
    print("No Recognized Skills Found In The Job Description.")

else:

        analysis = analyze_resume(resume_text,required_skills)

        found_skills = "✓ " + "\n✓ ".join(analysis['found'])
        missing_skills = "✗ " + "\n✗ ".join(analysis['missing'])

        print(f"""
================================
        RESUME ANALYZER
================================

Found skills:
{found_skills}

Missing skills:
{missing_skills}

Match score: {analysis["score"]}%
================================
""")
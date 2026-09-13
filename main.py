from analyzer import analyze_resume

resume_text = input("Enter the resume text : ")

required_skills = ['Python','Git','SQL','Flask','Django']

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
def analyze_text_answers(answers):
    """ Extract interests from behavioral Q&A """
    interests = []
    if "research" in answers.lower():
        interests.append("Research")
    if "ai" in answers.lower() or "ml" in answers.lower():
        interests.append("AI/ML")
    if "web" in answers.lower():
        interests.append("Web Development")
    if "medicine" in answers.lower() or "pharma" in answers.lower():
        interests.append("Medical/Pharma")
    if "finance" in answers.lower():
        interests.append("Finance/Business")
    return interests

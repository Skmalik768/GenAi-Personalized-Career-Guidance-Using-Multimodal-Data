# fusion_model.py
def fuse_modalities(resume_skills, manual_skills, text_interests, confidence):
    """
    Combine resume skills, manual skills (fallback), interests, and audio confidence
    into a single profile string suitable for embedding / LLM prompts.

    Returns:
        profile_text (str), confidence (float)
    """
    # Merge skills: prefer resume_skills if present; otherwise use manual_skills.
    skills_list = []
    if resume_skills:
        skills_list.extend([s.strip() for s in resume_skills if s and s.strip()])
    if manual_skills:
        for s in manual_skills:
            s_clean = s.strip()
            if s_clean and s_clean not in skills_list:
                skills_list.append(s_clean)

    skills_text = ", ".join(skills_list) if skills_list else "No explicit technical skills provided"
    interests_text = ", ".join([i.strip() for i in text_interests]) if text_interests else "No stated interests"

    profile_text = f"Skills: {skills_text}. Interests: {interests_text}."

    # Ensure confidence is a float between 0.0 and 1.0; if None, assign default 0.6
    try:
        conf = float(confidence) if confidence is not None else 0.6
    except Exception:
        conf = 0.6

    # Clamp to [0.0, 1.0]
    conf = max(0.0, min(1.0, conf))

    return profile_text, conf

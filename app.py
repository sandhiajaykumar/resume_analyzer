import streamlit as st
from resume_parser import extract_text_from_pdf
from score_calculator import get_score

st.set_page_config(page_title="Resume Analyzer", layout="centered")

st.title("📄 Resume Analyzer - Job Fit Score")
st.write("Upload your resume and paste a job description to see your match score.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description", height=200)

if st.button("Analyze"):
    if uploaded_file and job_description:
        with st.spinner("Analyzing Resume..."):
            resume_data = extract_text_from_pdf(uploaded_file)
            
            if "error" in resume_data:
                st.error(f"Error parsing resume: {resume_data['error']}")
            else:
                score = get_score(resume_data, job_description)
                
                st.success(f"✅ Job Fit Score: {score}%")
                
                st.subheader("Extracted Information:")
                st.write(f"**Name:** {resume_data.get('name', 'Not Found')}")
                st.write(f"**Email:** {resume_data.get('email', 'Not Found')}")
                st.write(f"**Skills:** {', '.join(resume_data.get('skills', []))}")

                if score > 80:
                    st.balloons()
                    st.info("Great match! You are highly suitable for this job.")
                elif score > 50:
                    st.warning("Moderate match. Consider tailoring your resume more.")
                else:
                    st.error("Low match. Revise your resume to align better with the job.")
    else:
        st.warning("Please upload a resume and provide a job description.")

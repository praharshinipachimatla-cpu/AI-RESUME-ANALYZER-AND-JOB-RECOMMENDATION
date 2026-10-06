import streamlit as st
from pypdf import PdfReader
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)
st.title("🤖 AI Resume Generator & Job Recommendation Assistant")
st.write("Upload your resume and find suitable jobs.")
st.sidebar.title("📌 Menu")
option = st.sidebar.selectbox(
    "Choose an option",
    ["Resume Analyzer", "Job Recommendation"]
)
uploaded_file = st.file_uploader(
    "📄 resume.pdf",
    type=["pdf"]
)
if uploaded_file:
    reader = PdfReader(uploaded_file)
    resume_text = ""
    for page in reader.pages:
        resume_text += page.extract_text() or ""
    st.success("Resume uploaded successfully! ✅")
    st.subheader("📋 Resume Content")
    st.text_area("Resume", resume_text, height=300)
    text = resume_text.lower()
    # Find skills
    skills = []
    for skill in [
        "python", "java", "c", "c++", "sql",
        "html", "css", "javascript",
        "machine learning", "data analysis",
        "embedded systems", "vlsi"
    ]:
        if skill in text:
            skills.append(skill)
    st.subheader("🛠️ Skills Found")
    st.write(", ".join(skills))
    # Job recommendation
    st.subheader("💼 Suitable Jobs")
    jobs = {
        "Python Developer": ["python"],
        "Data Analyst": ["python", "sql", "data analysis"],
        "Machine Learning Engineer": ["python", "machine learning"],
        "Web Developer": ["html", "css", "javascript"],
        "Embedded Systems Engineer": ["c", "c++", "embedded systems"],
        "VLSI Engineer": ["vlsi", "c"]
    }
    for job, required in jobs.items():
        match = [skill for skill in required if skill in skills]
        if match:
            percentage = int(len(match) / len(required) * 100)
            st.write(
                f"### 💼 {job} — {percentage}% Match"
            )
            st.progress(percentage)

            st.write(
                "Matching skills:",
                ", ".join(match)
            )
else:
    st.info("📄 Upload your resume to get suitable job recommendations.")
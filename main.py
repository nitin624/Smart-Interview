# main.py (Unique & Polished UI)
import streamlit as st
from generator import generate_questions
from fpdf import FPDF
from io import BytesIO
import fitz  # PyMuPDF

# ============ Utility Functions ============

def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    return "".join([page.get_text() for page in doc])

def generate_pdf(questions: list[str]) -> BytesIO:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_title("AI Interview Questions")

    pdf.set_text_color(40, 40, 150)
    pdf.cell(0, 10, "AI-Generated Interview Questions", ln=True, align='C')
    pdf.set_text_color(0, 0, 0)
    pdf.ln(10)

    for idx, question in enumerate(questions, start=1):
        pdf.multi_cell(0, 10, f"{idx}. {question.strip()}", align='L')
        pdf.ln(1)

    pdf_bytes = pdf.output(dest='S').encode('latin-1')
    pdf_stream = BytesIO()
    pdf_stream.write(pdf_bytes)
    pdf_stream.seek(0)
    return pdf_stream

# ============ Streamlit Config ============
st.set_page_config(
    page_title="AI Interview Builder",
    page_icon="🧠",
    layout="wide"
)

# ============ Custom CSS ============
st.markdown("""
<style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        background: linear-gradient(to right, #f0f4ff, #ffffff);
    }
    h1, h2, h3, h4, h5, h6 {
        color: #1a3c6d;
    }
    .stButton>button {
        background-color: #5a78e3;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.5rem 1.2rem;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #445cc2;
    }
    .stDownloadButton>button {
        background-color: #2f9e44;
        color: white;
        border-radius: 8px;
    }
    .stDownloadButton>button:hover {
        background-color: #267a36;
    }
</style>
""", unsafe_allow_html=True)

# ============ Sidebar ============
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4727/4727491.png", width=90)


    st.markdown("<h2 style='margin-top:0;'>🤖 Interview AI</h2>", unsafe_allow_html=True)
    st.write("Leverage AI to prepare for interviews using your resume.")
    st.markdown("---")
    st.info("Upload your resume *(PDF)* or paste the content manually.")
    st.caption("Crafted by Nitin Atude")

# ============ Header ============
st.markdown("<h1 style='text-align: center;'>🧠 AI Interview Question Generator</h1>", unsafe_allow_html=True)
with st.expander("💡 How to Use This App", expanded=False):
    st.markdown("""
    - *Upload your resume* as a PDF or paste your resume text manually.
    - The app uses *AI* to generate 5–10 technical interview questions.
    - You can *download* the questions as a clean PDF.
    - Make sure your resume is detailed with technical skills/projects for better results.
    """)
st.markdown("<p style='text-align:center;font-size:18px;color:#444;'>Generate smart, personalized interview questions instantly based on your resume!</p>", unsafe_allow_html=True)

# ============ Input Section ============
col1, col2 = st.columns(2)
with col1:
    uploaded_pdf = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
with col2:
    resume_text = st.text_area("✍️ Paste Resume Text", height=220, placeholder="Paste your resume content here...")

final_text = ""
if uploaded_pdf:
    final_text = extract_text_from_pdf(uploaded_pdf)
elif resume_text.strip():
    final_text = resume_text.strip()

st.markdown("---")

# ============ Button & Output ============
st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
if st.button("🚀 Generate Interview Questions", use_container_width=True):
    if not final_text:
        st.warning("⚠ Please provide a resume PDF or paste your resume.")
    else:
        with st.spinner("🧠 Processing and generating questions..."):
            try:
                response = generate_questions(final_text)
                questions_list = [q.strip() for q in response.split("\n") if q.strip()]

                if questions_list:
                    st.success("✅ Interview questions ready!")
                    st.markdown("<h4 style='margin-top: 1rem;'>📋 Your Questions:</h4>", unsafe_allow_html=True)
                    with st.expander("View Generated Questions", expanded=True):
                        for idx, q in enumerate(questions_list, 1):
                            st.markdown(f"<p style='margin-bottom:8px;'>{idx}. {q}</p>", unsafe_allow_html=True)

                    st.markdown("---")
                    pdf_file = generate_pdf(questions_list)
                    st.download_button(
                        label="📥 Download PDF",
                        data=pdf_file,
                        file_name="interview_questions.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )
                else:
                    st.warning("⚠ No questions were generated. Please check your resume.")
            except Exception as e:
                st.error(f"❌ Something went wrong:\n`{e}`")
st.markdown("</div>", unsafe_allow_html=True)

# ============ Footer ============
st.markdown("""
---
<p style='text-align: center; font-size: 13px;'> Designed with 💙 by <strong>Nitin Atude</strong>| Powered by Mistral AI </p>
""", unsafe_allow_html=True)

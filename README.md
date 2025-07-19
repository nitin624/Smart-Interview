# 🤖 AI Interview Question Generator

![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> Generate smart, personalized technical interview questions instantly from your resume using Mistral AI.

---

## 🚀 Demo

👉 [Live Demo on Streamlit](https://your-streamlit-link-here.streamlit.app)

---

## 📌 Features

- 📤 Upload your resume as a **PDF**
- ✍️ Or directly **paste** resume text
- ⚡ Uses **Mistral AI API** to generate 5 personalized questions
- 📄 Download generated questions as a **PDF**
- 🎨 Clean & professional UI with gradients and subtle effects
- 🌐 Deploy easily using **Streamlit Cloud**

---

## 📸 Screenshots

| Upload or Paste Resume | AI-Generated Questions |
|------------------------|------------------------|
| ![upload](assets/upload_resume.png) | ![output](assets/generated_questions.png) |

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **PDF Processing:** PyMuPDF (`fitz`), FPDF
- **AI Model:** Mistral API (e.g., `mistral-small`, `mistral-medium`)
- **Deployment:** GitHub + Streamlit Cloud

---

## 🔧 Installation

```bash
git clone https://github.com/your-username/ai-interview-generator.git
cd ai-interview-generator

# Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Set your API key (Mistral)
echo MISTRAL_API_KEY=your_key_here > .env

# Run the app
streamlit run main.py

import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_lottie import st_lottie
import requests

# --- Utility Functions ---
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css():
    st.markdown("""
    <style>
        .stTabs [data-baseweb="tab"] {
            font-size: 18px;
            font-weight: 600;
            padding: 12px 24px;
        }
        .stDownloadButton > button, .stForm button, .contact-button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            transition: all 0.3s ease-in-out;
            text-decoration: none;
            display: inline-block;
            margin-right: 10px;
        }
        .stDownloadButton > button:hover, .stForm button:hover, .contact-button:hover {
            background-color: #2e7d32;
            transform: scale(1.05);
            color: white;
        }
        .contact-row {
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
            margin-top: 10px;
        }
        .fade-in {
            animation: fadeIn 1s ease-in;
        }
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(10px); }
            100% { opacity: 1; transform: translateY(0); }
        }
    </style>
    """, unsafe_allow_html=True)

# --- Load Lottie Assets ---
lottie_urls = {
    "coding": "https://assets2.lottiefiles.com/packages/lf20_tno6cg2w.json",
    "skills": "https://assets4.lottiefiles.com/packages/lf20_jtbfg2nb.json",
    "projects": "https://assets2.lottiefiles.com/packages/lf20_ydo1amjm.json",
    "education": "https://assets4.lottiefiles.com/packages/lf20_yr6zz3wv.json",
    "contact": "https://assets9.lottiefiles.com/packages/lf20_u25cckyh.json"
}
lotties = {key: load_lottie_url(url) for key, url in lottie_urls.items()}

# --- Page Config ---
st.set_page_config(page_title="Madhu Sekhar | AI/ML Portfolio", layout="wide")
local_css()

# --- Load Resume PDF ---
with open("Madhu_Sekhar_Resume.pdf", "rb") as file:
    resume_data = file.read()

# --- Data ---
skills = {
    "Python, Machine Learning": 90,
    "GitHub, Streamlit, Flask, Docker, Kubernetes": 85,
    "HTML, CSS, UI/UX Basics": 80,
    "Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn": 85,
    "Linear Regression, Decision Tree, Random Forest, Logistic Regression": 80
}

education = [
    ("B.Tech", "Electronics & Communication Engineering", "GPCET", "2024"),
    ("Intermediate", "MPC", "Sri Chaitanya Jr College", "2017")
]

projects = [
    ("Zomato Restaurant Rating Prediction", "Built predictive models with real restaurant data, EDA, model evaluation, and visualization."),
    ("Student Grading System", "GUI-based grading system with secure login, course management, and modular design."),
    ("Student Performance Prediction", "Streamlit ML app predicting student scores with real-time visualization and CSV export."),
    ("Tax Calculator", "Interactive tax calculator app for Indian tax regimes with real-time validation and analytics.")
]

# --- Tabs ---
tabs = st.tabs([
    "👤 About Me",         # 0
    "🛠 Skills",           # 1
    "📊 Projects",         # 2
    "🎓 Education",        # 3
    "💼 Experience",       # 4
    "📝 Summary",          # 5
    "📬 Contact"           # 6
])

# --- About Me ---
with tabs[0]:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("Hi, I'm Madhu Sekhar")
        st.subheader("AI/ML Intern | Python | Data Science Enthusiast")
        st.write("""
I’m a passionate Software Engineer with a strong focus on Artificial Intelligence, Machine Learning, Web Development, and Scalable System Design.

I Thrive on transforming complex problems into elegant, data-driven solutions — whether it's crafting intelligent ML models, designing responsive Streamlit dashboards, or developing robust end-to-end applications. With a blend of creativity and precision, I turn ideas into impactful, production-ready systems that solve real-world challenges.

Driven by curiosity and continuous learning, I specialize in building smart, user-centric solutions that bridge the gap between cutting-edge technology and practical implementation.
        """)
        st.download_button("📥 Download Resume", data=resume_data, file_name="Madhu_Sekhar_Resume.pdf", mime="application/pdf")
        st.markdown("""
        <div class="contact-row">
            <a class="contact-button" href="https://mail.google.com/mail/u/0/#inbox">📧 Email</a>
            <a class="contact-button" href="https://www.linkedin.com/in/madhusekharshavala/">🔗 LinkedIn</a>
            <a class="contact-button" href="https://github.com/madhusekhar">💻 GitHub</a>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st_lottie(lotties["coding"], height=280)

# --- Skills ---
with tabs[1]:
    st_lottie(lotties["skills"], height=200)
    for skill, value in skills.items():
        st.write(f"**{skill}**")
        st.progress(value)

# --- Projects ---
with tabs[2]:
    st_lottie(lotties["projects"], height=200)

    with st.expander("📌 Zomato Restaurant Rating Prediction"):
        st.write("""
        Developed an end-to-end machine learning pipeline using **Pandas, Seaborn, and Scikit-learn** to predict restaurant ratings from real-world Zomato dataset.
        - Conducted detailed **Exploratory Data Analysis (EDA)** to understand customer behavior and cuisine preferences.
        - Applied **feature engineering** on categorical and geospatial data (like city, cuisines, location).
        - Trained and evaluated multiple models including **Random Forest** and **Linear Regression**, achieving over **85% accuracy**.
        - Visualized key features affecting restaurant ratings using **Seaborn heatmaps** and **Plotly charts**.
        """)

    with st.expander("📌 Student Grading System"):
        st.write("""
        Created a GUI-based internal tool using **Python and Tkinter**, enabling efficient student grade management for teachers and admins.
        - Integrated **modular OOP design** for better maintainability and scalability.
        - Enabled secure login system for **admin and faculty roles**.
        - Managed subjects, grades, student records with data validation using **NumPy and Pandas**.
        - Future-ready architecture designed to support **ML integration** for automated grading and analytics.
        """)

    with st.expander("📌 Student Performance Prediction"):
        st.write("""
        Developed a **real-time Streamlit application** that predicts student final scores based on attendance and test data.
        - Trained multiple regression models including **Linear, Polynomial, Decision Tree, and Random Forest Regression**.
        - Created interactive **matplotlib and seaborn visualizations** for score trend comparison.
        - Implemented **CSV export** of results and **batch prediction** feature for classroom evaluation.
        - Deployed model using **Streamlit sharing**, made mobile responsive with enhanced UI/UX and Lottie animations.
        """)

    with st.expander("📌 Tax Calculator"):
        st.write("""
        Built a dynamic **Streamlit-based Indian income tax calculator** that supports both **Old and New tax regimes**.
        - Designed an intuitive form with validation using sliders and dropdowns.
        - Implemented tax logic using **Python dictionaries, conditionals, and modular functions**.
        - Integrated real-time **summary cards** and **Plotly bar charts** for visual tax breakdown.
        - Added export functionality to **PDF and CSV**, and styled UI with custom CSS for a professional look.
        """)


# --- Education ---
with tabs[3]:
    st_lottie(lotties["education"], height=200)
    for degree, branch, institution, year in education:
        st.write(f"**{degree} - {branch}**, {institution} ({year})")
        st.markdown("---")

# --- Experience ---
with tabs[4]:
    st.markdown("""
💼 Software Engineer | Lyros Technologies Pvt. Ltd. (Feb 2025 – Present)
- Undergoing a comprehensive, industry-aligned training program specializing in Artificial Intelligence and Machine Learning (AI/ML).

- Gaining hands-on experience with Python, scikit-learn, deep learning frameworks, and real-world data pipelines.

- Building and deploying end-to-end ML solutions, translating theoretical concepts into production-grade applications.

- Collaborating closely with senior engineers and mentors, contributing to live projects and enhancing both technical depth and professional agility.

- Focusing on scalable, intelligent system design while following agile development practices and modern software engineering principles.
    """)

# --- Summary (was tab 7) ---
with tabs[5]:
    st.write("""
I'm a results-driven Software Engineer with a strong foundation in Artificial Intelligence, Machine Learning, and Full-Stack Development. Currently working at Lyros Technologies Pvt. Ltd., where I’m actively involved in real-time AI/ML projects and collaborative, agile-based development.

My expertise spans across:

- Python programming, data analysis, and ML model development using tools like scikit-learn, Pandas, and Seaborn.

- Building interactive web applications using Streamlit, enhanced with Lottie animations and custom UI/UX styling.

- Deploying scalable, modular systems that bridge the gap between data science and real-world applications.

With a passion for innovation and a commitment to continuous learning, I thrive on turning complex problems into intelligent, actionable solutions — whether it's through predictive modeling, system design, or intuitive data-driven apps.
    """)

# --- Contact (was tab 6) ---
with tabs[6]:
    st_lottie(lotties["contact"], height=200)
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        if st.form_submit_button("Send"):
            st.success("✅ Message received. Thank you!")
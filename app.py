# app.py
# Offline AI Career Guidance Chatbot
# This app works completely OFFLINE using rule-based logic and predefined data.
# No internet, no APIs - everything runs locally!

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from fpdf import FPDF
import io
import re
from career_data import CAREERS, ALL_SKILLS, CAREER_NAMES

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="AI Career Guidance Chatbot",
    page_icon="🎯",
    layout="wide"
)

# ---------------------------------------------------------
# LOAD CSS FILE FOR STYLING
# ---------------------------------------------------------
def load_css(file_name):
    """Read the CSS file and inject it into the Streamlit app."""
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

# ---------------------------------------------------------
# SESSION STATE INITIALIZATION
# Session state remembers values between user interactions.
# ---------------------------------------------------------
if "user_profile" not in st.session_state:
    st.session_state.user_profile = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------------------------------------------------
# HERO BANNER
# ---------------------------------------------------------
st.markdown("""
<div class="hero-banner">
    <h1>🎯 AI Career Guidance Chatbot</h1>
    <p>Get personalized career recommendations, skill gap analysis, and learning roadmaps </p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SIDEBAR - USER PROFILE FORM
# ---------------------------------------------------------
st.sidebar.title("👤 Your Profile")
st.sidebar.markdown("Fill in your details to get personalized guidance.")

with st.sidebar.form("profile_form"):
    name = st.text_input("Full Name", placeholder="e.g deep malvankar")
    education = st.selectbox(
        "Highest Education",
        ["High School", "Diploma", "Bachelor's Degree", "Master's Degree", "PhD"]
    )
    interest_area = st.selectbox(
        "Field of Interest",
        ["Technology", "Data & AI", "Design", "Management", "Security", "Networking", "Other"]
    )
    current_skills = st.multiselect("Your Current Skills", ALL_SKILLS)
    experience = st.slider("Years of Experience", 0, 20, 0)
    submitted = st.form_submit_button("Save Profile")

if submitted:
    st.session_state.user_profile = {
        "name": name if name else "Guest",
        "education": education,
        "interest_area": interest_area,
        "skills": current_skills,
        "experience": experience
    }
    st.sidebar.success("✅ Profile saved successfully!")

# ---------------------------------------------------------
# HELPER FUNCTIONS (RULE-BASED LOGIC)
# ---------------------------------------------------------

def recommend_careers(user_skills, top_n=5):
    """
    Recommend careers based on how many of the user's skills
    match the required skills for each career.
    Returns a sorted list of (career_name, match_percent, matched_skills, missing_skills)
    """
    results = []
    for career, info in CAREERS.items():
        required = set(info["skills"])
        user_set = set(user_skills)
        matched = required.intersection(user_set)
        missing = required - user_set

        if len(required) > 0:
            match_percent = (len(matched) / len(required)) * 100
        else:
            match_percent = 0

        results.append((career, match_percent, matched, missing))

    # Sort by match percentage, highest first
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:top_n]


def calculate_readiness_score(matched_skills, required_skills, experience):
    """
    Calculate a Career Readiness Score (0-100) based on:
    - Skill match percentage (70% weight)
    - Years of experience (30% weight, capped at 10 years)
    """
    if len(required_skills) == 0:
        skill_score = 0
    else:
        skill_score = (len(matched_skills) / len(required_skills)) * 70

    # Experience contributes up to 30 points (capped at 10 years = full 30 points)
    exp_score = min(experience, 10) / 10 * 30

    total_score = round(skill_score + exp_score, 1)
    return total_score


def generate_pdf_report(profile, recommendations):
    """
    Generate a PDF report containing the user's profile and
    top career recommendations with skill gaps and roadmap.
    Returns PDF as bytes.
    """
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "AI Career Guidance Report", ln=True, align="C")
    pdf.ln(5)

    # Profile section
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "User Profile", ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 8, f"Name: {profile['name']}", ln=True)
    pdf.cell(0, 8, f"Education: {profile['education']}", ln=True)
    pdf.cell(0, 8, f"Field of Interest: {profile['interest_area']}", ln=True)
    pdf.cell(0, 8, f"Experience: {profile['experience']} years", ln=True)

    skills_text = ", ".join(profile['skills']) if profile['skills'] else "None"
    pdf.multi_cell(0, 8, f"Current Skills: {skills_text}")
    pdf.ln(5)

    # Recommendations section
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Top Career Recommendations", ln=True)

    for career, match, matched, missing in recommendations:
        info = CAREERS[career]
        pdf.set_font("Arial", "B", 11)
        pdf.cell(0, 8, f"{career} - Match: {match:.1f}%", ln=True)

        pdf.set_font("Arial", "", 10)
        pdf.multi_cell(0, 6, f"Description: {info['description']}")
        pdf.multi_cell(0, 6, f"Salary Range: {info['salary_range']}")

        missing_text = ", ".join(missing) if missing else "None - You meet all requirements!"
        pdf.multi_cell(0, 6, f"Skills to Learn: {missing_text}")

        resources_text = ", ".join(info['resources'])
        pdf.multi_cell(0, 6, f"Learning Resources: {resources_text}")

        certs_text = ", ".join(info['certifications'])
        pdf.multi_cell(0, 6, f"Recommended Certifications: {certs_text}")

        pdf.multi_cell(0, 6, f"Career Growth Path: {info['growth']}")
        pdf.ln(3)

    # Output as bytes
    pdf_bytes = pdf.output(dest="S").encode("latin-1", errors="replace")
    return pdf_bytes


def chatbot_response(user_message):
    """
    Simple rule-based chatbot.
    Looks for keywords in the user's message and matches them
    to career names, skills, or general guidance questions.
    """
    message = user_message.lower()

    # Greetings
    greetings = ["hi", "hello", "hey", "good morning", "good evening"]
    if any(word in message for word in greetings):
        return "Hello! 👋 I'm your offline career assistant. Ask me about any career, skill, or salary range!"

    # Thanks
    if "thank" in message:
        return "You're welcome! Best of luck with your career journey! 🚀"

    # Check if message mentions a specific career
    for career in CAREER_NAMES:
        if career.lower() in message:
            info = CAREERS[career]
            if "salary" in message:
                return f"💰 The salary range for {career} is {info['salary_range']}."
            elif "skill" in message:
                return f"🛠️ Skills required for {career}: {', '.join(info['skills'])}."
            elif "certification" in message or "certificate" in message:
                return f"📜 Recommended certifications for {career}: {', '.join(info['certifications'])}."
            elif "resource" in message or "learn" in message:
                return f"📚 Learning resources for {career}: {', '.join(info['resources'])}."
            elif "growth" in message or "promotion" in message:
                return f"📈 Career growth path for {career}: {info['growth']}."
            elif "interview" in message:
                return f"❓ Sample interview question for {career}: {info['interview_questions'][0]}"
            else:
                return f"ℹ️ {career}: {info['description']} Salary: {info['salary_range']}."

    # Check if message mentions a specific skill
    for skill in ALL_SKILLS:
        if skill.lower() in message:
            matching_careers = [c for c, info in CAREERS.items() if skill in info["skills"]]
            return f"🔍 Careers that require {skill}: {', '.join(matching_careers[:5])}."

    # General questions
    if "career" in message and "recommend" in message:
        return "Please fill in your profile in the sidebar and check the 'Career Recommendations' tab for personalized suggestions!"

    if "salary" in message:
        return "Salary ranges vary by career. Ask me about a specific career, e.g., 'What is the salary for Data Scientist?'"

    if "roadmap" in message:
        return "Check the 'Learning Roadmap' tab after getting your recommendations for a step-by-step learning plan!"

    # Default response
    return ("I'm not sure about that. Try asking me about a specific career "
            "(e.g., 'Tell me about Data Scientist'), a skill, salary, or certifications. "
            "You can also explore the tabs above for detailed guidance!")


# ---------------------------------------------------------
# MAIN CONTENT - TABS
# ---------------------------------------------------------
tabs = st.tabs([
    "🏠 Home",
    "🎯 Career Recommendations",
    "📊 Skill Gap Analysis",
    "🗺️ Learning Roadmap",
    "❓ Interview Questions",
    "💰 Salary Insights",
    "📈 Readiness Score",
    "📊 Skill Dashboard",
    "💬 Career Chatbot",
    "📄 PDF Report"
])

# -----------------------------
# TAB 1: HOME
# -----------------------------
with tabs[0]:
    st.markdown("<h2 class='section-header'>Welcome!</h2>", unsafe_allow_html=True)

    if st.session_state.user_profile is None:
        st.info("👈 Please fill in your profile in the sidebar to get started.")
        st.markdown("""
        ### How this app works:
        1. **Fill your profile** in the sidebar (skills, education, interest).
        2. Get **personalized career recommendations** based on your skills.
        3. See your **skill gaps** for each recommended career.
        4. Follow a **learning roadmap** to bridge those gaps.
        5. Practice **interview questions** for your target career.
        6. Explore **salary insights** with interactive charts.
        7. Check your **Career Readiness Score**.
        8. Track your progress on the **Skill Dashboard**.
        9. Download a **PDF report** of your career plan.
        
        """)
    else:
        profile = st.session_state.user_profile
        st.success(f"Welcome back, **{profile['name']}**! 🎉")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <div class="career-card">
                <h3>🎓 Education</h3>
                <p>{profile['education']}</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="career-card">
                <h3>💡 Interest Area</h3>
                <p>{profile['interest_area']}</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <div class="career-card">
                <h3>⏳ Experience</h3>
                <p>{profile['experience']} years</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<h3 class='section-header'>Your Skills</h3>", unsafe_allow_html=True)
        if profile['skills']:
            st.write(", ".join(profile['skills']))
        else:
            st.warning("No skills added yet. Update your profile in the sidebar.")

# -----------------------------
# TAB 2: CAREER RECOMMENDATIONS
# -----------------------------
with tabs[1]:
    st.markdown("<h2 class='section-header'>🎯 Career Recommendations</h2>", unsafe_allow_html=True)

    if st.session_state.user_profile is None:
        st.warning("⚠️ Please fill in your profile in the sidebar first.")
    else:
        profile = st.session_state.user_profile
        recommendations = recommend_careers(profile["skills"], top_n=5)

        # Save recommendations for use in other tabs
        st.session_state.recommendations = recommendations

        st.write(f"Based on your skills, here are the top {len(recommendations)} career matches:")

        for career, match, matched, missing in recommendations:
            info = CAREERS[career]
            st.markdown(f"""
            <div class="career-card">
                <h3>{career} — {match:.1f}% Match</h3>
                <p>{info['description']}</p>
                <p><b>💰 Salary:</b> {info['salary_range']}</p>
                <p><b>✅ Matched Skills:</b> {', '.join(matched) if matched else 'None'}</p>
                <p><b>📌 Skills to Learn:</b> {', '.join(missing) if missing else 'You meet all requirements!'}</p>
            </div>
            """, unsafe_allow_html=True)

            # Progress bar for match percentage
            st.progress(min(int(match), 100))

# -----------------------------
# TAB 3: SKILL GAP ANALYSIS
# -----------------------------
with tabs[2]:
    st.markdown("<h2 class='section-header'>📊 Skill Gap Analysis</h2>", unsafe_allow_html=True)

    if st.session_state.user_profile is None:
        st.warning("⚠️ Please fill in your profile in the sidebar first.")
    else:
        profile = st.session_state.user_profile

        selected_career = st.selectbox("Select a career to analyze:", CAREER_NAMES)
        info = CAREERS[selected_career]

        required = set(info["skills"])
        user_set = set(profile["skills"])
        matched = required.intersection(user_set)
        missing = required - user_set

        match_percent = (len(matched) / len(required)) * 100 if required else 0

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class="career-card">
                <h3>✅ Skills You Have</h3>
                <p>{', '.join(matched) if matched else 'None yet'}</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="career-card">
                <h3>📌 Skills You Need</h3>
                <p>{', '.join(missing) if missing else 'None - Great job!'}</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("### Overall Skill Match")
        st.progress(int(match_percent))
        st.write(f"**{match_percent:.1f}%** of required skills matched.")

        # Plotly bar chart showing skill match
        fig = go.Figure(data=[
            go.Bar(name='Have', x=['Skill Match'], y=[len(matched)], marker_color='#11998e'),
            go.Bar(name='Missing', x=['Skill Match'], y=[len(missing)], marker_color='#ff6b6b')
        ])
        fig.update_layout(barmode='stack', title=f"Skill Breakdown for {selected_career}", height=350)
        st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# TAB 4: LEARNING ROADMAP
# -----------------------------
with tabs[3]:
    st.markdown("<h2 class='section-header'>🗺️ Learning Roadmap</h2>", unsafe_allow_html=True)

    if st.session_state.user_profile is None:
        st.warning("⚠️ Please fill in your profile in the sidebar first.")
    else:
        profile = st.session_state.user_profile

        selected_career = st.selectbox("Select a career for your roadmap:", CAREER_NAMES, key="roadmap_career")
        info = CAREERS[selected_career]

        required = info["skills"]
        user_set = set(profile["skills"])
        missing = [s for s in required if s not in user_set]

        st.markdown(f"### Roadmap to become a **{selected_career}**")

        if not missing:
            st.success("🎉 You already have all the required skills! Focus on certifications and real-world projects.")
        else:
            st.write("Follow these steps in order to build the missing skills:")
            for i, skill in enumerate(missing, start=1):
                st.markdown(f"""
                <div class="career-card">
                    <h3>Step {i}: Learn {skill}</h3>
                    <p>Recommended resources: {', '.join(info['resources'])}</p>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("### 📜 Recommended Certifications")
        for cert in info["certifications"]:
            st.write(f"- {cert}")

        st.markdown("### 📈 Career Growth Path")
        st.write(info["growth"])

# -----------------------------
# TAB 5: INTERVIEW QUESTIONS
# -----------------------------
with tabs[4]:
    st.markdown("<h2 class='section-header'>❓ Interview Questions</h2>", unsafe_allow_html=True)

    selected_career = st.selectbox("Select a career:", CAREER_NAMES, key="interview_career")
    info = CAREERS[selected_career]

    st.markdown(f"### Common Interview Questions for {selected_career}")
    for i, q in enumerate(info["interview_questions"], start=1):
        st.markdown(f"""
        <div class="career-card">
            <p><b>Q{i}:</b> {q}</p>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------
# TAB 6: SALARY INSIGHTS
# -----------------------------
with tabs[5]:
    st.markdown("<h2 class='section-header'>💰 Salary Insights</h2>", unsafe_allow_html=True)

    # Extract approximate average salary (in lakhs) for each career for visualization
    # We parse the salary_range string to get min and max values
    career_names = []
    min_salaries = []
    max_salaries = []

    for career, info in CAREERS.items():
        salary_str = info["salary_range"]
        # Remove currency symbols and split by '-'
        clean_str = salary_str.replace("₹", "").replace(" / year", "").replace(",", "")
        parts = clean_str.split("-")
        try:
            min_val = int(parts[0].strip()) / 100000  # convert to lakhs
            max_val = int(parts[1].strip()) / 100000
        except (ValueError, IndexError):
            min_val, max_val = 0, 0

        career_names.append(career)
        min_salaries.append(min_val)
        max_salaries.append(max_val)

    # Bar chart comparing min and max salaries across careers
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Min Salary (Lakhs ₹)', x=career_names, y=min_salaries, marker_color='#2575fc'))
    fig.add_trace(go.Bar(name='Max Salary (Lakhs ₹)', x=career_names, y=max_salaries, marker_color='#11998e'))
    fig.update_layout(
        barmode='group',
        title="Salary Ranges Across Careers (in Lakhs ₹ per year)",
        height=600,
        xaxis_tickangle=-45
    )
    st.plotly_chart(fig, use_container_width=True)

    # Show detailed table for selected career
    st.markdown("### Detailed Salary Information")
    selected_career = st.selectbox("Select a career for details:", CAREER_NAMES, key="salary_career")
    st.write(f"**{selected_career}**: {CAREERS[selected_career]['salary_range']}")

# -----------------------------
# TAB 7: CAREER READINESS SCORE
# -----------------------------
with tabs[6]:
    st.markdown("<h2 class='section-header'>📈 Career Readiness Score</h2>", unsafe_allow_html=True)

    if st.session_state.user_profile is None:
        st.warning("⚠️ Please fill in your profile in the sidebar first.")
    else:
        profile = st.session_state.user_profile

        selected_career = st.selectbox("Select a career to check readiness:", CAREER_NAMES, key="readiness_career")
        info = CAREERS[selected_career]

        required = set(info["skills"])
        user_set = set(profile["skills"])
        matched = required.intersection(user_set)

        score = calculate_readiness_score(matched, required, profile["experience"])

        # Gauge chart for readiness score
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            title={'text': f"Readiness Score for {selected_career}"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "#2575fc"},
                'steps': [
                    {'range': [0, 40], 'color': "#ff6b6b"},
                    {'range': [40, 70], 'color': "#ffd93d"},
                    {'range': [70, 100], 'color': "#11998e"}
                ]
            }
        ))
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

        if score < 40:
            st.warning("🔴 You're at an early stage. Focus on building core skills for this career.")
        elif score < 70:
            st.info("🟡 You're making good progress! Keep learning the missing skills.")
        else:
            st.success("🟢 You're well-prepared for this career! Consider applying for relevant roles.")

# -----------------------------
# TAB 8: SKILL PROGRESS DASHBOARD
# -----------------------------
with tabs[7]:
    st.markdown("<h2 class='section-header'>📊 Skill Progress Dashboard</h2>", unsafe_allow_html=True)

    if st.session_state.user_profile is None:
        st.warning("⚠️ Please fill in your profile in the sidebar first.")
    else:
        profile = st.session_state.user_profile
        user_set = set(profile["skills"])

        # Calculate match percentage for ALL careers
        dashboard_data = []
        for career, info in CAREERS.items():
            required = set(info["skills"])
            matched = required.intersection(user_set)
            match_percent = (len(matched) / len(required)) * 100 if required else 0
            dashboard_data.append({"Career": career, "Match %": round(match_percent, 1)})

        # Sort by match percentage
        dashboard_data.sort(key=lambda x: x["Match %"], reverse=True)

        careers_list = [d["Career"] for d in dashboard_data]
        match_list = [d["Match %"] for d in dashboard_data]

        # Horizontal bar chart showing readiness across all careers
        fig = px.bar(
            x=match_list,
            y=careers_list,
            orientation='h',
            labels={'x': 'Skill Match %', 'y': 'Career'},
            title="Your Skill Match Across All Careers",
            color=match_list,
            color_continuous_scale=['#ff6b6b', '#ffd93d', '#11998e']
        )
        fig.update_layout(height=700, yaxis={'categoryorder': 'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

        # Show individual progress bars too
        st.markdown("### Detailed Progress")
        for d in dashboard_data[:10]:
            st.write(f"**{d['Career']}**")
            st.progress(int(d["Match %"]))

# -----------------------------
# TAB 9: CAREER CHATBOT
# -----------------------------
with tabs[8]:
    st.markdown("<h2 class='section-header'>💬 AI Career Chatbot</h2>", unsafe_allow_html=True)
    st.write("Ask me anything about careers, skills, salaries, certifications, or interview tips!")

    # Display chat history
    for sender, message in st.session_state.chat_history:
        if sender == "user":
            st.markdown(f"<div class='chat-user'>{message}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-bot'>{message}</div>", unsafe_allow_html=True)

    # Chat input
    user_input = st.chat_input("Type your question here...")

    if user_input:
        st.session_state.chat_history.append(("user", user_input))
        response = chatbot_response(user_input)
        st.session_state.chat_history.append(("bot", response))
        st.rerun()

# -----------------------------
# TAB 10: PDF REPORT DOWNLOAD
# -----------------------------


with tabs[9]:
    st.markdown(
        "<h2 class='section-header'>📄 Download Your Career Report</h2>",
        unsafe_allow_html=True
    )

    if st.session_state.user_profile is None:
        st.warning("⚠️ Please fill in your profile in the sidebar first.")

    else:
        profile = st.session_state.user_profile

        recommendations = recommend_careers(
            profile["skills"],
            top_n=5
        )

        st.write(
            "Click the button below to generate and download your personalized career report as a PDF."
        )

        if st.button("📥 Generate PDF Report"):

            pdf_bytes = generate_pdf_report(
                profile,
                recommendations
            )

            st.download_button(
                label="⬇️ Download PDF Report",
                data=pdf_bytes,
                file_name=f"{profile['name'].replace(' ', '_')}_Career_Report.pdf",
                mime="application/pdf"
            )

            st.success(
                "✅ Report generated successfully! Click the download button above."
            )
# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("---")
st.markdown("""
<div class="hero-slider">

<div class="slide">
    <div class="slide-content">
        <h1>🎯 AI Career Guidance</h1>
        <p>Discover Your Dream Career Path 🚀</p>
    </div>
</div>

<div class="slide">
    <div class="slide-content">
        <h1>💡 Skill Analysis</h1>
        <p>Find Skills You Need To Grow 📈</p>
    </div>
</div>

<div class="slide">
    <div class="slide-content">
        <h1>🏆 Interview Preparation</h1>
        <p>Get Ready For Your Dream Job 💼</p>
    </div>
</div>

</div>
""", unsafe_allow_html=True)


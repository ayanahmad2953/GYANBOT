import streamlit as st
from ai_quiz_generator import generate_quiz
from utils import evaluate_answers, generate_recommendations

st.set_page_config(page_title="GyanBot", page_icon="🧠", layout="wide")

# Session state
if "quiz_generated" not in st.session_state:
    st.session_state.quiz_generated = False

if "questions" not in st.session_state:
    st.session_state.questions = []

if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}

if "subject" not in st.session_state:
    st.session_state.subject = ""

if "topic" not in st.session_state:
    st.session_state.topic = ""

# Title
st.title("🧠 GyanBot — AI-Powered Student Assessment Tool")
st.markdown("Generate quizzes using AI, solve them, and get smart feedback.")

# Sidebar
st.sidebar.header("Quiz Settings")

subject = st.sidebar.selectbox(
    "Choose Subject",
    ["Python", "DBMS", "Machine Learning", "Operating System", "Computer Networks"]
)

topic = st.sidebar.text_input("Enter Topic", placeholder="e.g. OOPs, SQL Joins, Regression")
difficulty = st.sidebar.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
num_questions = st.sidebar.slider("Number of Questions", 3, 10, 5)

generate_btn = st.sidebar.button("🚀 Generate Quiz")

# Generate quiz
if generate_btn:
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("Generating quiz using AI..."):
            questions = generate_quiz(subject, topic, difficulty, num_questions)

        if questions:
            st.session_state.quiz_generated = True
            st.session_state.quiz_submitted = False
            st.session_state.questions = questions
            st.session_state.user_answers = {}
            st.session_state.subject = subject
            st.session_state.topic = topic
            st.success("Quiz generated successfully!")
        else:
            st.error("Quiz generation failed. Try again with a simpler topic.")

# Show quiz
if st.session_state.quiz_generated and st.session_state.questions:
    st.subheader(f"📘 Quiz on {st.session_state.topic} ({st.session_state.subject})")

    with st.form("quiz_form"):
        user_answers = {}

        for i, q in enumerate(st.session_state.questions):
            st.markdown(f"### Q{i+1}. {q['question']}")
            answer = st.radio(
                "Select your answer:",
                q["options"],
                key=f"q_{i}"
            )
            user_answers[i] = answer
            st.markdown("---")

        submit_btn = st.form_submit_button("✅ Submit Quiz")

    if submit_btn:
        st.session_state.user_answers = user_answers
        st.session_state.quiz_submitted = True

# Evaluate quiz
if st.session_state.quiz_submitted:
    score, weak_topics, results = evaluate_answers(
        st.session_state.questions,
        st.session_state.user_answers
    )

    recommendations = generate_recommendations(
        weak_topics,
        st.session_state.subject,
        st.session_state.topic
    )

    st.success(f"🎯 Your Score: {score} / {len(st.session_state.questions)}")

    if score == len(st.session_state.questions):
        st.balloons()
        st.info("Excellent! You answered all questions correctly.")
    elif score >= len(st.session_state.questions) // 2:
        st.info("Good attempt! Review incorrect answers and revise weak areas.")
    else:
        st.warning("You need more practice on this topic.")

    st.subheader("📊 Quiz Analysis")

    for i, r in enumerate(results):
        st.markdown(f"### Q{i+1}. {r['question']}")

        if r["is_correct"]:
            st.markdown(f"✅ Your Answer: **{r['your_answer']}**")
        else:
            st.markdown(f"❌ Your Answer: **{r['your_answer']}**")
            st.markdown(f"✅ Correct Answer: **{r['correct_answer']}**")

        st.markdown("---")

    st.subheader("📚 Personalized Recommendations")
    for rec in recommendations:
        st.write(f"- {rec}")

    if weak_topics:
        st.subheader("⚠️ Weak Areas")
        for t in set(weak_topics):
            st.write(f"- {t}")

st.markdown("---")
st.caption("Built with Streamlit + Gemini API")
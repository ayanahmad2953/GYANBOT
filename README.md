# 🧠 GyanBot — AI-Powered Student Assessment Tool

[![Streamlit App](https://img.shields.io/badge/Live%20App-Streamlit-red?logo=streamlit)](https://ayanahmad2953-gyanbot-app-rz3tel.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/Status-Student%20Project-success)](#)

GyanBot is an **AI-powered student assessment and quiz generation platform** built using **Streamlit** and the **Google Gemini API**.  
The application enables students to generate topic-specific multiple-choice quizzes, attempt them in an interactive interface, and receive **instant evaluation, performance analysis, weak-area detection, and personalized study recommendations**.

🔗 **Live Demo:**  
**https://ayanahmad2953-gyanbot-app-rz3tel.streamlit.app/**

---

## 📌 Overview

Traditional quiz applications usually rely on static, pre-written question banks.  
**GyanBot** improves this experience by using **Generative AI** to create quizzes dynamically based on:

- **Subject**
- **Topic**
- **Difficulty level**
- **Number of questions**

This makes the app flexible, scalable, and more useful for personalized learning and self-assessment.

---

## ✨ Key Features

- **AI-Generated Quizzes**  
  Dynamically generates MCQ-based quizzes using the **Google Gemini API**.

- **Custom Quiz Configuration**  
  Students can choose:
  - Subject
  - Topic
  - Difficulty level
  - Number of questions

- **Interactive Quiz Interface**  
  Clean and user-friendly **Streamlit UI** for answering questions directly in the browser.

- **Automatic Evaluation**  
  Instantly checks answers and calculates the final score.

- **Weak Area Identification**  
  Highlights the topics where the student made mistakes.

- **Personalized Recommendations**  
  Suggests which topics should be revised and where additional practice is needed.

- **Responsive Web App**  
  Runs as a lightweight web application that can be deployed on **Streamlit Community Cloud**.

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Frontend / UI | Streamlit |
| AI Model | Google Gemini API |
| Environment Management | python-dotenv |
| Data Handling | Pandas |

---

## 📂 Project Structure

```bash
GyanBot/
│── app.py                  # Main Streamlit application
│── ai_quiz_generator.py    # Gemini-based quiz generation logic
│── utils.py                # Quiz evaluation + recommendation functions
│── requirements.txt        # Python dependencies
│── .gitignore              # Ignore secrets and cache files
│── .env                    # API key file (local only, not uploaded to GitHub)

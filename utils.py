def evaluate_answers(questions, user_answers):
    score = 0
    weak_topics = []
    results = []

    for i, q in enumerate(questions):
        user_ans = user_answers.get(i)
        correct_ans = q["answer"]

        is_correct = user_ans == correct_ans

        if is_correct:
            score += 1
        else:
            weak_topics.append(q["topic"])

        results.append({
            "question": q["question"],
            "your_answer": user_ans,
            "correct_answer": correct_ans,
            "is_correct": is_correct,
            "topic": q["topic"]
        })

    return score, weak_topics, results


def generate_recommendations(weak_topics, subject, topic):
    recommendations = []

    if weak_topics:
        unique_topics = list(set(weak_topics))

        for t in unique_topics:
            recommendations.append(f"Revise topic: {t} in {subject}")

        recommendations.append(f"Practice more MCQs on '{topic}'")
        recommendations.append(f"Review theory and examples of '{topic}'")
    else:
        recommendations.append("Excellent work! You performed very well.")
        recommendations.append("Try a harder difficulty level next time.")

    return recommendations
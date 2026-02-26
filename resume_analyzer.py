import os
import PyPDF2
from docx import Document
import google.generativeai as genai

# 🔐 Read API Key securely from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    GEMINI_API_KEY = input("Enter your Gemini API Key: ")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

# ---------------- FILE READER ---------------- #

def read_resume(file_path):
    ext = file_path.split(".")[-1].lower()

    if ext == "txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    elif ext == "docx":
        doc = Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])

    elif ext == "pdf":
        text = ""
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
        return text

    else:
        return ""


# ---------------- AI QUESTION GENERATOR ---------------- #

def generate_ai_questions(resume_text):
    try:
        prompt = f"""
        You are a professional technical interviewer.

        Based on this resume:

        {resume_text}

        Generate 5 technical interview questions.
        Make them specific to the candidate.
        """

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error generating questions: {e}"


# ---------------- AI EVALUATION ---------------- #

def evaluate_answer(question, answer):
    try:
        prompt = f"""
        You are a strict technical interviewer.

        Question: {question}
        Candidate Answer: {answer}

        Give:
        1. Score out of 10
        2. Short feedback
        3. Follow-up question if weak
        """

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error evaluating answer: {e}"


# ---------------- MAIN ---------------- #

def main():
    path = input("Enter Resume Path: ")
    resume = read_resume(path)

    if not resume:
        print("Could not read resume.")
        return

    print("\n🤖 Generating AI Interview Questions...\n")
    questions_text = generate_ai_questions(resume)
    print(questions_text)

    print("\n===== AI INTERVIEW STARTED =====")

    questions = questions_text.split("\n")

    for q in questions:
        if len(q.strip()) < 5:
            continue

        print("\n" + q)
        ans = input("Your Answer: ")

        print("\n🔍 AI Evaluating...\n")
        result = evaluate_answer(q, ans)
        print(result)


if __name__ == "__main__":
    main()
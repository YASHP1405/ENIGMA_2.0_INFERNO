import os
import re
import google.generativeai as genai
import PyPDF2
from docx import Document

# ==============================
# 🔐 GEMINI CONFIGURATION
# ==============================

# Replace with your actual Gemini API Key
GEMINI_API_KEY = "AIzaSyCnnIRfTQsfxJ4qQOAMCr3RocObYZFPemU"
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

# ==============================
# 📄 FILE READER
# ==============================

def read_resume(file_path):
    # Remove quotes if user drags and drops file into terminal
    file_path = file_path.replace('"', '').replace("'", "")
    ext = file_path.split(".")[-1].lower()

    try:
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
            print("❌ Unsupported file format. Use txt, pdf, or docx.")
            return None

    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None


# ==============================
# 🤖 GENERATE QUESTIONS
# ==============================

def generate_ai_questions(resume_text):
    prompt = f"""
    You are a professional technical interviewer.
    Based on this resume:
    {resume_text}

    Generate exactly 5 numbered technical interview questions based on the candidate's skills and experience.
    Format: 
    1. Question here
    2. Question here
    Only return the questions.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error generating questions: {e}"


# ==============================
# 🔍 EVALUATE ANSWER
# ==============================

def evaluate_answer(question, answer):
    prompt = f"""
    You are a strict technical interviewer.

    Question: {question}
    Candidate Answer: {answer}

    Provide:
    1. Score out of 10 (Format: Score: X/10)
    2. Short feedback
    3. One follow-up question if the answer is weak or incomplete.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error evaluating answer: {e}"


# ==============================
# 🎤 MAIN INTERVIEW FLOW
# ==============================

def main():
    print("===== AI RESUME INTERVIEW SYSTEM (GEMINI) =====\n")

    path = input("Enter Resume File Path: ").strip()
    resume = read_resume(path)

    if not resume:
        print("❌ Could not read resume.")
        return

    print("\n🤖 Generating Questions...\n")
    questions_text = generate_ai_questions(resume)

    if "❌" in questions_text:
        print(questions_text)
        return

    # Split the response into a list of questions
    # This regex looks for digits followed by a dot
    questions = re.findall(r"\d+\.\s*(.*)", questions_text)
    
    # Fallback if regex fails (Gemini sometimes formats differently)
    if not questions:
        questions = [q.strip() for q in questions_text.split('\n') if q.strip() and q[0].isdigit()]

    if not questions:
        print("❌ Could not parse questions. Raw output:")
        print(questions_text)
        return

    print("Questions Generated Successfully!")
    print("\n===== AI INTERVIEW STARTED =====")

    total_score = 0
    actual_count = 0

    for i, q in enumerate(questions[:5], start=1):
        print(f"\nQ{i}: {q}")
        ans = input("Your Answer: ")

        print("\n🔍 Evaluating...\n")
        result = evaluate_answer(q, ans)
        print(result)

        # Extract score using regex (looks for X/10)
        score_match = re.search(r"(\d+)/10", result)
        if score_match:
            total_score += int(score_match.group(1))
            actual_count += 1

    if actual_count > 0:
        avg_score = total_score / actual_count
        print("\n==============================")
        print(f"🎯 Final Average Score: {avg_score:.2f}/10")
        print("==============================\n")


if __name__ == "__main__":
    main()
from flask import Flask, render_template, request, jsonify
import subprocess
import tempfile
import os
from questions import get_random_question

app = Flask(__name__)

current_question = get_random_question()

@app.route("/")
def interview():
    return render_template("interview.html", question=current_question["question"])

@app.route("/get_question")
def get_question():
    global current_question
    current_question = get_random_question()
    return jsonify({
        "question": current_question["question"],
        "tests": current_question["tests"]
    })

@app.route("/submit", methods=["POST"])
def submit():
    code = request.json.get("code")
    tests = current_question["tests"]

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
            tmp.write(code.encode())
            tmp_path = tmp.name

        for test in tests:
            result = subprocess.run(
                ["python", tmp_path],
                input=test["input"],
                text=True,
                capture_output=True,
                timeout=5
            )

            output = result.stdout.strip()

            if output != test["output"]:
                os.remove(tmp_path)
                return jsonify({"result": "❌ Failed"})

        os.remove(tmp_path)
        return jsonify({"result": "✅ All Test Cases Passed"})

    except Exception as e:
        return jsonify({"result": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, session
from solver import solve_math
from explain import explain_solution
from PIL import Image
import pytesseract
import os
import pyttsx3

app = Flask(__name__)
app.secret_key = 'qais_smart_secret'

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Path to tesseract.exe (adjust if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Voice Function (pyttsx3)
def speak(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("❌ Voice Error:", str(e))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = ""

    # Image input
    if 'image' in request.files:
        img_file = request.files['image']
        if img_file.filename:
            img_path = os.path.join(UPLOAD_FOLDER, 'input.jpg')
            img_file.save(img_path)
            try:
                img = Image.open(img_path)
                question = pytesseract.image_to_string(img)
            except Exception as e:
                return render_template('error.html', message=f"OCR Error: {str(e)}")

    # Manual input
    if not question:
        question = request.form.get('question', '').strip()

    if not question:
        return render_template('error.html', message="No input provided.")

    # Solve
    solution = solve_math(question)
    explanation = explain_solution(question, solution)

    # Voice output
    speak(f"The answer is {solution}")

    return render_template('result.html', question=question, solution=solution, explanation=explanation)

if __name__ == '__main__':
    app.run(debug=True)

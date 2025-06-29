from gtts import gTTS
import os

def explain_solution(question, solution):
    # Simple step explanation
    explanation = f"To solve the question {question}, we simplify it step-by-step. The final answer is {solution}."

    # Generate audio
    tts = gTTS(explanation)
    audio_file = f"static/voice.mp3"
    tts.save(audio_file)

    return explanation

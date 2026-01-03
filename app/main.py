"""This python module handles running the heavy lifting of loading the text model pipeline and processing the prompt and outputting infromation from AI Assistant"""

from fastapi import FastAPI
from models import load_text_model, generate_text

app = FastAPI()

pipe = load_text_model()


@app.get("/generate/text")
def serve_language_model_controller(prompt: str) -> str:
    output = generate_text(pipe, prompt)
    return output

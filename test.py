from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)
models = [m.name for m in genai.list_models()]
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")  # Note the full model path

# Route for rendering the form and handling the POST request
@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        print(f"Prompt received: {prompt}")
        print(f"AI Response: {response}")
        try:
            result = model.generate_content(prompt)
            response = result.text
        except Exception as e:
            response = f"Error: {e}"
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)

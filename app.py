from flask import Flask, request, render_template
from transformers import pipeline

# load sentiment model
sentiment_pipeline = pipeline("sentiment-analysis")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        text = request.form["text"]
        result = sentiment_pipeline(text)[0]  # {'label': 'POSITIVE', 'score': 0.998}
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
 

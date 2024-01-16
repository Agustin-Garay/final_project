"""Application Server"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("emotionDetector")

@app.route("/")
def render_index_page():
    """Renders the main page"""
    return render_template('index.html')

@app.route("/emotionDetector")
def emo_detector():
    """Runs the emotion detector once the button is clicked"""
    text_to_analyse = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyse)
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    anger = str(response["anger"])
    disgust = str(response["disgust"])
    fear = str(response["fear"])
    joy = str(response["joy"])
    sadness = str(response["sadness"])
    dominant = str(response["dominant_emotion"])
    return f"For the given statement, the system response is 'anger': {anger}, \
        'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. \
        The dominant emotion is {dominant}."

if __name__ == "__main__":
    app.run(port=5000)

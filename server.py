from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Analyzer")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    #emotion_result = "\n".join(f"{key}: {value}" for key, value in response.items())
    dom_emotion = None
    emotions = []

    for key, value in response.items():
        if key == "dominant_emotion":
            dom_emotion = value
        else:
            emotions.append(f"{key}: {value}")

    emotion_result = "\n".join(emotions)

    return "For the given statement, the system response is." , emotion_result, "The dominant emotion is ", dom_emotion ,"."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
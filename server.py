from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')
    
    if text_to_analyze is None:
        return "Invalid text! Please try again!"
    
    if text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"
    
    result = emotion_detector(text_to_analyze)
    
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    
    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
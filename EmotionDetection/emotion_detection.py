import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = input, headers = headers)
    if response.status_code == 400:
        return {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}
    response_emotion_predictor = json.loads(response.text)["emotionPredictions"][0]["emotion"]
    score_max = 0
    emotion_max = None
    for emotion, score in response_emotion_predictor.items():
        if score > score_max:
            score_max = score
            emotion_max = emotion
    response_emotion_predictor["dominant_emotion"] = emotion_max
    return response_emotion_predictor

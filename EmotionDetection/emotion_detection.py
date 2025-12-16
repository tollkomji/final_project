import requests
import json


def emotion_detector(text_to_analyze):
  
    # URL та заголовки для запиту
    url = ('https://sn-watson-emotion.labs.skills.network/v1/'
           'watson.runtime.nlp.v1/NlpService/EmotionPredict')
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Підготовка вхідних даних
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    try:
        # Відправка POST-запиту
        response = requests.post(url, headers=headers, json=input_json, timeout=10)
        
        # Обробка статусу відповіді
        status_code = response.status_code
        
        if status_code == 400 or text_to_analyze.strip() == "":
            # Повертаємо словник з None для всіх значень
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        
        if status_code == 200:
            # Конвертуємо JSON-текст в словник
            response_dict = json.loads(response.text)
            
            # Витягуємо емоції з відповіді
            emotions = response_dict['emotionPredictions'][0]['emotion']
            
            # Отримуємо бали для кожної емоції
            anger_score = emotions['anger']
            disgust_score = emotions['disgust']
            fear_score = emotions['fear']
            joy_score = emotions['joy']
            sadness_score = emotions['sadness']
            
            # Створюємо словник з емоціями
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            
            # Знаходимо домінуючу емоцію
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            
            # Додаємо домінуючу емоцію до результату
            emotion_scores['dominant_emotion'] = dominant_emotion
            
            return emotion_scores
        
        # Для інших кодів статусу
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
            
    except (requests.exceptions.RequestException, KeyError, json.JSONDecodeError):
        # Обробка помилок
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
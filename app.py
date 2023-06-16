from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
import pickle
import random

app = Flask(__name__)

# Memuat model dan tokenizer
model = load_model('my_model.h5')
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Memuat Label Encoder
with open('label_encoder.pickle', 'rb') as le:
    encoder = pickle.load(le)

# Predict response
def generate_response(text):
    sequences = tokenizer.texts_to_sequences([text])
    padded_sequences = pad_sequences(sequences, maxlen=20, truncating='post')
    prediction = model.predict(padded_sequences)
    predicted_label = encoder.classes_[np.argmax(prediction)]
    return predicted_label

def generate_alternative_response(emotion):
    if emotion == "fear":
        alternative_responses = [
            "Perhaps the feeling of fear arises due to uncertainty in the situation. You can try to find ways to address it by seeking more information.",
            "Fear is a natural response to challenging situations. Try to identify the root of the problem and seek support from your loved ones.",
            "Don't let fear hold you back. Face your fears bravely and find ways to overcome them gradually."
        ]
    elif emotion == "joy":
        alternative_responses = [
            "Joy is an incredible gift. Fully embrace and enjoy the moment, and share your happiness with your loved ones.",
            "Joy brings positive energy into our lives. Keep seeking activities and experiences that bring you happiness and gratitude.",
            "When you feel joyful, don't hesitate to spread happiness to others. Kindness and joy can inspire those around you."
        ]
    elif emotion == "anger":
        alternative_responses = [
            "When experiencing anger, try to pause and slowly manage it. Communicate calmly and search for better solutions.",
            "Anger is a natural emotion, but it's important to manage it effectively. Find ways to express your feelings calmly and constructively.",
            "Managing anger is a challenge, but you can do it. Take time to reflect, practice relaxation techniques, or talk to someone who can provide support."
        ]
    elif emotion == "sadness":
        alternative_responses = [
            "Sadness is a natural part of life. Allow yourself to feel it, but remember to seek support and maintain emotional balance.",
            "In moments of sadness, it's important to take care of your mental and physical health. Find ways to indulge yourself and interact with loved ones.",
            "You're not alone in this feeling of sadness. If needed, seek professional help to assist you in the healing process and find ways to regain happiness."
        ]
    else:
        alternative_responses = [
            "I understand that you're feeling something unique right now. It may be helpful to reflect on your emotions and seek support from loved ones.",
            "Every emotion has its own significance. Take the time to explore and understand your feelings, and remember that you're not alone in your experiences.",
            "Emotions can be complex, and it's okay to have a mixture of feelings. Be kind to yourself and give yourself space to process and navigate through your emotions."
        ]
    
    alternative_response = random.choice(alternative_responses)
    return alternative_response

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data['input']

    response = generate_response(user_input)
    alternative_response = generate_alternative_response(response)

    return jsonify({'response': response, 'alternative_response': alternative_response})

if __name__ == '__main__':
    app.run()
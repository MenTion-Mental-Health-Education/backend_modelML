from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import sklearn as sklearn
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

app = Flask(__name__)

# Memuat model dan tokenizer
model = load_model('my_model.h5')
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Memuat Label Encoder
with open('label_encoder.pickle', 'rb') as le:
    encoder = pickle.load(le)

# Predict the emotion
def predict_emotion(text):
    # Mengubah text menjadi sequence
    sequences = tokenizer.texts_to_sequences([text])
    # Padding sequence
    padded_sequences = pad_sequences(sequences, maxlen=20, truncating='post')
    # Membuat prediksi
    prediction = model.predict(padded_sequences)
    # Mengambil label dengan probabilitas tertinggi
    predicted_label = encoder.classes_[np.argmax(prediction)]
    return predicted_label

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']
    response = predict_emotion(text)
    return jsonify({'emotion': response})

if __name__ == '__main__':
    app.run()
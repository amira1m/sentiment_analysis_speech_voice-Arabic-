from keras.src.utils import pad_sequences

from model import *
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/ConvertVoiceToText',methods=['POST'])
def function_kkk():
    print("Start Resolve text")
    ayhaga = request.form["text"]
    loaded_model = tf.keras.models.load_model("my_model")
    sentence = [ayhaga]
    sequences = tokenizer.texts_to_sequences(sentence)
    padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)
    output = loaded_model.predict(padded)
    print(output)
    if (output >0.6):
       return "ايجابي"
    else: return "سلبي"


@app.route('/GetTestMethod',methods=['GET'])
def function_Get():
    return "Test"




if __name__ == "__main__":
    app.run(host="0.0.0.0")




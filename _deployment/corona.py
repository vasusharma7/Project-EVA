import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import re
import pickle

# dataset coronavirus WHO
pd.set_option('max_colwidth', 200)  # Increase column width
data = pd.read_excel("WHO_FAQ.xlsx", encoding='utf8')
data.head()


def preprocess_sentences(input_sentences):
    return [re.sub(r'(covid-19|covid)', 'coronavirus', input_sentence, flags=re.I) 
            for input_sentence in input_sentences]
        
# Load module containing USE
module = hub.load('https://tfhub.dev/google/universal-sentence-encoder-multilingual-qa/3')

# Create response embeddings
response_encodings = module.signatures['response_encoder'](
        input=tf.constant(preprocess_sentences(data.Answer)),
        context=tf.constant(preprocess_sentences(data.Context)))['outputs']
print(response_encodings)


# with open("encodings.pkl") as file:
#   pickle.dump({"encodings" : response_encodings},file)

# with open("encodings.pkl") as file:
#   encodings = pickle.load(file)
#   print(encodings)



def get_answer(question):
  question_encodings = module.signatures['question_encoder'](
      tf.constant(preprocess_sentences([question]))
  )['outputs']
  return data.Answer[np.argmax(np.inner(question_encodings, response_encodings), axis=1)]
if __name__ == "__main__":
  get_answer('How is corona virus transmitted')

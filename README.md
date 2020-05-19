# PPL_Project_2020

Your personal Assistant and chatbot

# Suppoted Platforms 
  - Windows Native GUI Application - Chatbot + Assistant
  - Android App - Chatbot
  - Chatbot Deployed on WhatsApp - +1 415 523 8886
  
# Assistant
 - Just a replica of known assitants - Siri, Cortana, Google Assitant etc.

# Chatbot
 - General Purpose Chatbot
 - Can chat like any other human friend with you.
 - Can send emojis 
 - Trained on Reddit Data
The chatbot is trained on Reddit Data using Tensorflow Neural Machine Translation (nmt) .It uses a concept that training a chatbot is similar to training a machine translation (Engish - Japanese) model , the differnce being that it is English - English translation.The training data had 740k samples of question-answer pairs. Its training files were prepared on google Colab. The Chatbot was trained on 512x3 neural network for 100k epochs with batch size of 64. It was trainedon AWS t2xLarge for about 10 days ( non-GPU ). The hyperparameters were set to fit the constraints of the server we had.(16gb RAM). It can be improved if the number of epochs are increased as there was enough data.




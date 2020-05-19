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
 - You can try chatbot in GUI mode, through Android App and also in CLI mode.
 
 
The chatbot is trained on Reddit Data using Tensorflow Neural Machine Translation (nmt) .It uses a concept that training a chatbot is similar to training a machine translation (Engish - Japanese) model , the differnce being that it is English - English translation.The training data had 740k samples of question-answer pairs. Its training files were prepared on google Colab. The Chatbot was trained on 512x3 neural network for 100k epochs with batch size of 64. It was trainedon AWS t2xLarge for about 10 days ( non-GPU ). The hyperparameters were set to fit the constraints of the server we had.(16GB RAM). It can be improved if the number of epochs are increased as there was enough data.

Since Reddit data is a little slang and doesn't contain proper answers to some trivial qustions, same is true for out chatbot also.

To chat with EVA, Download the App from here - [EVA-Chatbot
](https://drive.google.com/file/d/1texcg1mpMae6LmStEbK8IwDS_M1rKGXo/view?usp=drive_open)
Next, We are working on to make chatbot a bit specific to answer health related queries of people like queries regarding a particular disease, Corona Virus etc. Even the model to answer corona virus related questions is ready but we could not deploy that live due to server constraints.




 






# Chatbot Deployment with Flask and JavaScript
## Initial Setup:
This repo currently contains the files for a chatbot.
Initially we need to create a virtual environment and install all the dependencies there.
```
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk
```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
```
To run the project:
This project uses gpt-3.5 model , but in case of api call fail cases , custom chat bot runs.
To train the model for the custom data set.
The custom data is stored in intents.json file.
```
$ (venv) python train.py
```
To test the chatbot on console:
```
$ (venv) python chat.py
```
Type "quit" to quit the conversation.
Initially ask - "what do you do?" or" what do you sell?" to check the chatbot.
To run the chatbot on local server:
```
$ (venv) python app.py
```
Chatbot button is present in the rightmost down corner of the webpage.

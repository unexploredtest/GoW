## Grapes of Wrath

![sample](https://github.com/aliPMPAINT/GoW/blob/master/readme-assests/screenshot.png)

A web chatbot using django. You can also use your desired chatbot model (written in python). If you wanted to use the default one, please refer to [here](/home/alipmpaint/Documents/github/aliPMPAINT/GoW/chatbotAPI/model/README.md).

### Installation guide:

Clone the repository and make a virtual environment:
```
git clone https://github.com/aliPMPAINT/GoW.git
cd GoW
virtualenv GoW_venv
```

For Linux/Mac:
```
source GoW_venv/bin/activate
```

For Windows:
```
.\GoW_venv\Scripts\activate
```

Then install the dependencies:
```
pip install -r requirements.txt
```

Start the server:
```
python manage.py runserver
```

### The UI in use is [this](https://github.com/aliPMPAINT/WebChatUI) a fork from [here](https://github.com/LandyGuo/WebChatUI)

Special thanks to [LandyGuo](https://github.com/LandyGuo/WebChatUI)

### To do

- [x] Nice UI and works on the front-end
- [x] Instructions on how to use any desired chatbot model and add a default one
- [ ] Add a database and store the chats
- [ ] Having the ability to train the chatbot based on the new data
- [ ] Deploying it


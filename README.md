# flask-chatbot

Simple chatbot api using flask

## How To Run the API

### Ready-built docker image
1. Run on terminal :
```
docker pull nobelf27/flask-chatbot:latest
```
2. Run :
```
docker run -p 5000:5000 nobelf27/flask-chatbot
```

### Without using docker

1. Install dependencies, run on terminal :
```
pip3 install -r requirements.txt
```
2. Start the flask server, run :
```
python3 -m flask run
```

the API will run on port 5000

## Testing the API
The API uses SocketIO as websocket technology to provide full-duplex communication.

1. Open front.html
2. Enter 'password123' as the password to establish the connection

    the password is not saved on the browser and the validation is done fully on the server side.
3. Send the bot messages, the bot replies according to the question-answer pairs saved in file qa.sqlite3

    | Question | Answer   |
    | :---:   | :---: |
    | what's your name? | my name is mochi   |
    | how old are you | im 5   |
    | what is your favorite food | I love meatt   |
    | what are your hobbies? | I like sleeping a lot, eating   |
    | pizza | my favorite italian dish!   |

4. If the user does not send any messages within 10 seconds, the bot will send message "are you there?" to the user.
    it is done to prove the connection between the front and the API server is full-duplex.

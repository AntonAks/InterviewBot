# InterviewBot




InterviewBot - is a Python program for interviewing candidates. It allows you to create questions, record candidates' answers and save interview results.

## Installation

First clone this repository to your computer:

```
git clone https://github.com/AntonAks/InterviewBot.git
```

Starts docker-compose:
```
docker-compose up -d
```


Go to the project directory:
```
cd InterviewBot
```

Activate your Poetry virtual environment:
```
poetry shell
```

Install dependencies:
```
poetry install fastapi, uvicorn, asyncpg,
```

## Using
Run the main program file:
```
python main.py
```
Go to http://localhost:8000/docs in your web browser.

Now you can create questions, conduct interviews and view results through the user interface.
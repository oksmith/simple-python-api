# Simple Python API

A simple Python API using fastapi. Everything in this repo is a bit pointless but should serve as an illustration to build proper apps in the future.

## User guide

### Step 1
Create a Python 3.12 environment which has the packages in `requirements.txt` installed (`pip install -r requirements.txt`).

### Step 2
Activate the virtual environment, and then `python main.py` to start the app.

### Step 3
To use the app, you can call the `calculate` endpoint. To do this, run the following example commands in a new terminal:
```console
foo@bar:~$ curl -X POST "http://127.0.0.1:8000/calculate" -H "Content-Type: application/json" -d '{"n": 5}'
```
And you can send additional inputs to change the default ones if you want to. For example:
```console
foo@bar:~$ curl -X POST "http://127.0.0.1:8000/calculate" -H "Content-Type: application/json" -d '{"n": 5, "env_param": 6.2}'
```

There is data validation built in which means if you send a parameter which does not take an expected value you'll expect information in the response's `msg` about that.
```console
foo@bar:~$ curl -X POST "http://127.0.0.1:8000/calculate" -H "Content-Type: application/json" -d '{"n": 5, "colour": "green"}'
{"detail":[{"type":"enum","loc":["body","colour"],"msg":"Input should be 'red' or 'blue'","input":"green","ctx":{"expected":"'red' or 'blue'"}}]}
```
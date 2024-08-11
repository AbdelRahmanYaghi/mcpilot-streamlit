from flask import Flask,request
import os
from res import assist_res
import dotenv
import subprocess

app = Flask(__name__)

@app.route("/res",methods = ['POST'])
def assis():

    res = request.get_json()
    print(res["messages"][1]["content"])
    result = assist_res(res["messages"][1]["content"])

# the Json format will be as this (The last Lamda accept this format)
# {
#         "channel": "IVR",
#         "session_id":"0000000 not used here",
#         "messages": [
            
#             {
                
#             "role": "assistant",
#             "content": "LastMsg:  last response from system for later usgae (not necessary  here)"
#             },
            
#             {
#                 "role": "user",
#                 "content":  "user message"
#             }
#         ]
#     }

    return f"{result}"


@app.route("/reload", methods = ["GET"])

def reload():
  subprocess.run(["flask", "run"])

  return "reload"


@app.route("/", methods = ['GET'])

def wel():
    return "Welcome"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
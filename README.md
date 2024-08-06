Communication Contract

1) REQUEST data from the Flask server
  a) Start micro_server.py
  b) Start micro_client.py, which connects to HTTP endpoint, port 5555
  c) Client sends a POST request data to the server, which then processed and a response is sent back
  d) Example call:
     request = {'info': 'get_plant_info', 'name': plant_name}
     response = requests.post('http://localhost:5555/api', json=request)
     - The requests Python library is used to send HTTP post requests to microservice server
     - Request is in Python dictionary format, easily converted to json
     - 'json=request' This sends the dictionary 'request' to the server
2) RECEIVE data from the client
  a) Start the client, micro_client.py
  b) After making a selection, a response is sent back from the server and received by the client
  c) The response is then printed for the user to see: print(response.json())

3) Mitigation Plan
   a) This microservice is for my teammate Andrew Rodrigues.
   b) The microservice has been completed.
   c) n/a
   d) This microservice can be accessed through my GitHub, and run locally. A web app or similar can
   access the HTTP endpoint if needed.
   e) I will be available to help access the microservice if needed. I am available 5pm - 10pm PST.
   f) Let me know if there is trouble with the microservice within the next week.
   g) I am new to Flask, but think I have completed a working program. I am assuming you will be using a
   web app, I hope this works well for you. As a backup, I have a working version which does not use Flask,
   instead has ZeroMQ, but this does not have HTTP endpoint.

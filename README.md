# FastAPI_and_SocketIO
A server hosts a FastAPI application and multiple clients can be connected to it via SocketIO.
<br>
Executing `server.py` sets up the server up and running along with the initialization of the FastAPI application.
<br>
When we execute the `client1.py`, it creates individual clients who can send and recieve data between clients and the server.
<br>
NOTE: each execution of `client1.py` will start up a new client.
<br>
All of the clients run coherently in the same session of the API.
<br>
The file `main.py` has the contents for the API.
<br>
The file `models.py` contains the frame of the database which uses `pydantic`.

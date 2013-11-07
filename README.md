simple-pyserver
===============

<h3>Simple Python Server</h3>

<b>Concept</b>
<p>simple-pyserver is a simple server (contained in server.py) that accepts HTTP GET requests from a client.  The server then chooses to return a custom-coded 404 error if the file is not found in the right place, or returns the file.</p>

<b>Operation</b>
<p>simple-pyserver utilizes the Python Socket library to accept and receive GET requests.  Currently, the client must request the server with a particular hard-coded port number.  For example, if the server.py is running on your local computer and listening for requests, the address to ping/request the server would be localhost:8889 by default.</p>





This section of the AutoCite Repository contains the files required to run AutoCite as a web service with a web portal.

To run the server, first install the requirements as stated in the requirements.txt in the root directory of the repository. Then install gunicorn3 (if possible).

To run with gunicorn3:
> chmod +x run_deployment_server.sh
> ./run_deployment_server

To run directly from python flask
> python3 autocite_server.py

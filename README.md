Very simple server registrar for https://github.com/eamonnmr/project_orinoco

and whatever else you want to use it for. Made with Redis and Fastapi.

GPL'd.

To run locally (Python 3.8)

`pip install -r requirements.txt`

`uvicorn server_tracker.main:app`

To Deploy to a server:

Run `deploy.yml`, probably changing `inventory` to point to a server you can ssh into.



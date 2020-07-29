Very simple server registrar for https://github.com/eamonnmr/orbital_fortress

and whatever else you want to use it for. Made with Redis and Fastapi.

GPL'd.

To run locally (Python 3.8)

`pip install -r requirements.txt`

`uvicorn server_tracker.main:app`

To Deploy to a server:

Run `deploy.yml`, probably changing `inventory` to point to a server you can ssh into. Also make sure the hostname in the configs matches the hostname of your server.



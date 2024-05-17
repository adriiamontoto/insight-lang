"""
Start application module.
"""
from uvicorn import run as uvicorn_run

from app.database import create_database

if __name__ == '__main__':
    create_database()

    uvicorn_run(app='app.app:app', host='0.0.0.0', port=80, log_level='info', reload=True, reload_delay=2)

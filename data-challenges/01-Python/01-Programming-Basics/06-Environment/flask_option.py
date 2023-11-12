# pylint: disable=missing-docstring

import os

def start():
    Set = False
    if Set==True:
        os.environ['FLASK_ENV'] = 'development'
        return "Starting in development mode..."
    else:
        Set =False
        os.environ['FLASK_ENV'] = 'production'
        return "Starting in production mode..."

if __name__ == "__main__":
    print(start())

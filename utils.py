# https://stackoverflow.com/questions/15562446/how-to-stop-flask-application-without-using-ctrl-c

# RUN THIS FILE TO SHUT DOWN RUNNING FLASK SERVER
from flask import request


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


def shutdown():
    shutdown_server()
    return 'Server shutting down...'


shutdown()

# from app import create_app
#
#
# app = create_app('config')
#
#
# if __name__ == '__main__':
#     app.run(host=app.config['HOST'],
#             port=app.config['PORT'],
#             debug=app.config['DEBUG'])

from flask_script import Manager

from app import app


manager = Manager(app)


@manager.option('-p', '--port', help='Server port')
@manager.option('-h', '--host', help='Server host')
def runserver(host, port):
    app.run(host, port, debug=True)


if __name__ == "__main__":
    manager.run()

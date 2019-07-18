from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from core.app import app
from core.models.models import db


manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.option('-p', '--port', help='Server port')
@manager.option('-h', '--host', help='Server host')
def runserver(host, port):
    app.run(host, port)


if __name__ == '__main__':
    manager.run()

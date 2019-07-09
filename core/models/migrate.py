from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from core.models.models import db
from core.manage import app


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

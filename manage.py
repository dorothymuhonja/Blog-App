from app import create_app, db
from app.models import User,Role,Blog,Comment


app = create_app('development')
migrate = Migrate(app,db)

manager = manager(app)
manager.add_command('db', MigrationCommand)
manager.add_command('server',Server)

manager.shell
def make_shell_context():
    return dict(app=app,User=User,Role=Role,Blog=Blog,Comment=Comment)

manager.add_command('server', Server)
@manager.command
def test():
    import unittest
    test = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(test)

if __name__ == '__main__':
    manager.run()
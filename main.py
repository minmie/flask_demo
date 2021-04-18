from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_demo import create_app, db

app = create_app('develop')
# 创建flask脚本管理工具对象
manager = Manager(app  )
# 创建数据库迁移工具对象
Migrate(app, db)
# 向manager对象中添加数据库的操作命令
manager.add_command('db',MigrateCommand)






if __name__ == '__main__':
    # manager.run()
    app.run()

    """
    python main.py db init 
    python main.py db migrate  # 类似django的 makermigrations ，即生成迁移文件
    python main.py db upgrade  # 类似django的 migrate，提交迁移到数据库
    
    """
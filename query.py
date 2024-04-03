import db
from sqlalchemy import func

def add_task(user_id,task):
    max_task_id = db.session.query(func.max(db.Task.task_id)).filter(db.Task.user_id==user_id).scalar()or 0
    max_task_id += 1
    new_task = db.Task(text=task,user_id=user_id,task_id = max_task_id)
    db.session.add(new_task)
    db.session.commit()

def remove_task(user_id,task):
    remove_task = db.session.query(db.Task).filter_by(user_id=user_id,task_id=task).first()
    if remove_task:    
        task_too_update = db.session.query(db.Task).filter(user_id==user_id,db.Task.task_id>task).all()
        for x in task_too_update:
            x.task_id -= 1
        db.session.delete(remove_task)
        db.session.commit()
        return "Задача успешно удалена"
    else:
        return "Такой задачи нет"

def view_task(user_id):
    view_task = db.session.query(db.Task).filter_by(user_id=user_id).all()
    id_text = ""
    for x in view_task:    
        id_text += f"{x.task_id} {x.text}" 
    return id_text

def user_add(user_id):
    if not db.session.query(db.User).filter_by(user_id=user_id).first():
        user = db.User(user_id=user_id)
        db.session.add(user)
        db.session.commit()

def change_task(user_id,task_id,task):
    print(user_id,task,task_id)
    change_task = db.session.query(db.Task).filter_by(user_id=user_id,task_id=task_id).first()
    print(change_task)
    change_task.text = task
    db.session.commit()
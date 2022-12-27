from ..backend.celery import app


@app.task
def send_selery():
    print("send_selery")
from {{ project_name }}.celery import celery as app


@app.task(queue='sample-queue')
def sample_task(*args, **kwargs):
    print('Teste!!', args, kwargs)

Django2 Starter Template
========================

Requirements
------------
* Python 3
* Django 2

Instructions
------------
Create a django project:

    django-admin startproject --template= --extension=py,sh,md,env <project_name>
  
Go into the project directory:

    cd <project_name>

Execute the startup script:

    ./start.sh
    
Install all the dependencies:

    pip install -r requirements/dev.txt
    
Run celery:

    python -m celery -A {{ project_name }} worker -B -Q sample-queue -l info
    
Done!
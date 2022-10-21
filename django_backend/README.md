# How to run Django with Python

## Steps

1 - Python Installation

2 - Installing anaconda and creating conda environment

3 - Run Django project

## 1 - Python Installation

If you still don't have python in your windows system, please refer to this [youtube tutorial](https://youtu.be/Kn1HF3oD19c)

After sucessfully installed, you should be able to run below command in your terminal.

```bash
python --version
```

## 2 - Installing anaconda and creating conda environment

Change your current working directory to **django_backend** in your terminal.

If you don't have anaconda in your windows system, please refer to this [youtube tutorial](https://youtu.be/C4OPn58BLaU)

After successful installation, open anaconda prompt and type below commands to create a new anaconda environment.

*Note: you can give your environment name whatever you want, in the example, the name is **uow_itpm***

Run line by line

```bash
conda create uow_itpm python=3.8.13 \\Create a new env
conda activate uow_itpm \\ open your created env
pip install -r requirements.txt \\ install required libaries into your env
```


## Run

After all the setup, run below command to open Django web application
```
python manage.py  runserver
```

and follow your ip address as shown in your anaconda prompt and copy the link in your browser.

Sample output from my terminal

```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 21, 2022 - 14:43:35
Django version 4.1.1, using settings 'main.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
 ```

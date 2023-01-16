# API Test Automation Framework with Python

This is a Test Automation Framework with `Python` that is used to automate CRUD APIs

## 🚀 Description:

Automated CRUD (i.e., `POST`, `GET`, `PUT`, `DELETE`) APIs using `python`

## 🚀 Prerequisites:

`requests` `pytest` `assertpy` `python-dotenv`

## 🚀 Project Structure:

```
api-framework-python/
├─ services/
│  ├─ restful_booker/
│  │  ├─ __init__.py
│  │  ├─ restful_booker_service.py
│  ├─ __init__.py
│  ├─ base_service.py
├─ tests/
│  ├─ data/
│  │  ├─ create_booking.json
│  │  ├─ update_booking.json
│  ├─ __init__.py
│  ├─ test_restful_booker_crud_operation.py
├─ utils/
│  ├─ __init__.py
│  ├─ file_reader.py
│  ├─ request.py
├─ .env
├─ .gitignore
├─ config.py
├─ conftest.py
├─ LICENSE
├─ Pipfile
├─ Pipfile.lock
├─ README.md
```

## 🚀 Test Execution:

- [Fork](https://github.com/ashikkumar23/api-framework-python/fork) and Clone the repository https://github.com/ashikkumar23/api-framework-python
- Open [Pycharm](https://www.jetbrains.com/pycharm/) (or any IDE) > File > Open > Open the project where the repository is located (i.e., `../api-framework-python`)
- On the `Pycharm` terminal, navigate to the `tests` directory via `cd tests`
- Make sure a one-time [Installation](https://github.com/ashikkumar23/api-framework-python#-installation-steps) is performed before executing the tests
- On the `Pycharm` terminal, run the command: `python -m pytest -v`

## 🚀 Installation Steps:

- For Mac: Install `pipenv` via `homebrew`

```commandline
brew install pipenv
```

- For Windows: Install `pipenv` via `pip`

```commandline
pip install pipenv
```

- Create a home directory

```commandline
mkdir ~/.virtualenvs
```

- Add below in `~/.zshrc` or `~/.bash_profile` (if on Mac/Linux) or your Windows system variables

```commandline
export WORKON_HOME=~/virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
```

- Source the above changes

```commandline
source ~/.zshrc
```

- Create a new project using Python 3.8

```commandline
pipenv --python 3.8
```

- Activate virtualenv

```commandline
pipenv shell
```

- Install all dependencies in your virtualenv

```commandline
pipenv install
```

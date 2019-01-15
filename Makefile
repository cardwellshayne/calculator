init:
    pip install pipenv
    pipenv install

test:
    pipenv install --dev
    py.test tests
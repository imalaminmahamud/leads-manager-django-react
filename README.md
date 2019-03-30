### Python Test Coverage

```shell
pip install coverage
```

1. test for coverage
```shell
coverage run --source='.' manage.py test
coverage html
```

2. Open `./htmlcov/index.html`
3. See the report in command line
```shell
coverage report
```
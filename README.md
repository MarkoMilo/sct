# README

The project is about data verification. It is checked whether the generated data is entered correctly in the database. The project is made on Windows 10 OS

# Requirements

Python 10
MySqlConnector https://dev.mysql.com/downloads/connector/j/
Docker https://github.com/jstormes/php-docker-compose/blob/main/Documentation/01a_InstallingDockerOnWindows.md

# Run application
In the git root/zadatak run:
```bash
docker-compose up
```
In the git root folder, open cmd and run the following command:
```bash
pip install pipenv
pipenv shell
pipenv install
main.py
```

### NOTE: The test is not completely finished, running the command will not give the desired results. The plan is to perform an automated check and generate an test report. 
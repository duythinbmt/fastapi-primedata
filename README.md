# About the project
Build a Launch Ordering Webapp with FastAPI
## Technology
- API: FastAPI 
- Database: Postgres
- Language: Python 3
- Database host: Heroku

## Schemas

## Getting Started
### Prerequisites
```
psycopg2==2.9.3
psycopg2-binary==2.9.3
SQLAlchemy==1.4.32
```
### Installation
1. Clone the repository:
   ```
   git clone https://github.com/duythinbmt/fastapi-primedata.git
   ```
2. Install prerequisites:
    ```
    cd fastapi-primedata
    pip install requirements.txt
    ```
## Run
In the same directory as project:
```
uvicorn fastapi-primedata.main:app --reload
```
Then, go through Swagger UI: http://127.0.0.1:8000/docs

![](https://github.com/duythinbmt/fastapi-primedata/blob/main/docs/swagger.png?raw=true)

# About the project
Build a Launch Ordering Webapp with FastAPI
## Technology
- API: FastAPI 
- Database: Postgres
- Language: Python 3
- Database host: Heroku

## Schemas
![](https://github.com/duythinbmt/fastapi-primedata/blob/main/docs/schemas.png?raw=true)
## Getting Started
### Prerequisites
```
anyio==3.6.1
asgiref==3.5.1
click==8.1.3
dnspython==2.2.1
email-validator==1.2.1
fastapi==0.77.1
greenlet==1.1.2
h11==0.13.0
httptools==0.4.0
idna==3.3
psycopg2-binary==2.9.3
pydantic==1.9.0
python-dotenv==0.20.0
PyYAML==6.0
sniffio==1.2.0
SQLAlchemy==1.4.36
starlette==0.19.1
typing-extensions==4.2.0
uvicorn==0.17.6
uvloop==0.16.0
watchgod==0.8.2
websockets==10.3
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

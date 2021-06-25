# Stocks Search

## Approach
1. I first started with the backend. Created the model and the command to import the data at [import.py](backend/stocks/management/commands/import.py).
2. I split the command in several functions. One that takes a nseindia.com zip url and returns all the stocks. Another one that build the url from a date object. And so on.
3. After that I create the API endpoint to search using Django ORM and filters.
4. Later on I went and created the frontend using create-react-app. I added all the libraries and components.
5. Finally i created both frontend/backend Dockerfiles and a docker-compose.yuml to deploy it on my server.

## Deployment
### Using Docker
1. Clone repository.  
`git clone && cd stocks`  
2. Run services.   
`docker-compose up -d`  
3. Run migrations.   
`docker exec -it stocks_api python manage.py migrate`   
4. Run import (by default imports 30 days from nseindia.com).  
`docker exec -it stocks_api python manage.py import`

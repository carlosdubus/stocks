# Stocks Search

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

# Finance APP example

## Introduction
This is a demonstration on how to use several services/technologies used on a
daily basis by a data engineer, the scope of this project is only educational, the
idea is to create a project that involves API consumption and design, Docker to
work with container and cloud services to deploy your app.

## Basic structure
1. Data provider: https://rapidapi.com/sparior/api/yahoo-finance15
   2. **Endpoints of interest: v1/search, v1/stock/history, v1/market/quotes
3. Backend: 
   4. Google Cloud Platform simulating a DB
      4. Google Sheet: Simulating a RDB
      5. Google Drive: to store data snapshots
   6. RabbitMQ: To decouple the Data consumption
   7. Airflow: To orchestrate the data pipline. Not confirmed yet.
   8. Docker: To Containerize the backend app, this will help with consistency
   9. ECR + EC2: To deploy the backend app 
6. Frontend: We will build a Streamlit App for this, to consume stock data from GSheets
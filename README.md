# Finance APP example

## Introduction

In this demonstration we will show an easy decoupling example for a basic pipeline involving realtime data. This
example will consist on ingesting realtime stock market data from a free provider. The project's goal is to show how
to decouple database transactions (in this example only insert) using a message broker, with this approach
we will benefit by reducing the waiting time between API calls, resulting in a much accurate market data in terms of time
precision. Other benefits of this architecture would involve: fault tolerance, reliability, loose coupling,
maintainability, and scalability.


For the purpose of this example we will be working Apple stocks from the NASDAQ stock market.

## Technologies used
1. PostgreSQL: relational database engine
2. RabbitMQ: message broker
3. Docker: to handle PostgreSQL and RabbitMQ images


## Database Structure

<img src="https://github.com/rjpererag/Financial-App-Example/blob/1c4945ae6ec8b4dadd9d83ee6166697dc1f9308c/other_files/db_schema.png"/>

## Data pipeline description
In this example we will be consuming data from a free API provider to simulate a real-time market data, the goal of this
example is to divide the process in two separates services:

#### Data provider: https://rapidapi.com/sparior/api/yahoo-finance15

1. API consumption: in this process we will connect to the API and request data from it.
For this we will create an API consumer following OOP principles to select and validate the data of interest. After
validation, we will handle the message creation so our data can be inserted in our custom database.
2. Database Handler: during this process we will receive and decode the incoming message with the data to insert, to
achieve this we must validate the existence of several datapoints in our auxiliary table, following that we will insert
the incoming real-time market data into our primary table.


## Docker commands:
### PostgreSQL:
docker pull postgres:latest

docker run -d --name my_postgres_db \
  -e POSTGRES_USER=myuser \
  -e POSTGRES_PASSWORD=mypassword \
  -e POSTGRES_DB=mydatabase \
  -p 5432:5432 \
  postgres:latest


### RabbitMQ:
docker pull rabbitmq:latest

docker run -d --name my_rabbitmq \
  -p 5672:5672 \
  -p 15672:15672 \
  -e RABBITMQ_DEFAULT_USER=myuser \
  -e RABBITMQ_DEFAULT_PASS=mypassword \
  rabbitmq:latest


### ENV Variables
RAPIDAPI_KEY: your yahoo finance API Key

DB_USER: your PostgreSQL user (by default myuser)
DB_PASSWORD= your PostgreSQL password (by default mypassword)
DB_NAME: your PostgreSQL database name (by default mydatabase)
DB_PORT: your PostgreSQL port (by default 5432)
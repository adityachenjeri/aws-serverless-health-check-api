# AWS Serverless Cloud Health Check API

A simple serverless health-check API built using Amazon API Gateway and AWS Lambda.

## Architecture

Client
   |
   v
API Gateway
   |
   v
AWS Lambda
   |
   v
JSON Response

## AWS Services

- Amazon API Gateway
- AWS Lambda
- IAM
- Amazon CloudWatch

## API Endpoint

GET /health

## Sample Response

{
    "status": "healthy",
    "service": "AWS Serverless Application",
    "environment": "UAT",
    "timestamp": "2026-09-25T10:57:58.752828"
}

## Lambda Function

The Lambda function is written in Python and returns the health status of the application as a JSON response.

## Key Concepts

- HTTP APIs
- API Gateway routes
- Lambda integration
- Synchronous invocation
- IAM permissions
- CloudWatch logging

## Architecture Flow

Client → API Gateway → Lambda → JSON Response

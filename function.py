import json
from datetime import datetime

def lambda_handler(event, context):

    response = {
        "status": "healthy",
        "service": "AWS Serverless Application",
        "environment": "UAT",
        "timestamp": datetime.utcnow().isoformat()
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response)
    }

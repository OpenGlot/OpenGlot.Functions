import json
import requests
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    api_url = "https://api.beta.openglot.com/api/Languages"

    # Make the HTTP GET request to the API
    response = requests.get(api_url)
    
    # Get the response code and content
    response_code = response.status_code
    response_content = response.text

    # Log the response code and content
    logger.info(f"Response Code: {response_code}")
    logger.info(f"Response Content: {response_content}")

    # Return the response code and content
    return {
        'statusCode': response_code,
        'body': response_content
    }
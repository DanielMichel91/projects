import requests
import boto3
import json

# Create an SNS client
sns = boto3.client('sns')

def lambda_handler(event, context):
    # Get latitude and longitude for Berlin using a geocoding API
    geocoding_url = 'https://geocoding-api.open-meteo.com/v1/search'
    response_geocoding = requests.get(geocoding_url, params={'name': 'Berlin'})
    response_geocoding_json = response_geocoding.json()
    lat = response_geocoding_json['results'][0]['latitude']
    lng = response_geocoding_json['results'][0]['longitude']
    
    # Get daily weather forecast for Berlin using the Open Meteo API
    weather_url = 'https://api.open-meteo.com/v1/forecast?daily=temperature_2m_max,temperature_2m_min&timezone=Europe%2FBerlin'
    response_weather = requests.get(weather_url, params={'latitude': lat, 'longitude': lng})
    weather_data = response_weather.json()
    
    # Extract min and max temperatures from the weather data
    weather_info = {
        'min_temp': weather_data['daily']['temperature_2m_min'],
        'max_temp': weather_data['daily']['temperature_2m_max']
    }
    min_temp = weather_info['min_temp'][0]
    
    # Publish weather information to an SNS topic
    sns.publish(
        TopicArn='arn:aws:sns:eu-central-1:606610296747:weather-email',  # Must be adjusted when creating a new SNS topic
        Subject='Weather Update',
        Message=f'The minimum temperature today in Berlin is {str(min_temp)} °C.'
    )
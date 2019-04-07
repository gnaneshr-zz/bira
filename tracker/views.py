from django.http import HttpResponse, JsonResponse
from django.conf import settings

import json

import requests

def response_to_json(response):
    json_data = json.dumps(response.json())
    return json_data

def make_json_response(data):
    return HttpResponse(data, content_type='application/json')

def data_to_http_json(data):
    return make_json_response(response_to_json(data))

def index(request):
    message = "Hello, You're Awesome, and your token is " + settings.GITHUB_API_TOKEN
    return HttpResponse(message)

def get_all_projects(request):
    organization = "hashedin"
    url = settings.GITHUB_API_URI + "/orgs/" + organization + "/repos"
    headers = {'Authorization': 'token %s' % settings.GITHUB_API_TOKEN}
    r = requests.get(url, headers=headers)
    return data_to_http_json(r)

import requests
from behave import *
import json


@given('the user pings the API and gets status 200')
def api_get(context):

    resp = requests.get("https://jsonplaceholder.typicode.com/todos/")
    assert (resp.status_code == 200), "Status code is not 200. Got : " + str(resp.status_code)


@then('the user validates the JSON output')
def wrong_login(context):

    resp = requests.get("https://jsonplaceholder.typicode.com/todos/")
    raw_output = resp.text
    filtered_output = json.loads(raw_output)
    for i in filtered_output:
        if i['id'] == 5:
            assert not i['completed']





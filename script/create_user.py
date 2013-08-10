import requests
import json
def create_a_user():
    url = "http://localhost:8080/register"
    # url = "http://diabeteselsewhere.appspot.com/register"
    user = {}
    user["userID"] = 12340001
    user["userEmail"] = "test@test.com"
    user["userPassward"] = "12344321"
    requests.post(url, json.dumps(user))

if __name__ == '__main__':
    create_a_user()
#Sources used: https://stackoverflow.com/questions/13941742/rest-post-using-python-request

import requests
import json

def post_info():
    url = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"

    #data in JSON format
    data = {
        "UCID": input("Enter your UCID: ").strip(),
        "first_name": input("Enter your First Name: ").strip(),
        "last_name": input("Enter your Last Name: ").strip(),
        "github_username": input("Enter your GitHub Username: ").strip(),
        "discord_username": input("Enter your Discord Username: ").strip(),
        "favorite_cartoon": input("Enter your Favorite Cartoon: ").strip(),
        "favorite_language": input("Enter your Favorite Programming Language: ").strip(),
        "movie_or_game_or_book": input("Enter your Favorite Movie, Game, or Book: ").strip(),
        "section": input("Enter your Section (101 or 103): ").strip()
    }


    try:
        #sending post request
        response = requests.post(url, json=data, headers={"Content-Type": "application/json"})

        #printing status and responses 
        print(f"Status: {response.status_code}")
        try:
            print("Response JSON:", json.dumps(response.json()))
        except json.JSONDecodeError:
            print("Response Text:", response.text)

    except requests.exceptions.RequestException as e:
        print("Error while sending request:", e)


if __name__ == "__main__":
    post_info()

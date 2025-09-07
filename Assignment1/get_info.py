import requests

def get_student_info(ucid, section):
    # API endpoint with query parameters
    url = f"https://student-info-api.netlify.app/.netlify/functions/submit_student_info?UCID={ucid}&section={section}"

    try:
        # Send GET request
        response = requests.get(url)

        # Print status
        print(f"Status: {response.status_code}")

        # Print response (try JSON first)
        try:
            print("Response JSON:", response.json())
        except Exception:
            print("Response Text:", response.text)

    except requests.exceptions.RequestException as e:
        print("Error while sending GET request:", e)


if __name__ == "__main__":
    # Replace with your actual UCID and section (101 or 103)
    get_student_info("NAW5", "101")

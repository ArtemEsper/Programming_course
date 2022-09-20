import os
import requests

# AUTH_TOKEN = os.environ['AUTH_TOKEN']  # all keys mast be saved in environment variables and never exposed in the code


def main():
    response = requests.get(
        url='http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json'
        # headers={'Authorization': AUTH_TOKEN}
    )
    print("Response status code:", response.status_code)
    print("Response JSON", response.json())


if __name__ == '__main__':
    main()

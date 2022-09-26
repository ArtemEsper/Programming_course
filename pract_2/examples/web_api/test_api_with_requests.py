import os
import requests


# AUTH_TOKEN: str = os.environ['OC_API_AUTH_TOKEN'] # all keys mast be saved in environment variables
# для додавання змінної середовища у терміналі виконати команду (якщо у вас zsh)
# 'export OC_API_AUTH_TOKEN=7a000fb5-b549-4958-9e90-e5c809b7cf0b' >> ~/.zshenv
# source ~/.zshenv
# перевірка echo $OC_API_AUTH_TOKEN
# https://opencitations.net/index/coci/api/v1

def main():
    response = requests.get(
        url='https://opencitations.net/index/coci/api/v1/citations/10.1103/PhysRevLett.113.251301?format=json',
        headers={'Authorization': '7a000fb5-b549-4958-9e90-e5c809b7cf0b'}
    )
    print("Response status code:", response.status_code)
    print("Response JSON", response.json())


if __name__ == '__main__':
    main()

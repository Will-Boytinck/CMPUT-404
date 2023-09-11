import requests

def main():
    print(requests.__version__)
    google_request = requests.get("https://www.google.com")
    print(google_request)
    code_request = requests.get("https://raw.githubusercontent.com/Will-Boytinck/CMPUT-404/main/Lab1/requests_demo.py")
    data = code_request.text
    print(data)
    
if __name__ == "__main__":
    main()

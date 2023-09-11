import requests

def main():
    print(requests.__version__)
    google_request = requests.get("https://www.google.com")
    print(google_request)
    
if __name__ == "__main__":
    main()

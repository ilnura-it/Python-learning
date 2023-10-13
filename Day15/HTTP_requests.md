# HTTP requests with Python

Using the requests Module

      python3 -m pip install requests

      import requests
      response = requests.get("http://dkfgdjgdkj")
      response # <Response [200]>

      response.headers

      response.text # will give while html

## Query String

- Option1
            import requests

            response = requests.get(
                  "http://www.example.com?key1=value1&key2=value2
            )

- Option2

            import requests

            response = requests.get(
                  "http://www.example.com",
                  params={
                        "key1" : "value1",
                        "key2" : "value2"
                  }
            )
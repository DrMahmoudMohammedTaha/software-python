

# #!/usr/bin/env python

# import requests as req

# resp = req.post("http://localhost:8000")

# print(resp.text)


# import os
# import requests

# os.environ['NO_PROXY'] = '127.0.0.1'
# r = requests.get('http://127.0.0.1:8000')
# print(r.content)


# import requests
# receive = requests.get('https://imgs.xkcd.com/comics/making_progress.png')
# with open(r'C:\\Users\\El-Wattaneya\\Downloads\\New folder\\image5.png','wb') as f:
#     f.write(receive.content)

import requests
receive = requests.get('http://localhost:8080/?op=asReq&clId=123456789&srvId=987654321')
print(receive.content)
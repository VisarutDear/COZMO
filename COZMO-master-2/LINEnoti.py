import requests
def linenotify():
    url = "https://notify-api.line.me/api/notify"

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"message\"\r\n\r\n Your relative forget to take medicine please contract your relativec to take medicine.\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'Authorization': "Bearer vGgUBwZhsTnYrYs9RHVyO7Nt8XUIKXa2QUaVqAkYIZY",
        'cache-control': "no-cache",
        'Postman-Token': "231012f8-953d-4046-bdf6-9df87d46c0c0"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
# linenotify()
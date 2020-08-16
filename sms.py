import requests
url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message=hello&language=english&route=p&numbers=6261512166"
headers = {
'authorization': "8Wgcw1qJCmMlQEvyRo7Ys9DGPh0OunkNajzKe6ItfHUxX52SAiL2BOMHefg8bzjkv1XPIV3RoATNJi0m",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
import requests

url='https://mineru.net/api/v4/extract/task'
header = {
    'Content-Type':'application/json',
    'Authorization':'Bearer eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiI1MzAwMDg0MyIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTc1MzAwODM1MSwiY2xpZW50SWQiOiJsa3pkeDU3bnZ5MjJqa3BxOXgydyIsInBob25lIjoiMTg5MjQ5Mzk4MDIiLCJvcGVuSWQiOm51bGwsInV1aWQiOiI3ZDczOTNlNC1jZGVlLTRmMWItOTY0MS0yNzhjOWY4Y2NlMTgiLCJlbWFpbCI6IiIsImV4cCI6MTc1NDIxNzk1MX0.U3O7AiEkhhRalkycAukCYNohx1CSI6hSLh0owABOdgMlQT8RqseEeou8oKhkzVFjRdoRjVsZGQuJZW5aEMiLLA'
}
data = {
    'url':'https://cdn-mineru.openxlab.org.cn/demo/example.pdf',
    'is_ocr':True,
    'enable_formula': False,
}

res = requests.post(url,headers=header,json=data)
print(res.status_code)
print(res.json())
print(res.json()["data"])
import requests
session = requests.Session()
res = session.post(
    url="https://192.168.4.31:8445/PortalServer/Webauth/webAuthAction!login.action",
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; \
            Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0"},
    data={
        "authType":"",
        "userName":input("User Name: "),
        "password":input("Password: "),
        "validCode":"验证码",
        "valideCodeFlag":"false",
        "authLan":"zh_CN",
        "hasValidateNextUpdatePassword":"true",
        "rememberPwd":"false",
        "browserFlag":"zh",
        "hasCheckCode":'false',
        "checkcode":"",
        "hasRsaToken":'false',
        "rsaToken":"",
        "autoLogin":"false",
        "userMac":"",
        "isBoardPage":"false",
        "disablePortalMac":"false",
        "overdueHour":0,
        "overdueMinute":0,
        "isAccountMsgAuth":"",
        "validCodeForAuth":"",
        "isAgreeCheck":1,
    },
    verify=False,
)

print(res.json())
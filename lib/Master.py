

class Proxy:
    PROXY_IP = ""
    PROXY_PORT = "3128"
    PROXY_PROTOCOL = "http"
    PROXY_ID = "instime"
    PROXY_PW = "ozsZ1zwXZzrd"


class Customer:
    id = ""
    name = ""
    instaAccount = ""
    instaPW = ""
    twAccount = ""
    twPW = ""
    keyWord = ""
    status = "" # 0:有効 1:無効
    agentName = ""
    webApplySeq = ""
    webApplyStatus = "" # 1:アカウント設定中 2:無料期間中 3:契約中 4:課金NG 100:未処理 101:停止 102:解約
    webApplyCreatedate = ""
    webApplyUpdatedate = ""
    createdate = ""


class DailyArchive:
    id = ""
    follower = ""
    follow = ""
    post = ""
    customerId = ""
    createdate = ""


class DailyArchiveMaster:
    id = ""
    follower = ""
    follow = ""
    post = ""
    instaAccount = ""
    createdate = ""

class History:
    id = ""
    contents = ""
    createdate =""

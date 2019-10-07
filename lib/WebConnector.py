import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib.ProxyAuthFile import ProxyCode
from lib.Master import Proxy


class WebConnector:

    driver = None
    # TEST USER
    TEST_MASTER_ACCOUNT = "desert_9363"
    TEST_MASTER_PW = "fsY8Fupv"
    # PROXY
    PROXY = ""
    PROXY_FLAG = False
    DRIVER_PATH = ""

    HEADLESS = False

    def __init__(self):
        self.DRIVER_PATH = config.driver_info['path']
        self.PROXY = Proxy()

    def set_headless(self, flag):
        if flag == True:
            self.HEADLESS = True
        else:
            self.HEADLESS = False

    # !proxyのON OFF
    def set_proxy(self, proxy, flag):
        self.PROXY = proxy
        self.PROXY_FLAG = flag


    def readyDriver(self):

        # 次回ログイン用にuser dataを作成

        options = Options()
        if self.HEADLESS:
            options.add_argument('--headless')
        options.add_argument("--start-maximized")
        options.add_argument("--lang=ja")


        if self.PROXY_FLAG:
            server = self.PROXY.PROXY_IP
        else:
            server = ""
        port = self.PROXY.PROXY_PORT
        protocol = self.PROXY.PROXY_PROTOCOL
        proxy = '%s:%s' % (server, port)
        proxy_id = self.PROXY.PROXY_ID
        proxy_pw = self.PROXY.PROXY_PW

        # proxy server authありの場合
        if proxy_id != "" and server != "":
            print("■■■proxy接続（認証あり）■■■")
            proxy_auther = ProxyCode(server, port, proxy_id, proxy_pw)
            pluginfilepath = './proxy_zip/proxy_auth_plugin_%s.zip' % server
            proxy_auther.createZip(pluginfilepath)
            options.add_extension(pluginfilepath)

        elif self.PROXY.PROXY_IP != "":
            print("■■■proxy接続（認証なし）■■■")
            options.add_argument('--proxy-server=%s://%s' % (protocol, proxy))

        else:
            print("■■■proxyなしの接続■■■")
            print("現在のglobal ipでの接続")

        # user agent偽装
        # agent = "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1"
        # options.add_argument('--user-agent=' + agent)

        # ユーザープロファイル保存場所※ログインは最初の一回のみにするために必ずプロファイルを保存。
        # path = "user_data/t_" + self.customer.getTwitterAccountName()
        # # ログイン設定ありなし
        # options.add_argument("user-data-dir=" + path)
        self.driver = webdriver.Chrome(self.DRIVER_PATH,options=options)



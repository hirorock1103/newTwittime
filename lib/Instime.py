from lib.WebConnector import WebConnector
from lib.DbManager import MysqlDbManager
import datetime
from datetime import datetime, date, timedelta
from lib.Master import DailyArchiveMaster
from lib.Master import Customer
from lib.Master import Proxy
from lib.Master import History
from multiprocessing import Process
import threading
import time
import config


class Instime(MysqlDbManager):

    DATA_PATH = r"C:\Users\USER\Desktop\instime_data"
    INSTA_URL = "https://www.twitter.com"


    # INIT
    def __init__(self):
        super().__init__()

        # ArchiveMasterへの追加

    # 顧客をuniqueで取得
    def get_customer(self, conditions = [], args = []):
        query = "SELECT * FROM " + self.TABLE_CUSTOMER

        where = ""
        for condition in conditions:
            if where == "":
                where = " WHERE " + condition
            else:
                where += " AND " + condition

        query += where

        # print(query)
        c = self.con.cursor(dictionary=True)
        c.execute(query, args)
        list = []
        for row in c:
            # print(row)
            customer = Customer()
            customer.id = row[self.COLUMN_CUSTOMER_ID]
            customer.name = row[self.COLUMN_CUSTOMER_NAME]
            customer.instaAccount = row[self.COLUMN_DAILYARCHIVE_INSTA_ACCOUNT]
            customer.twAccount = row[self.COLUMN_CUSTOMER_TW_ACCOUNT]
            customer.instaPW = row[self.COLUMN_CUSTOMER_INSTA_PW]
            customer.twPW = row[self.COLUMN_CUSTOMER_TW_PW]
            customer.keyWord = row[self.COLUMN_CUSTOMER_INSTA_KEYWORD]
            customer.status = row[self.COLUMN_CUSTOMER_STATUS]
            customer.agentName = row[self.COLUMN_CUSTOMER_WEB_AGENT_NAME]
            customer.webApplySeq = row[self.COLUMN_CUSTOMER_WEB_APPLY_SEQ]
            customer.webApplyStatus = row[self.COLUMN_CUSTOMER_WEB_APPLY_STATUS]
            customer.webApplyCreatedate = row[self.COLUMN_CUSTOMER_WEB_APPLY_CREATEDATE]
            customer.webApplyUpdatedate = row[self.COLUMN_CUSTOMER_WEB_APPLY_UPDATEDATE]
            customer.createdate = row[self.COLUMN_CUSTOMER_CREATEDATE]
            list.append(customer)

        return list

    def convert_str_to_date(self, str_date):
        self.logger.log(str_date)
        today = datetime.today()
        ans_date = ""
        # 時間前 / 分前　→　todayとして登録
        if str_date.find("時間前") >= 0 or str_date.find("分前") >= 0:
            self.logger.log("「時間前、分前」が含まれる")
            target_date = today
            ans_date = datetime.strftime(target_date, '%Y-%m-%d')

        # 日前　→　指定日で計算
        elif str_date.find("日前") >= 0:
            count = int(str_date[0:1])
            self.logger.log("「日前」が含まれる")
            target_date = today - timedelta(days=count)
            ans_date = datetime.strftime(target_date, '%Y-%m-%d')

        # 〇年〇月〇日　→　指定年月日
        elif str_date.find("年") >= 0 and str_date.find("月") >= 0 and str_date.find("日") >= 0:
            self.logger.log("指定年月日" + str_date)
            date_string = str_date
            self.logger.log("date_string" + date_string)
            target_date = datetime.strptime(date_string, '%Y年%m月%d日')
            ans_date = datetime.strftime(target_date, '%Y-%m-%d')

        # 〇月〇日　→ 今年の指定年月日
        elif str_date.find("月") >= 0 and str_date.find("日") >= 0:
            self.logger.log("今年の指定年月日" + str_date)
            date_string = str(today.year) + "年" + str_date
            self.logger.log("date_string" + date_string)
            target_date = datetime.strptime(date_string, '%Y年%m月%d日')
            ans_date = datetime.strftime(target_date, '%Y-%m-%d')

        return ans_date

    # リストを取得
    def get_db_tables(self):
        c = self.con.cursor()
        # query = "select name from sqlite_master where type='table'"
        query = "show full tables"
        c.execute(query)
        list = []
        for row in c:
            list.append(row[0])

        return list

    # column
    def get_columns(self, tablename):
        c = self.con.cursor()
        # query = "PRAGMA table_info(%s);" % tablename
        query = "show columns from %s;" % tablename
        c.execute(query)
        list = []
        for row in c:
            list.append(row)
        return list

    # インスタから該当アカウントの情報を取得する
    def browser_action(self, customer_list):

        limit = 20
        process = False
        exelist = []
        count = 1
        for customer in customer_list:
            if count > limit:
                break
            if process:
                p = Process(target=self.headlessTest, args=(customer.twAccount, ))
                if count % 2 == 0:
                    time.sleep(2)
                p.start()
            else:
                exelist.append(
                    threading.Thread(target=self.headlessTest, args=(customer.twAccount,))
                )

            count += 1

        if process == False:
            count = 1
            for exe in exelist:
                exe.start()
                time.sleep(3)
                if count % 2 == 0:
                    time.sleep(15)
                count += 1

    # tw_action
    def tw_action(self, account):
        print("tw_action : " + account)


    # headless test
    def headlessTest(self, account):

        now = datetime.today()
        fmt = now.strftime("%Y%m%d")

        browser = WebConnector()
        browser.set_headless(False)
        proxy = Proxy()
        # proxy.PROXY_IP = "140.227.235.173"
        # browser.set_proxy(proxy, False)
        browser.readyDriver()
        browser.driver.get(self.INSTA_URL + "/" + account)
        time.sleep(3)
        file_name = self.DATA_PATH + "/" + account + "_" + fmt + ".png"
        browser.driver.save_screenshot(file_name)


    # getCustomerFromWeb
    def getCustomerFromWeb(self):
        import requests
        import json
        apply_status = config.web_apply_status
        url = "https://instime.jp/api/get_tw_customer.php?date="
        response = requests.get(url)
        if response.status_code == 200:
            print("※管理画面との通信....success:200\n")
            # json.load  ,  json.loads   ※https://blog.aristo-solutions.net/2018/06/pythonattributeerror-object-has-no_17.html
            list = json.loads(response.text)

            for row in list:
                customer = Customer()
                # print(row)
                customer.instaAccount = row['ac_id']
                customer.instaPW = ""
                customer.twAccount = row['tw_ac_id']
                customer.twPW = ""
                customer.name = row['ac_name']
                customer.status = 0
                customer.webAppczQlyStatus = row['status']
                customer.webApplySeq = row['seq']
                customer.webApplyUpdatedate = row['updatedate']
                customer.webApplyCreatedate = row['createdate']
                customer.keyWord = row['ac_keyword']
                customer.agentName = row['agent_name']
                # print(customer.__dict__)
                # add customer or update customer
                # webseqが同じcusexist targettomerが存在するかをチェック
                target = None
                conditions = []
                args = []
                conditions.append(self.COLUMN_CUSTOMER_WEB_APPLY_SEQ + "= %s")
                args = [customer.webApplySeq, ]
                target = self.search_customer(conditions, args)

                if target.id == "":
                    print("# " + customer.instaAccount)
                    msg = "新規追加されました\n"
                    msg += customer.__dict__.__str__()
                    print(msg)
                    history = History()
                    history.contents = msg
                    self.add_history(history)
                    # add customer
                    insert_id = self.add_customer(customer)
                else:
                    # update customer
                    # 最終更新日を比較してwebが更新されていれば更新する
                    update_flag = False
                    msg = ""
                    if target.webApplyUpdatedate != "":
                        kizon_dt = datetime.strptime(target.webApplyUpdatedate, "%Y-%m-%d %H:%M:%S")
                        web_dt = datetime.strptime(customer.webApplyUpdatedate, "%Y-%m-%d %H:%M:%S")

                        if kizon_dt < web_dt:

                            msg += "# " + customer.instaAccount + "\n"
                            msg +="※WEB管理画面が更新されています" + "\n"
                            # 差分
                            msg +=" - 差分 - " + "\n"
                            before_diff = target.__dict__.items() - customer.__dict__.items()
                            diff = customer.__dict__.items() - target.__dict__.items()
                            msg += dict(before_diff).__str__() + "\n"
                            msg += "↓" + "\n"
                            msg += dict(diff).__str__() + "\n"
                            print(msg)
                            update_flag = True

                    else:
                        update_flag = True

                    # 更新処理
                    if update_flag:
                        self.update_customer(customer, target.id)
                        if msg != "":
                            history = History()
                            history.contents = msg
                            self.add_history(history)

        else:
            print("fail:" + str(response.status_code))

    # update_customer
    def update_customer(self, customer, id):
        query = "UPDATE " + self.TABLE_CUSTOMER + " SET " \
                + self.COLUMN_CUSTOMER_INSTA_ACCOUNT + " =%s ," \
                + self.COLUMN_CUSTOMER_INSTA_PW + " = %s," \
                + self.COLUMN_CUSTOMER_NAME + " = %s," \
                + self.COLUMN_CUSTOMER_STATUS + " = %s," \
                + self.COLUMN_CUSTOMER_WEB_APPLY_STATUS + " = %s," \
                + self.COLUMN_CUSTOMER_WEB_APPLY_SEQ + " = %s," \
                + self.COLUMN_CUSTOMER_WEB_APPLY_UPDATEDATE + " = %s," \
                + self.COLUMN_CUSTOMER_WEB_APPLY_CREATEDATE + " = %s," \
                + self.COLUMN_CUSTOMER_INSTA_KEYWORD + " = %s," \
                + self.COLUMN_CUSTOMER_WEB_AGENT_NAME + " = %s," \
                + self.COLUMN_DAILYARCHIVE_CREATEDATE + " = NOW()" \
                + " WHERE " + self.COLUMN_CUSTOMER_ID + " = %s "
        args = [
            customer.instaAccount,
            customer.instaPW,
            customer.name,
            customer.status,
            customer.webApplyStatus,
            customer.webApplySeq,
            customer.webApplyUpdatedate,
            customer.webApplyCreatedate,
            customer.keyWord,
            customer.agentName,
            id,
        ]
        c = self.con.cursor()
        c.execute(query, args)
        self.con.commit()

    # add customer
    def add_customer(self, customer):
        query = "INSERT INTO " + self.TABLE_CUSTOMER + "(" \
                + self.COLUMN_CUSTOMER_INSTA_ACCOUNT + "," \
                + self.COLUMN_CUSTOMER_INSTA_PW + "," \
                + self.COLUMN_CUSTOMER_TW_ACCOUNT + "," \
                + self.COLUMN_CUSTOMER_TW_PW + "," \
                + self.COLUMN_CUSTOMER_NAME + "," \
                + self.COLUMN_CUSTOMER_STATUS + "," \
                + self.COLUMN_CUSTOMER_WEB_APPLY_STATUS + "," \
                + self.COLUMN_CUSTOMER_WEB_APPLY_SEQ + "," \
                + self.COLUMN_CUSTOMER_WEB_APPLY_UPDATEDATE + "," \
                + self.COLUMN_CUSTOMER_WEB_APPLY_CREATEDATE + "," \
                + self.COLUMN_CUSTOMER_INSTA_KEYWORD + "," \
                + self.COLUMN_CUSTOMER_WEB_AGENT_NAME + "," \
                + self.COLUMN_CUSTOMER_CREATEDATE + "" \
                + ") values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW())"

        c = self.con.cursor()

        args = [
            customer.instaAccount,
            customer.instaPW,
            customer.twAccount,
            customer.twPW,
            customer.name,
            customer.status,
            customer.webApplyStatus,
            customer.webApplySeq,
            customer.webApplyUpdatedate,
            customer.webApplyCreatedate,
            customer.keyWord,
            customer.agentName,
        ]

        c.execute(query, args)
        self.con.commit()

        lastInsertId = c.lastrowid

        return lastInsertId

    # send log
    def api_get_account_info(self, customer_list):
        import requests

        url = "http://133.167.80.198/tw_index_api.php"

        # archive 取得
        for customer in customer_list:
            print("対象アカウント:" + str(customer.instaAccount))
            info = {
                'account': customer.twAccount,
            }
            print(info.__str__())
            r = requests.post(url, data=info)
            print(r.text)

    def send_first_log(self, list):

        # 更新対象カラム　
        # follow_cnt
        # follower_cnt
        # post_cnt
        # service_start_date
        import requests

        # post dataを作成する
        for customer in list:

            archive_list = self.get_archive_list(customer.instaAccount)

            if archive_list.__len__() > 0:
                post_cnt = archive_list[0].post
                follower_cnt = archive_list[0].follower
                follow_cnt = archive_list[0].follow

                print("更新対象SEQ:" + str(customer.webApplySeq))
                situation = {
                    'post_cnt': post_cnt,
                    'follower_cnt': follower_cnt,
                    'follow_cnt': follow_cnt,
                    'seq': customer.webApplySeq
                }
                print(situation.__str__())
                r = requests.post("https://instime.jp/api/send_account_situation.php", data=situation)
                print(r.text)

            else:
                print("ログがないので連携しません。")

    def proxy_test(self, proxy, proxy_flag):

        browser = WebConnector()
        browser.set_proxy(proxy, True)
        browser.set_headless(False)
        browser.readyDriver()
        browser.driver.get("https://www.yahoo.co.jp/")
        time.sleep(15)

    def add_history(self, history):
        # print("DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)")
        # DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)
        query = "INSERT INTO " + self.TABLE_HISTORY + "(" \
                + self.COLUMN_HISTORY_CONTENTS + "," \
                + self.COLUMN_DAILYARCHIVE_CREATEDATE + "" \
                + ") values (%s,NOW())"

        c = self.con.cursor()

        args = [history.contents]

        c.execute(query, args)
        self.con.commit()

        lastInsertId = c.lastrowid

        return lastInsertId

    # 顧客をuniqueで取得
    def get_history(self, conditions = [], args = []):
        query = "SELECT * FROM " + self.TABLE_HISTORY

        where = ""
        for condition in conditions:
            if where == "":
                where = " WHERE " + condition
            else:
                where += " AND " + condition

        query += where
        c = self.con.cursor(dictionary=True)
        c.execute(query, args)
        list = []
        for row in c:
            # print(row)
            history = History()
            history.id = row[self.COLUMN_HISTORY_ID]
            history.contents = row[self.COLUMN_HISTORY_CONTENTS]
            history.createdate = row[self.COLUMN_HISTORY_CREATEDATE]
            list.append(history)
        return list
import sqlite3
import config
import mysql.connector

# 共有DB
class MysqlDbManager:
    # db
    # https://blowup-bbs.com/mysql-connector-python-developer-guide/

    # PostList
    TABLE_PostList = "PostList"
    COLUMN_POSTLIST_ID = "id"
    COLUMN_POSTLIST_URL = "url"
    COLUMN_POSTLIST_WORD = "word"
    COLUMN_POSTLIST_POST_DATE = "post_date"
    COLUMN_POSTLIST_H_TAGS = "h_tags"
    COLUMN_POSTLIST_POST_USER_ID = "post_user_id"
    COLUMN_POSTLIST_CONVERTED_POST_DATE = "converted_post_date"
    COLUMN_POSTLIST_CREATEDATE = "createdate"

    # UserList
    TABLE_UserList = "UserList"
    COLUMN_USERLIST_ID = "id"
    COLUMN_USERLIST_URL = "url"
    COLUMN_USERLIST_USER = "user"
    COLUMN_USERLIST_CREATEDATE = "createdate"

    # DailyArchiveMaster
    TABLE_DailyArchiveMaster = "DailyArchiveMaster"
    COLUMN_DAILYARCHIVE_ID = "id"
    COLUMN_DAILYARCHIVE_FOLLOWER = "follower"
    COLUMN_DAILYARCHIVE_FOLLOW = "follow"
    COLUMN_DAILYARCHIVE_POST = "post"
    COLUMN_DAILYARCHIVE_STATUS = "status"
    COLUMN_DAILYARCHIVE_INSTA_ACCOUNT = "instaAccount"
    COLUMN_DAILYARCHIVE_CREATEDATE = "createdate"

    # Customer
    TABLE_CUSTOMER = "Customer"
    COLUMN_CUSTOMER_ID = "id"
    COLUMN_CUSTOMER_NAME = "customerName"
    COLUMN_CUSTOMER_INSTA_ACCOUNT = "instaAccount"
    COLUMN_CUSTOMER_TW_ACCOUNT = "twAccount"
    COLUMN_CUSTOMER_INSTA_PW = "instaPW"
    COLUMN_CUSTOMER_TW_PW = "twPW"
    COLUMN_CUSTOMER_INSTA_KEYWORD = "keyword"
    COLUMN_CUSTOMER_STATUS = "status" # 0:有効 1:無効
    COLUMN_CUSTOMER_WEB_APPLY_SEQ = "webApplySeq"
    COLUMN_CUSTOMER_WEB_AGENT_NAME = "agentName"
    COLUMN_CUSTOMER_WEB_APPLY_STATUS = "webApplyStatus" # 1:アカウント設定中 2:無料期間中 3:契約中 4:課金NG 100:未処理 101:停止 102:解約
    COLUMN_CUSTOMER_WEB_APPLY_CREATEDATE = "webApplyCreatedate"
    COLUMN_CUSTOMER_WEB_APPLY_UPDATEDATE = "webApplyUpdatedate"
    COLUMN_CUSTOMER_CREATEDATE = "createdate"

    # History
    TABLE_HISTORY = "History"
    COLUMN_HISTORY_ID = "id"
    COLUMN_HISTORY_CONTENTS = "contents"
    COLUMN_HISTORY_CREATEDATE = "createdate"


    def __init__(self):

        self.con = mysql.connector.connect(**config.mysql_db_info)


        # 今は未使用のテーブル
        query1 = "CREATE TABLE IF NOT EXISTS "+ self.TABLE_PostList+"("\
            + self.COLUMN_POSTLIST_ID+" int(11) auto_increment primary key,"\
            + self.COLUMN_POSTLIST_URL+" varchar(255) unique,"\
            + self.COLUMN_POSTLIST_WORD+" text,"\
            + self.COLUMN_POSTLIST_POST_DATE+" varchar(255),"\
            + self.COLUMN_POSTLIST_H_TAGS+" text,"\
            + self.COLUMN_POSTLIST_POST_USER_ID+" varchar(255),"\
            + self.COLUMN_POSTLIST_CONVERTED_POST_DATE+" varchar(255),"\
            + self.COLUMN_POSTLIST_CREATEDATE+" text"\
            + ")"

        # 今は未使用のテーブル
        query2 = "CREATE TABLE IF NOT EXISTS "+ self.TABLE_UserList+"("\
            + self.COLUMN_USERLIST_ID+" int(11) auto_increment primary key ,"\
            + self.COLUMN_USERLIST_URL+" varchar(255) unique,"\
            + self.COLUMN_USERLIST_USER+" varchar(255),"\
            + self.COLUMN_USERLIST_CREATEDATE+" text"\
            + ")"

        query3 = "CREATE TABLE IF NOT EXISTS "+self.TABLE_DailyArchiveMaster+"("\
                +self.COLUMN_DAILYARCHIVE_ID+" int(11) auto_increment primary key ,"\
                +self.COLUMN_DAILYARCHIVE_FOLLOWER+" int(11),"\
                +self.COLUMN_DAILYARCHIVE_FOLLOW+" int(11),"\
                +self.COLUMN_DAILYARCHIVE_POST+" int(11),"\
                +self.COLUMN_DAILYARCHIVE_INSTA_ACCOUNT+" text default null,"\
                +self.COLUMN_DAILYARCHIVE_CREATEDATE+" text"\
                +")"

        query4 = "CREATE TABLE IF NOT EXISTS "+self.TABLE_CUSTOMER+"("\
                +self.COLUMN_CUSTOMER_ID+" int(11) auto_increment primary key ,"\
                +self.COLUMN_CUSTOMER_NAME+" varchar(255) default null comment '顧客名',"\
                +self.COLUMN_CUSTOMER_INSTA_ACCOUNT+" varchar(255) default null,"\
                +self.COLUMN_CUSTOMER_TW_ACCOUNT+" varchar(255) default null,"\
                +self.COLUMN_CUSTOMER_INSTA_PW+" varchar(50) default null,"\
                +self.COLUMN_CUSTOMER_TW_PW+" varchar(50) default null,"\
                +self.COLUMN_CUSTOMER_INSTA_KEYWORD+" text default null,"\
                +self.COLUMN_CUSTOMER_STATUS+" int(11) default 0 comment '状態(0:有効 1:無効)',"\
                +self.COLUMN_CUSTOMER_WEB_APPLY_SEQ+" int(11) default 0 comment '管理画面の顧客SEQ',"\
                +self.COLUMN_CUSTOMER_WEB_AGENT_NAME+" text default null comment '代理店名'," \
                +self.COLUMN_CUSTOMER_WEB_APPLY_STATUS + " int(11) default 0 comment '1:アカウント設定中 2:無料期間中 3:契約中 4:課金NG 100:未処理 101:停止 102:解約'," \
                 + self.COLUMN_CUSTOMER_WEB_APPLY_CREATEDATE + " text default null comment '管理画面での作成日'," \
                 + self.COLUMN_CUSTOMER_WEB_APPLY_UPDATEDATE + " text default null comment '管理画面での更新日'," \
                 +self.COLUMN_DAILYARCHIVE_CREATEDATE+" text"\
                +")"

        query5 = "CREATE TABLE IF NOT EXISTS "+self.TABLE_HISTORY+"("\
                +self.COLUMN_HISTORY_ID+" int(11) auto_increment primary key ,"\
                +self.COLUMN_HISTORY_CONTENTS+" text default null,"\
                +self.COLUMN_DAILYARCHIVE_CREATEDATE+" datetime"\
                +")"

        c = self.con.cursor()

        try:
            c.execute(query1)
            self.con.commit()
        except Exception as e:
            print(e.args)

        try:
            c.execute(query2)
            self.con.commit()
        except Exception as e:
            print(e.args)

        try:
            c.execute(query3)
            self.con.commit()
        except Exception as e:
            print(e.args)

        try:
            c.execute(query4)
            self.con.commit()
        except Exception as e:
            print(e.args)

        try:
            c.execute(query5)
            self.con.commit()
        except Exception as e:
            print(e.args)

    def get_config(self):
        return config.mysql_db_info


#
# # SQLite
# class DbManager:
#
#     dbPath = "Insta.db"
#     con = ""
#
#     # Customer
#     TABLE_Customer = "Customer"
#     COLUMN_CUSTOMER_ID = "id"  # 0
#     COLUMN_CUSTOMER_INSTAACCOUNT = "instaAccount"  # 1
#     COLUMN_CUSTOMER_INSTAPW = "instaPW"  # 2
#     COLUMN_CUSTOMER_ACCOUNTDETAILS = "accountDetails"  # 3
#     COLUMN_CUSTOMER_CATEGORY = "category"  # 4
#     COLUMN_CUSTOMER_KEYWORD = "keyword"  # 5
#     COLUMN_CUSTOMER_SITEURL = "siteUrl"  # 6
#     COLUMN_CUSTOMER_TARGETDETAILS = "targetDetails"  # 7
#     COLUMN_CUSTOMER_CREATEDATE = "createdate"  # 8
#     COLUMN_CUSTOMER_PROXY = "proxy"  # 9
#     COLUMN_CUSTOMER_STATUS = "status"  # 10
#     COLUMN_CUSTOMER_ACTIONCOUNT = "actionCount"  # 11
#     COLUMN_CUSTOMER_FOLLEWERATSTART = "follewerAtStart"  # 12
#     COLUMN_CUSTOMER_FOLLEWATSTART = "follewAtStart"  # 13
#     COLUMN_CUSTOMER_PROTOCOL = "protocol"  # 14
#     COLUMN_CUSTOMER_PORT = "port"  # 15
#     COLUMN_CUSTOMER_PROXYID = "proxyID"  # 16
#     COLUMN_CUSTOMER_PROXYPW = "proxyPW"  # 17
#     COLUMN_CUSTOMER_INSTA_STARTTIME = "instaStartTime"  # 18
#     COLUMN_CUSTOMER_INSTA_ENDTIME = "instaEndTime"  # 19
#     COLUMN_CUSTOMER_WEB_APPLY_UPDATEDATE = "webApplyUpdatedate"  # 20
#     COLUMN_CUSTOMER_WEB_APPLY_SEQ = "webApplySeq"  # 21
#     COLUMN_CUSTOMER_UNFOLLOW_SPAN = "unfollowspan"  # 22
#
#     # PostList
#     TABLE_PostList = "PostList"
#     COLUMN_POSTLIST_ID = "id"
#     COLUMN_POSTLIST_URL = "url"
#     COLUMN_POSTLIST_WORD = "word"
#     COLUMN_POSTLIST_POST_DATE = "post_date"
#     COLUMN_POSTLIST_H_TAGS = "h_tags"
#     COLUMN_POSTLIST_POST_USER_ID = "post_user_id"
#     COLUMN_POSTLIST_CONVERTED_POST_DATE = "converted_post_date"
#     COLUMN_POSTLIST_CREATEDATE = "createdate"
#
#     # UserList
#     TABLE_UserList = "UserList"
#     COLUMN_USERLIST_ID = "id"
#     COLUMN_USERLIST_URL = "url"
#     COLUMN_USERLIST_USER = "user"
#     COLUMN_USERLIST_CREATEDATE = "createdate"
#
#     TABLE_Strategy = "Strategy"
#     COLUMN_STRATEGY_ID = "id"
#     COLUMN_STRATEGY_CUSTOMERID = "customerId"
#     COLUMN_STRATEGY_TITLE = "title"
#     COLUMN_STRATEGY_TYPE = "type"
#     COLUMN_STRATEGY_KEYWORD = "keyword"
#
#     # Schedule
#     TABLE_Schedule = "Schedule"
#     COLUMN_SCHEDULE_ID = "id"
#     COLUMN_SCHEDULE_STATUS = "status"
#     COLUMN_SCHEDULE_AVERAGECOUNT = "averageCount"
#     COLUMN_SCHEDULE_STARTTIME = "startTime"
#     COLUMN_SCHEDULE_ENDTIME = "endTime"
#     COLUMN_SCHEDULE_ACTIONDATE = "actiondate"
#     COLUMN_SCHEDULE_CUSTOMERID = "customerId"
#
#     TABLE_ActionBox = "ActionBox"
#     COLUMN_ACTIONBOX_ID = "id"
#     COLUMN_ACTIONBOX_SCHEDULEID = "scheduleId"
#     COLUMN_ACTIONBOX_URL = "url"
#     COLUMN_ACTIONBOX_TYPE = "type"
#     COLUMN_ACTIONBOX_CUSTOMERID = "customerId"
#     COLUMN_ACTIONBOX_CREATEDATE = "createdate"
#     COLUMN_ACTIONBOX_STATUS = "status"
#     COLUMN_ACTIONBOX_ACTION_TIME = "actionTime"
#     COLUMN_ACTIONBOX_INTERVAL = "interval"
#
#     def __init__(self):
#
#         self.con = sqlite3.connect(self.dbPath)
#
#         query = "CREATE TABLE IF NOT EXISTS "+ self.TABLE_Customer+"("\
#             + self.COLUMN_CUSTOMER_ID+" integer primary key autoincrement ,"\
#             + self.COLUMN_CUSTOMER_INSTAACCOUNT+" text unique,"\
#             + self.COLUMN_CUSTOMER_INSTAPW+" text,"\
#             + self.COLUMN_CUSTOMER_ACCOUNTDETAILS+" text,"\
#             + self.COLUMN_CUSTOMER_CATEGORY+" integer,"\
#             + self.COLUMN_CUSTOMER_KEYWORD+" text,"\
#             + self.COLUMN_CUSTOMER_SITEURL+" text,"\
#             + self.COLUMN_CUSTOMER_TARGETDETAILS+" text,"\
#             + self.COLUMN_CUSTOMER_CREATEDATE+" text,"\
#             + self.COLUMN_CUSTOMER_PROXY+" text unique,"\
#             + self.COLUMN_CUSTOMER_STATUS+" text,"\
#             + self.COLUMN_CUSTOMER_ACTIONCOUNT+" text,"\
#             + self.COLUMN_CUSTOMER_FOLLEWERATSTART+" text,"\
#             + self.COLUMN_CUSTOMER_FOLLEWATSTART+" text," \
#             + self.COLUMN_CUSTOMER_PROTOCOL + " text," \
#             + self.COLUMN_CUSTOMER_PORT + " integer," \
#             + self.COLUMN_CUSTOMER_PROXYID + " text," \
#             + self.COLUMN_CUSTOMER_PROXYPW + " text," \
#             + self.COLUMN_CUSTOMER_INSTA_STARTTIME + " integer," \
#             + self.COLUMN_CUSTOMER_INSTA_ENDTIME + " integer," \
#             + self.COLUMN_CUSTOMER_WEB_APPLY_UPDATEDATE + " text," \
#             + self.COLUMN_CUSTOMER_WEB_APPLY_SEQ + " integer," \
#             + self.COLUMN_CUSTOMER_UNFOLLOW_SPAN + " integer" \
#             + ")"
#
#         query1 = "CREATE TABLE IF NOT EXISTS "+ self.TABLE_PostList+"("\
#             + self.COLUMN_POSTLIST_ID+" integer primary key autoincrement ,"\
#             + self.COLUMN_POSTLIST_URL+" text unique,"\
#             + self.COLUMN_POSTLIST_WORD+" text,"\
#             + self.COLUMN_POSTLIST_POST_DATE+" text,"\
#             + self.COLUMN_POSTLIST_H_TAGS+" text,"\
#             + self.COLUMN_POSTLIST_POST_USER_ID+" text default null,"\
#             + self.COLUMN_POSTLIST_CONVERTED_POST_DATE+" text,"\
#             + self.COLUMN_POSTLIST_CREATEDATE+" text"\
#             + ")"
#
#         query2 = "CREATE TABLE IF NOT EXISTS "+ self.TABLE_UserList+"("\
#             + self.COLUMN_USERLIST_ID+" integer primary key autoincrement ,"\
#             + self.COLUMN_USERLIST_URL+" text unique,"\
#             + self.COLUMN_USERLIST_USER+" text,"\
#             + self.COLUMN_USERLIST_CREATEDATE+" text"\
#             + ")"
#
#         query3 = "CREATE TABLE IF NOT EXISTS "+self.TABLE_Schedule+"("\
#             +self.COLUMN_SCHEDULE_ID+" integer primary key autoincrement ,"\
#             +self.COLUMN_SCHEDULE_STATUS+" integer,"\
#             +self.COLUMN_SCHEDULE_AVERAGECOUNT+" integer,"\
#             +self.COLUMN_SCHEDULE_STARTTIME+" text,"\
#             +self.COLUMN_SCHEDULE_ENDTIME+" text,"\
#             +self.COLUMN_SCHEDULE_ACTIONDATE+" text,"\
#             +self.COLUMN_SCHEDULE_CUSTOMERID+" integer"\
#             + ")"
#
#         query4 = "CREATE TABLE IF NOT EXISTS "+self.TABLE_ActionBox+"("\
#             + self.COLUMN_ACTIONBOX_ID+" integer primary key autoincrement ,"\
#             + self.COLUMN_ACTIONBOX_SCHEDULEID+" integer,"\
#             + self.COLUMN_ACTIONBOX_URL+" text,"\
#             + self.COLUMN_ACTIONBOX_TYPE+" integer,"\
#             + self.COLUMN_ACTIONBOX_CUSTOMERID+" integer,"\
#             + self.COLUMN_ACTIONBOX_CREATEDATE+" text,"\
#             + self.COLUMN_ACTIONBOX_STATUS+" integer default 0,"\
#             + self.COLUMN_ACTIONBOX_ACTION_TIME+" text,"\
#             + self.COLUMN_ACTIONBOX_INTERVAL+" integer"\
#             + ")"
#
#         query5 = "CREATE TABLE IF NOT EXISTS " + self.TABLE_Strategy + "(" \
#              + self.COLUMN_STRATEGY_ID + " integer primary key autoincrement ," \
#              + self.COLUMN_STRATEGY_CUSTOMERID + " integer," \
#              + self.COLUMN_STRATEGY_TITLE + " text," \
#              + self.COLUMN_STRATEGY_TYPE + " integer," \
#              + self.COLUMN_STRATEGY_KEYWORD + " text" \
#              + ")"
#
#         c = self.con.cursor()
#
#         try:
#             c.execute(query)
#             self.con.commit()
#         except Exception as e:
#             print(e)
#
#         try:
#             c.execute(query2)
#             self.con.commit()
#         except Exception as e:
#             print(e)
#
#         try:
#             c.execute(query3)
#             self.con.commit()
#         except Exception as e:
#             print(e)
#
#
#         try:
#             c.execute(query4)
#             self.con.commit()
#         except Exception as e:
#             print(e)
#
#
#         try:
#             c.execute(query5)
#             self.con.commit()
#         except Exception as e:
#             print(e)
#
#         try:
#             c.execute(query1)
#             self.con.commit()
#             c.close()
#         except Exception as e:
#             print(e)
#
# # Local Mysql
# class DbManager2:
#
#     # https://blowup-bbs.com/mysql-connector-python-developer-guide/
#     con = ""
#
#     # Customer
#     TABLE_Customer = "Customer"
#     COLUMN_CUSTOMER_ID = "id"  # 0
#     COLUMN_CUSTOMER_INSTAACCOUNT = "instaAccount"  # 1
#     COLUMN_CUSTOMER_INSTAPW = "instaPW"  # 2
#     COLUMN_CUSTOMER_ACCOUNTDETAILS = "accountDetails"  # 3
#     COLUMN_CUSTOMER_CATEGORY = "category"  # 4
#     COLUMN_CUSTOMER_KEYWORD = "keyword"  # 5
#     COLUMN_CUSTOMER_SITEURL = "siteUrl"  # 6
#     COLUMN_CUSTOMER_TARGETDETAILS = "targetDetails"  # 7
#     COLUMN_CUSTOMER_CREATEDATE = "createdate"  # 8
#     COLUMN_CUSTOMER_PROXY = "proxy"  # 9
#     COLUMN_CUSTOMER_STATUS = "status"  # 10
#     COLUMN_CUSTOMER_ACTIONCOUNT = "actionCount"  # 11
#     COLUMN_CUSTOMER_FOLLEWERATSTART = "follewerAtStart"  # 12
#     COLUMN_CUSTOMER_FOLLEWATSTART = "follewAtStart"  # 13
#     COLUMN_CUSTOMER_PROTOCOL = "protocol"  # 14
#     COLUMN_CUSTOMER_PORT = "port"  # 15
#     COLUMN_CUSTOMER_PROXYID = "proxyID"  # 16
#     COLUMN_CUSTOMER_PROXYPW = "proxyPW"  # 17
#     COLUMN_CUSTOMER_INSTA_STARTTIME = "instaStartTime"  # 18
#     COLUMN_CUSTOMER_INSTA_ENDTIME = "instaEndTime"  # 19
#     COLUMN_CUSTOMER_WEB_APPLY_UPDATEDATE = "webApplyUpdatedate"  # 20
#     COLUMN_CUSTOMER_WEB_APPLY_SEQ = "webApplySeq"  # 21
#     COLUMN_CUSTOMER_UNFOLLOW_SPAN = "unfollowspan"  # 22
#     COLUMN_CUSTOMER_PROFILE_STATUS = "profileStatus"  # 23
#     COLUMN_CUSTOMER_BIKO = "biko"  # 24
#     COLUMN_CUSTOMER_MAILADDRESS = "mailaddress"  # 25
#     COLUMN_CUSTOMER_TWITTER_ACCOUNT_NAME = "twitterAccountName"  # 26
#     COLUMN_CUSTOMER_TWITTER_LOGIN_ID = "twitterLoginId"  # 27
#     COLUMN_CUSTOMER_TWITTER_LOGIN_PW = "twitterLoginPw"  # 28
#     COLUMN_CUSTOMER_USERAGENT = "userAgent"  # 29
#     COLUMN_CUSTOMER_INSTIME_SYSTEM_SWITCH = "instimeSwitch"  # 30
#     COLUMN_CUSTOMER_AGENT_NAME = "agentName"  # 31
#     COLUMN_CUSTOMER_INSTIME_STATUS = "instimeStatus"  # 32
#
#     # PostList
#     TABLE_PostList = "PostList"
#     COLUMN_POSTLIST_ID = "id"
#     COLUMN_POSTLIST_URL = "url"
#     COLUMN_POSTLIST_WORD = "word"
#     COLUMN_POSTLIST_POST_DATE = "post_date"
#     COLUMN_POSTLIST_H_TAGS = "h_tags"
#     COLUMN_POSTLIST_POST_USER_ID = "post_user_id"
#     COLUMN_POSTLIST_CONVERTED_POST_DATE = "converted_post_date"
#     COLUMN_POSTLIST_CREATEDATE = "createdate"
#     COLUMN_POSTLIST_APOLISTFLAG = "apolistFlag"
#     COLUMN_POSTLIST_PROFILE_URL = "profile_url"
#     COLUMN_POSTLIST_FOLLOWERS = "followers"
#     COLUMN_POSTLIST_FOLLOWINGS = "followings"
#     COLUMN_POSTLIST_USERNAME = "userName"
#     COLUMN_POSTLIST_INTRODUCTION = "intoroduction"
#     COLUMN_POSTLIST_SHOPURL = "shopUrl"
#
#     # UserList
#     TABLE_UserList = "UserList"
#     COLUMN_USERLIST_ID = "id"
#     COLUMN_USERLIST_URL = "url"
#     COLUMN_USERLIST_USER = "user"
#     COLUMN_USERLIST_CREATEDATE = "createdate"
#
#     TABLE_Strategy = "Strategy"
#     COLUMN_STRATEGY_ID = "id"
#     COLUMN_STRATEGY_CUSTOMERID = "customerId"
#     COLUMN_STRATEGY_TITLE = "title"
#     COLUMN_STRATEGY_TYPE = "type"
#     COLUMN_STRATEGY_KEYWORD = "keyword"
#
#     # Schedule
#     TABLE_Schedule = "Schedule"
#     COLUMN_SCHEDULE_ID = "id"
#     COLUMN_SCHEDULE_STATUS = "status"
#     COLUMN_SCHEDULE_AVERAGECOUNT = "averageCount"
#     COLUMN_SCHEDULE_STARTTIME = "startTime"
#     COLUMN_SCHEDULE_ENDTIME = "endTime"
#     COLUMN_SCHEDULE_ACTIONDATE = "actiondate"
#     COLUMN_SCHEDULE_CUSTOMERID = "customerId"
#     COLUMN_SCHEDULE_FILE_TITLE = "fileTitle"
#
#     TABLE_ActionBox = "ActionBox"
#     COLUMN_ACTIONBOX_ID = "id"
#     COLUMN_ACTIONBOX_SCHEDULEID = "scheduleId"
#     COLUMN_ACTIONBOX_URL = "url"
#     COLUMN_ACTIONBOX_TYPE = "type"#1post 2user 3twitter_user
#     COLUMN_ACTIONBOX_CUSTOMERID = "customerId"
#     COLUMN_ACTIONBOX_CREATEDATE = "createdate"
#     COLUMN_ACTIONBOX_STATUS = "status"
#     COLUMN_ACTIONBOX_ACTION_TIME = "actionTime"
#     COLUMN_ACTIONBOX_INTERVAL = "actionInterval"
#     COLUMN_ACTIONBOX_ACTION_METHOD = "actionMethod" # 1いいね 2フォロー 3いいね＆フォロー
#     COLUMN_ACTIONBOX_ACTION_USER_ACCOUNT = "userAccount"
#     COLUMN_ACTIONBOX_ACTION_LOG = "actionLog"
#     COLUMN_ACTIONBOX_UNFOLLOW_DATE = "unfollowdate"
#
#     # task
#     TABLE_Task = "Task"
#     COLUMN_TASK_ID = "id"
#     COLUMN_TASK_TASK = "task"
#     COLUMN_TASK_STATUS = "status"
#     COLUMN_TASK_CREATEDATE = "createdate"
#
#     # archive
#     TABLE_DailyArchive = "DailyArchive"
#     COLUMN_DAILYARCHIVE_ID = "id"
#     COLUMN_DAILYARCHIVE_FOLLOWER = "follower"
#     COLUMN_DAILYARCHIVE_FOLLOW = "follow"
#     COLUMN_DAILYARCHIVE_POST = "post"
#     COLUMN_DAILYARCHIVE_CUSTOMER_ID = "customerId"
#     COLUMN_DAILYARCHIVE_CREATEDATE = "createdate"
#
#     # follower log
#     TABLE_FollowerLog = "FollowerLog"
#     COLUMN_FOLLOWERLOG_ID = "id"
#     COLUMN_FOLLOWERLOG_FOLLOWERS = "followers"
#     COLUMN_FOLLOWERLOG_USERID = "userId"
#     COLUMN_FOLLOWERLOG_FOLLOWERCOUNT = "followerCount"
#     COLUMN_FOLLOWERLOG_TARGET_ACCOUNT = "targetAccount"
#     COLUMN_FOLLOWERLOG_CREATEDATE = "createdate"
#
#     # following log
#     TABLE_FOLLOWINGLOG = "FollowingLog"
#     COLUMN_FOLLOWINGLOG_ID = "id"
#     COLUMN_FOLLOWINGLOG_FOLLOWERS = "followings"
#     COLUMN_FOLLOWINGLOG_USERID = "userId"
#     COLUMN_FOLLOWINGLOG_FOLLOWERCOUNT = "followingCount"
#     COLUMN_FOLLOWINGLOG_TARGET_ACCOUNT = "targetAccount"
#     COLUMN_FOLLOWINGLOG_CREATEDATE = "createdate"
#
#     # ticket
#     TABLE_Ticket = "Ticket"
#     COLUMN_TICKET_ID = "id"
#     COLUMN_TICKET_TICKETCOUNT = "ticketCount"
#     COLUMN_TICKET_NAME = "name"
#     COLUMN_TICKET_USER_ID = "userId"
#     COLUMN_TICKET_CREATEDATE = "createdate"
#
#     # Pid
#     TABLE_Pid = "Pid"
#     COLUMN_PID_ID = "id"
#     COLUMN_PID_PID = "pid"
#     COLUMN_PID_CUSTOMER_ID = "customerId"
#     COLUMN_PID_TITLE = "title"
#     COLUMN_PID_CREATEDATE = "createdate"
#
#
#     # TWITTER --- こいつに対してアクションを行う
#     TABLE_TWITTER_USER_LIST = "TwitterUserList"
#     COLUMN_TWITTER_USER_LIST_ID = "id"
#     COLUMN_TWITTER_USER_LIST_USER_ID = "user_id"
#     COLUMN_TWITTER_USER_LIST_SEARCHWORD = "search_word"
#     COLUMN_TWITTER_USER_LIST_CREATEDATE = "createdate"
#
#     TABLE_TWITTER_FOLLOWER_LIST = "TwitterFollowerList"
#     COLUMN_TWITTER_FOLLOWER_LIST_ID = "id"
#     COLUMN_TWITTER_FOLLOWER_LIST_USER_ID = "follower_user_id"
#     COLUMN_TWITTER_FOLLOWER_LIST_TYPE = "follower_type"
#     COLUMN_TWITTER_FOLLOWER_LIST_PARENT_USER_ID = "parent_user_id"
#     COLUMN_TWITTER_FOLLOWER_LIST_CREATEDATE = "createdate"
#
#     TABLE_HISTORY_LOG = "HistoryLog"
#     COLUMN_HISTORY_LOG_ID = "id"
#     COLUMN_HISTORY_LOG_CONTENTS = "contents"
#     COLUMN_HISTORY_LOG_CUSTOMER_ID = "customerId"
#     COLUMN_HISTORY_LOG_ORDER = "orderNumber"
#     COLUMN_HISTORY_LOG_CREATEDATE = "createdate"
#
#     TABLE_TW_HISTORY_LOG = "TwHistoryLog"
#     COLUMN_TW_HISTORY_LOG_ID = "id"
#     COLUMN_TW_HISTORY_LOG_CONTENTS = "contents"
#     COLUMN_TW_HISTORY_LOG_CUSTOMER_ID = "customerId"
#     COLUMN_TW_HISTORY_LOG_ORDER = "orderNumber"
#     COLUMN_TW_HISTORY_LOG_CREATEDATE = "createdate"
#
#
#     # archive
#     TABLE_TW_DailyArchive = "TwDailyArchive"
#     COLUMN_TW_DAILYARCHIVE_ID = "id"
#     COLUMN_TW_DAILYARCHIVE_FOLLOWER = "follower"
#     COLUMN_TW_DAILYARCHIVE_FOLLOW = "follow"
#     COLUMN_TW_DAILYARCHIVE_POST = "tweet"
#     COLUMN_TW_DAILYARCHIVE_CUSTOMER_ID = "customerId"
#     COLUMN_TW_DAILYARCHIVE_CREATEDATE = "createdate"
#
#     def __init__(self):
#
#         # self.con = sqlite3.connect(self.dbPath)
#         self.con = mysql.connector.connect(**config.mysql_db_info_local)
#
#         query = "CREATE TABLE IF NOT EXISTS "+ self.TABLE_Customer+"("\
#             + self.COLUMN_CUSTOMER_ID+" int(11) auto_increment primary key  ,"\
#             + self.COLUMN_CUSTOMER_INSTAACCOUNT+" varchar(255) ,"\
#             + self.COLUMN_CUSTOMER_INSTAPW+" varchar(255),"\
#             + self.COLUMN_CUSTOMER_ACCOUNTDETAILS+" text,"\
#             + self.COLUMN_CUSTOMER_CATEGORY+" int(11),"\
#             + self.COLUMN_CUSTOMER_KEYWORD+" text,"\
#             + self.COLUMN_CUSTOMER_SITEURL+" text,"\
#             + self.COLUMN_CUSTOMER_TARGETDETAILS+" text,"\
#             + self.COLUMN_CUSTOMER_CREATEDATE+" text,"\
#             + self.COLUMN_CUSTOMER_PROXY+" varchar(255) ,"\
#             + self.COLUMN_CUSTOMER_STATUS+" int(11) default 0 COMMENT '0: 正常,1: 無効',"\
#             + self.COLUMN_CUSTOMER_ACTIONCOUNT+" text,"\
#             + self.COLUMN_CUSTOMER_FOLLEWERATSTART+" text,"\
#             + self.COLUMN_CUSTOMER_FOLLEWATSTART+" text," \
#             + self.COLUMN_CUSTOMER_PROTOCOL + " text," \
#             + self.COLUMN_CUSTOMER_PORT + " int(11)," \
#             + self.COLUMN_CUSTOMER_PROXYID + " varchar(255)," \
#             + self.COLUMN_CUSTOMER_PROXYPW + " varchar(255)," \
#             + self.COLUMN_CUSTOMER_INSTA_STARTTIME + " int(11)," \
#             + self.COLUMN_CUSTOMER_INSTA_ENDTIME + " int(11)," \
#             + self.COLUMN_CUSTOMER_WEB_APPLY_UPDATEDATE + " text," \
#             + self.COLUMN_CUSTOMER_WEB_APPLY_SEQ + " int(11)," \
#             + self.COLUMN_CUSTOMER_UNFOLLOW_SPAN + " int(11)," \
#             + self.COLUMN_CUSTOMER_PROFILE_STATUS + " int(11)," \
#             + self.COLUMN_CUSTOMER_BIKO + " text," \
#             + self.COLUMN_CUSTOMER_MAILADDRESS + " varchar(255)," \
#             + self.COLUMN_CUSTOMER_TWITTER_ACCOUNT_NAME + " varchar(255) default null," \
#             + self.COLUMN_CUSTOMER_TWITTER_LOGIN_ID + " varchar(255) default null," \
#             + self.COLUMN_CUSTOMER_TWITTER_LOGIN_PW + " varchar(255) default null," \
#             + self.COLUMN_CUSTOMER_USERAGENT + " text default null," \
#             + self.COLUMN_CUSTOMER_INSTIME_SYSTEM_SWITCH + " int(11) default 0," \
#             + self.COLUMN_CUSTOMER_AGENT_NAME + " varchar(255) default null," \
#             + self.COLUMN_CUSTOMER_INSTIME_STATUS + " int(11) default 0 COMMENT '1:アカウント設定中 2:無料期間中 3:契約中 4:課金NG 100:未処理 101:停止 102:解約'" \
#             + ")"
#
#         query1 = "CREATE TABLE IF NOT EXISTS "+ self.TABLE_PostList+"("\
#             + self.COLUMN_POSTLIST_ID+" int(11) auto_increment primary key ,"\
#             + self.COLUMN_POSTLIST_URL+" varchar(255) unique,"\
#             + self.COLUMN_POSTLIST_WORD+" varchar(255),"\
#             + self.COLUMN_POSTLIST_POST_DATE+" varchar(255),"\
#             + self.COLUMN_POSTLIST_H_TAGS+" text,"\
#             + self.COLUMN_POSTLIST_POST_USER_ID+" varchar(255),"\
#             + self.COLUMN_POSTLIST_CONVERTED_POST_DATE+" varchar(255),"\
#             + self.COLUMN_POSTLIST_CREATEDATE+" text,"\
#             + self.COLUMN_POSTLIST_APOLISTFLAG+" int(11),"\
#             + self.COLUMN_POSTLIST_PROFILE_URL+" text,"\
#             + self.COLUMN_POSTLIST_FOLLOWERS+" int(11),"\
#             + self.COLUMN_POSTLIST_FOLLOWINGS+" int(11),"\
#             + self.COLUMN_POSTLIST_USERNAME+" text,"\
#             + self.COLUMN_POSTLIST_INTRODUCTION+" text,"\
#             + self.COLUMN_POSTLIST_SHOPURL+" text"\
#             + ")"
#
#
#         query2 = "CREATE TABLE IF NOT EXISTS "+ self.TABLE_UserList+"("\
#             + self.COLUMN_USERLIST_ID+" int(11) auto_increment primary key ,"\
#             + self.COLUMN_USERLIST_URL+" varchar(255) unique,"\
#             + self.COLUMN_USERLIST_USER+" varchar(255),"\
#             + self.COLUMN_USERLIST_CREATEDATE+" text"\
#             + ")"
#
#         query3 = "CREATE TABLE IF NOT EXISTS "+self.TABLE_Schedule+"("\
#             +self.COLUMN_SCHEDULE_ID+" int(11) auto_increment primary key ,"\
#             +self.COLUMN_SCHEDULE_STATUS+" int(11),"\
#             +self.COLUMN_SCHEDULE_AVERAGECOUNT+" int(11),"\
#             +self.COLUMN_SCHEDULE_STARTTIME+" text,"\
#             +self.COLUMN_SCHEDULE_ENDTIME+" text,"\
#             +self.COLUMN_SCHEDULE_ACTIONDATE+" text,"\
#             +self.COLUMN_SCHEDULE_CUSTOMERID+" varchar(255),"\
#             +self.COLUMN_SCHEDULE_FILE_TITLE+" text"\
#             + ")"
#
#         query4 = "CREATE TABLE IF NOT EXISTS "+self.TABLE_ActionBox+"("\
#             + self.COLUMN_ACTIONBOX_ID+" int(11) auto_increment primary key,"\
#             + self.COLUMN_ACTIONBOX_SCHEDULEID+" int(11),"\
#             + self.COLUMN_ACTIONBOX_URL+" text,"\
#             + self.COLUMN_ACTIONBOX_TYPE+" int(11) COMMENT '1: 投稿URL, 2: ユーザーURL',"\
#             + self.COLUMN_ACTIONBOX_CUSTOMERID+" int(11),"\
#             + self.COLUMN_ACTIONBOX_CREATEDATE+" text,"\
#             + self.COLUMN_ACTIONBOX_STATUS+" int(11) default 0 COMMENT '0: 未対応,1: フォローOK,2: スキップ終了,3: 失敗,9: URL無効',"\
#             + self.COLUMN_ACTIONBOX_ACTION_TIME+" text,"\
#             + self.COLUMN_ACTIONBOX_INTERVAL+" int(11), "\
#             + self.COLUMN_ACTIONBOX_ACTION_METHOD+" int(11) COMMENT '0: いいね＆フォロー(基本ない) 1: いいねのみ 2: フォローのみ 3: アンフォロー', "\
#             + self.COLUMN_ACTIONBOX_ACTION_USER_ACCOUNT+" varchar(255) default null, "\
#             + self.COLUMN_ACTIONBOX_ACTION_LOG+" text default null, "\
#             + self.COLUMN_ACTIONBOX_UNFOLLOW_DATE+" text default null "\
#             + ")"
#
#         query5 = "CREATE TABLE IF NOT EXISTS " + self.TABLE_Strategy + "(" \
#              + self.COLUMN_STRATEGY_ID + " int(11) auto_increment primary key ," \
#              + self.COLUMN_STRATEGY_CUSTOMERID + " int(11)," \
#              + self.COLUMN_STRATEGY_TITLE + " varchar(255)," \
#              + self.COLUMN_STRATEGY_TYPE + " int(11)," \
#              + self.COLUMN_STRATEGY_KEYWORD + " text" \
#              + ")"
#
#         query6 = "CREATE TABLE IF NOT EXISTS "+self.TABLE_Task+"("\
#                 +self.COLUMN_TASK_ID+" int(11) auto_increment primary key ,"\
#                 +self.COLUMN_TASK_TASK+" text,"\
#                 +self.COLUMN_TASK_STATUS+" int(11),"\
#                 +self.COLUMN_TASK_CREATEDATE+" text"\
#                 +")"
#
#         query7 = "CREATE TABLE IF NOT EXISTS "+self.TABLE_DailyArchive+"("\
#                 +self.COLUMN_DAILYARCHIVE_ID+" int(11) auto_increment primary key ,"\
#                 +self.COLUMN_DAILYARCHIVE_FOLLOWER+" int(11),"\
#                 +self.COLUMN_DAILYARCHIVE_FOLLOW+" int(11),"\
#                 +self.COLUMN_DAILYARCHIVE_POST+" int(11),"\
#                 +self.COLUMN_DAILYARCHIVE_CUSTOMER_ID+" int(11),"\
#                 +self.COLUMN_DAILYARCHIVE_CREATEDATE+" text"\
#                 +")"
#
#         query8 = "CREATE TABLE IF NOT EXISTS "+self.TABLE_FollowerLog+"("\
#                 +self.COLUMN_FOLLOWERLOG_ID+" int(11) auto_increment primary key ,"\
#                 +self.COLUMN_FOLLOWERLOG_FOLLOWERS+" text,"\
#                 +self.COLUMN_FOLLOWERLOG_USERID+" int(11),"\
#                 +self.COLUMN_FOLLOWERLOG_FOLLOWERCOUNT+" int(11),"\
#                 +self.COLUMN_FOLLOWERLOG_TARGET_ACCOUNT+" varchar(255),"\
#                 +self.COLUMN_FOLLOWERLOG_CREATEDATE+" text"\
#                 +")"
#
#         query9 = "CREATE TABLE IF NOT EXISTS "+self.TABLE_Ticket+"("\
#                 +self.COLUMN_TICKET_ID+" int(11) auto_increment primary key  ,"\
#                 +self.COLUMN_TICKET_TICKETCOUNT+" int(11),"\
#                 +self.COLUMN_TICKET_NAME+" varchar(30),"\
#                 +self.COLUMN_TICKET_USER_ID+" int(11),"\
#                 +self.COLUMN_TICKET_CREATEDATE+" text"\
#                 +")"
#
#         query10 = "CREATE TABLE IF NOT EXISTS " + self.TABLE_Pid + "(" \
#                 + self.COLUMN_PID_ID + " int(11) auto_increment primary key ," \
#                 + self.COLUMN_PID_PID + " varchar(255) unique," \
#                 + self.COLUMN_PID_CUSTOMER_ID + " int(11)," \
#                 + self.COLUMN_PID_TITLE + " varchar(255)," \
#                 + self.COLUMN_PID_CREATEDATE + " text" \
#                 + ")"
#
#         query11 = "CREATE TABLE IF NOT EXISTS "+self.TABLE_FOLLOWINGLOG+"("\
#                 +self.COLUMN_FOLLOWINGLOG_ID+" int(11) auto_increment primary key ,"\
#                 +self.COLUMN_FOLLOWINGLOG_FOLLOWERS+" text,"\
#                 +self.COLUMN_FOLLOWINGLOG_USERID+" int(11),"\
#                 +self.COLUMN_FOLLOWINGLOG_FOLLOWERCOUNT+" int(11),"\
#                 +self.COLUMN_FOLLOWINGLOG_TARGET_ACCOUNT+" varchar(255),"\
#                 +self.COLUMN_FOLLOWINGLOG_CREATEDATE+" text"\
#                 +")"
#
#
#         query12= "CREATE TABLE IF NOT EXISTS "+self.TABLE_TWITTER_USER_LIST+"("\
#                 +self.COLUMN_TWITTER_USER_LIST_ID+" int(11) auto_increment primary key ,"\
#                 +self.COLUMN_TWITTER_USER_LIST_USER_ID+" varchar(255),"\
#                 +self.COLUMN_TWITTER_USER_LIST_SEARCHWORD+" text,"\
#                 +self.COLUMN_TWITTER_USER_LIST_CREATEDATE+" text"\
#                 +")"
#
#         query13= "CREATE TABLE IF NOT EXISTS "+self.TABLE_TWITTER_FOLLOWER_LIST+"("\
#                 +self.COLUMN_TWITTER_FOLLOWER_LIST_ID+" int(11) auto_increment primary key ,"\
#                 +self.COLUMN_TWITTER_FOLLOWER_LIST_USER_ID+" varchar(255),"\
#                 +self.COLUMN_TWITTER_FOLLOWER_LIST_TYPE+" varchar(10),"\
#                 +self.COLUMN_TWITTER_FOLLOWER_LIST_PARENT_USER_ID+" varchar(255),"\
#                 +self.COLUMN_TWITTER_FOLLOWER_LIST_CREATEDATE+" text"\
#                 +")"
#
#         query14= "CREATE TABLE IF NOT EXISTS "+self.TABLE_HISTORY_LOG+"("\
#                 +self.COLUMN_HISTORY_LOG_ID+" int(11) auto_increment primary key ,"\
#                 +self.COLUMN_HISTORY_LOG_CONTENTS+" text default null,"\
#                 +self.COLUMN_HISTORY_LOG_CUSTOMER_ID+" int(11),"\
#                 +self.COLUMN_HISTORY_LOG_ORDER+" int(11),"\
#                 +self.COLUMN_HISTORY_LOG_CREATEDATE+" text"\
#                 +")"
#
#         query15= "CREATE TABLE IF NOT EXISTS "+self.TABLE_TW_HISTORY_LOG+"("\
#                 +self.COLUMN_TW_HISTORY_LOG_ID+" int(11) auto_increment primary key ,"\
#                 +self.COLUMN_TW_HISTORY_LOG_CONTENTS+" text default null,"\
#                 +self.COLUMN_TW_HISTORY_LOG_CUSTOMER_ID+" int(11),"\
#                 +self.COLUMN_TW_HISTORY_LOG_ORDER+" int(11),"\
#                 +self.COLUMN_TW_HISTORY_LOG_CREATEDATE+" text"\
#                 +")"
#
#
#         query16 = "CREATE TABLE IF NOT EXISTS "+self.TABLE_TW_DailyArchive+"("\
#                 +self.COLUMN_TW_DAILYARCHIVE_ID+" int(11) auto_increment primary key ,"\
#                 +self.COLUMN_TW_DAILYARCHIVE_FOLLOWER+" int(11),"\
#                 +self.COLUMN_TW_DAILYARCHIVE_FOLLOW+" int(11),"\
#                 +self.COLUMN_TW_DAILYARCHIVE_POST+" int(11),"\
#                 +self.COLUMN_TW_DAILYARCHIVE_CUSTOMER_ID+" int(11),"\
#                 +self.COLUMN_TW_DAILYARCHIVE_CREATEDATE+" text"\
#                 +")"
#
#
#         c = self.con.cursor()
#
#         try:
#             c.execute(query)
#             self.con.commit()
#         except Exception as e:
#             print(e)
#
#         try:
#             c.execute(query2)
#             self.con.commit()
#         except Exception as e:
#             print(e)
#
#         try:
#             c.execute(query3)
#             self.con.commit()
#         except Exception as e:
#             print(e)
#
#
#         try:
#             c.execute(query4)
#             self.con.commit()
#         except Exception as e:
#             print(query4)
#             print(e)
#
#
#         try:
#             c.execute(query5)
#             self.con.commit()
#         except Exception as e:
#             print(e)
#
#         try:
#             c.execute(query6)
#             self.con.commit()
#         except Exception as e:
#             print(e)
#
#         try:
#             c.execute(query7)
#             self.con.commit()
#         except Exception as e:
#             print(e)
#
#         try:
#             c.execute(query8)
#             self.con.commit()
#         except Exception as e:
#             print(e)
#
#         try:
#             c.execute(query9)
#             self.con.commit()
#         except Exception as e:
#             print(e)
#
#         try:
#             c.execute(query10)
#             self.con.commit()
#         except Exception as e:
#             print(e)
#
#         try:
#             c.execute(query11)
#             self.con.commit()
#         except Exception as e:
#             print(e)
#
#         try:
#             c.execute(query12)
#             self.con.commit()
#         except Exception as e:
#             print(e)
#
#         try:
#             c.execute(query13)
#             self.con.commit()
#         except Exception as e:
#             print(e)
#
#         try:
#             c.execute(query14)
#             self.con.commit()
#         except Exception as e:
#             print(e)
#
#         try:
#             c.execute(query15)
#             self.con.commit()
#         except Exception as e:
#             print(e)
#
#         try:
#             c.execute(query16)
#             self.con.commit()
#         except Exception as e:
#             print(e)
#
#         try:
#             c.execute(query1)
#             self.con.commit()
#             c.close()
#         except Exception as e:
#             print(e)
#
#     def get_config(self):
#         return config.mysql_db_info_local

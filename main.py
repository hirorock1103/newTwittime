from lib.Command import Basic
from lib.Instime import Instime

args_name = [

    "----フォロー数の調査----",

    "----連携----",
    "3:あいまい検索",
    "5:管理画面と連携(管理画面から最新GET)",
    "----その他----",
    "2:顧客表示",
    "4:chromeテスト",
    "6:apiテスト",
    "99:終了"
]

def main(val):

    print("[実行]main")
    # archive ---- 全顧客のlogを取得する

    basic = Basic()

    # 引数
    if val is None:
        print("実行時に引数がないため、処理ストップ")
        exit()

    if val == "99":
        print("stop bye")
        exit()

    if val == "2":
        basic.customer()

    if val == "4":
        print("input account")
        account = input()
        customers = account.split(",")
        new_list = aimai_search(customers)
        for l in new_list:
            print(l.__dict__)

        instime = Instime()
        instime.browser_action(new_list)

    if val == "3":
        print("input account")
        account = input()
        customers = account.split(",")
        new_list = aimai_search(customers)
        for l in new_list:
            print(l.__dict__)

    if val == "5":
        basic.renkei()

    if val == "6":
        print("input account")
        account = input()
        customers = account.split(",")
        new_list = aimai_search(customers)
        for l in new_list:
            print(l.__dict__)
        instime = Instime()
        instime.api_get_account_info(new_list)

# 曖昧検索
def aimai_search(customers):
    instime = Instime()
    new_list = []
    for c in customers:
        print("searching " + c + " ...")
        conditions = []
        conditions.append(instime.COLUMN_CUSTOMER_INSTA_ACCOUNT + " LIKE '%" + c + "%'")
        args = []
        try:
            list = instime.get_customer(conditions, args)
            if list.__len__() > 0:
                target = list[0]
                print("found:" + target.instaAccount)
                new_list.append(target)
            else:
                print("not found...")
        except Exception as e:
            print(e.args)

    return new_list


if __name__ == "__main__":
    # args = sys.argv
    num = 1
    while num < 99:

        print("\n==============================================\n")
        print('処理コードを入力してください！')
        for title in args_name:
            print("#" + title)
        args = input()
        main(args)
        num += 1





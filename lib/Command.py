from lib.Instime import Instime
from lib.Master import Proxy
from datetime import datetime as dt
import datetime
import time
import config

class Basic:

    # 処理
    def customer(self):
        instime = Instime()
        list = instime.get_customer()

        web_apply_status = config.web_apply_status

        for status in web_apply_status:
            print("===="+web_apply_status[status]+"====")
            for customer in list:
                if customer.webApplyStatus == status:
                    print("# " + customer.instaAccount)
                    print("-name-" + str(customer.name))
                    print("-twAccount-" + str(customer.twAccount))
                    # print("-applyStatus-" + config.web_apply_status[customer.webApplyStatus])
                    print("-agentName-" + str(customer.agentName))
                    # print("-status-" + str(customer.status))
                    time.sleep(0.5)
            print("\n")

    # 連携
    def renkei(self):
        instime = Instime()
        instime.getCustomerFromWeb()


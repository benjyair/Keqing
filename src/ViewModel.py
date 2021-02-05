from Dao import MysqlDao as Dao
from DataBaseEntry import Rank
from DataBaseEntry import Favourite
import Network


def get_numeric(dic, key, def_val=0):
    val = dic.get(key, def_val)
    if len(val) == 0:
        return def_val
    else:
        return val


class ViewModel:
    fund_url = 'https://api.doctorxiong.club/v1/fund'
    page_size = 10

    def __init__(self):
        self.__dao = Dao()
        self.__dao.init_table()

    def sync_rank(self):
        favourites = self.__dao.get_favourite()
        if favourites is None:
            return

        for i in range(0, len(favourites), self.page_size):
            self.load_rank(favourites[i:i + self.page_size])

    def load_rank(self, codes):
        params = ''
        for index, f in enumerate(codes):
            params += f.code
            if index != len(codes) - 1:
                params += ','

        print('params = ' + params)
        data = Network.get_req(self.fund_url, {'code': params})

        if data is None:
            return

        ranks = set()
        for fund in data:
            print(fund)

            trend = round(float(fund['lastWeekGrowth']) * 4 - float(fund['lastMonthGrowth']), 2)
            rank = Rank(code=fund["code"], name=fund["name"], netWorthDate=fund["netWorthDate"],
                        netWorth=fund["netWorth"], dayGrowth=fund["dayGrowth"],
                        lastWeekGrowth=get_numeric(fund, "lastWeekGrowth"),
                        lastMonthGrowth=get_numeric(fund, "lastMonthGrowth"),
                        lastThreeMonthsGrowth=get_numeric(fund, "lastThreeMonthsGrowth"),
                        lastSixMonthsGrowth=get_numeric(fund, "lastSixMonthsGrowth"),
                        lastYearGrowth=get_numeric(fund, "lastYearGrowth"),
                        trend=trend)
            ranks.add(rank)

        self.__dao.add_rank(ranks)

    def sync_favourite(self, codes):
        if codes is None:
            return

        for i in range(0, len(codes), self.page_size):
            self.load_favourite(codes[i:i + self.page_size])

    def load_favourite(self, codes):
        if codes is None:
            return

        params = ''
        for index, code in enumerate(codes):
            params += code
            if index != len(codes) - 1:
                params += ','

        print('params = ' + params)
        data = Network.get_req(self.fund_url, {'code': params})

        if data is None:
            return

        favourites = set()
        for fund in data:
            favourite = Favourite(code=fund["code"], name=fund["name"])
            favourites.add(favourite)

        self.__dao.add_favourite(favourites)

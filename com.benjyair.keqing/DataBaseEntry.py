from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Favourite(Base):
    __tablename__ = "favourites"

    code = Column(String(64), primary_key=True)
    name = Column(String(64))

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __str__(self):
        return '基金代码：%s  基金名称：%s' % (self.code, self.name)


class Rank(Base):
    __tablename__ = "ranks"

    code = Column(String(64), primary_key=True)
    name = Column(String(64))
    netWorthDate = Column(String(64), primary_key=True)
    netWorth = Column(DECIMAL(10, 2))
    dayGrowth = Column(DECIMAL(5, 2))
    lastWeekGrowth = Column(DECIMAL(10, 2))
    lastMonthGrowth = Column(DECIMAL(10, 2))
    lastThreeMonthsGrowth = Column(DECIMAL(10, 2))
    lastSixMonthsGrowth = Column(DECIMAL(10, 2))
    lastYearGrowth = Column(DECIMAL(10, 2))
    trend = Column(DECIMAL(10, 2))

    def __init__(self, code, name, netWorthDate, netWorth, dayGrowth, lastWeekGrowth, lastMonthGrowth,
                 lastThreeMonthsGrowth, lastSixMonthsGrowth, lastYearGrowth, trend):
        self.code = code
        self.name = name
        self.netWorthDate = netWorthDate
        self.netWorth = netWorth
        self.dayGrowth = dayGrowth
        self.lastWeekGrowth = lastWeekGrowth
        self.lastMonthGrowth = lastMonthGrowth
        self.lastThreeMonthsGrowth = lastThreeMonthsGrowth
        self.lastSixMonthsGrowth = lastSixMonthsGrowth
        self.lastYearGrowth = lastYearGrowth
        self.trend = trend

    def __str__(self):
        return '基金代码：%s  基金名称：%s' % (self.code, self.name)

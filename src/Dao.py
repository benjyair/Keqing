from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import DataBaseEntry as Entry


class MysqlDao:
    __engine = None
    __session = None

    def connect(self):
        self.__engine = create_engine("mysql://keqing:abc123@192.168.192.1:3306/Keqing?charset=utf8", echo=True)
        self.__session = sessionmaker(bind=self.__engine)

    def dispose(self):
        self.__engine.dispose()

    def init_table(self):
        Entry.Base.metadata.create_all(self.__engine)

    def add_rank(self, ranks):
        session = self.__session()
        for fund in ranks:
            session.query(Entry.Rank) \
                .filter(Entry.Rank.code == fund.code, Entry.Rank.netWorthDate == fund.netWorthDate) \
                .delete()
            session.add(fund)
        session.commit()

    def add_favourite(self, favourites):
        session = self.__session()
        for it in favourites:
            session.query(Entry.Favourite).filter(Entry.Favourite.code == it.code).delete()
            session.add(it)
        session.commit()

    def get_favourite(self):
        session = self.__session()
        return session.query(Entry.Favourite).all()

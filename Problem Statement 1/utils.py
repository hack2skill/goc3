from features import date_time, news, sys_stat

class DesktopAssistant:
    def __init__(self):
        pass

    def tell_time(self):
        return date_time.time()

    def system_info(self):
        return sys_stat.system_stats()

    def news(self):
        """
        Fetch top news of the day from google news
        :return: news list of string if True, False if fail
        """
        return news.get_news()
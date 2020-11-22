class TeamEntity:
    __score = None
    __title = None
    __country = None

    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_country(self, country):
        self.__country = country

    def get_country(self):
        return self.__country

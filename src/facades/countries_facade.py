from src.logic.countries_logic import CountriesLogic


class CountriesFacade:
    def __init__(self):
        self.countries = []

    @staticmethod
    def get_all_countries():
        logic = CountriesLogic()
        return logic.get_all_countries()

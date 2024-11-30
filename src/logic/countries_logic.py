from src.utils.dal import DAL


class CountriesLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_countries(self):
        query = "SELECT country_name FROM countries ORDER BY country_name ASC"
        countries = self.dal.get_table(query)
        return countries

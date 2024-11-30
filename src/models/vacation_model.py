# ✅
class VacationModel:
    PARAM_COUNT = 8

    def __init__(
            self,
            vacation_id,
            vacation_name,
            vacation_description,
            start_date,
            end_date,
            price,
            vacation_img,
            country_name,  # Assuming country_name is used instead of country_id here
            likes,
            vacation_days
    ):
        self.vacation_id = vacation_id
        self.vacation_name = vacation_name
        self.vacation_description = vacation_description
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
        self.vacation_img = vacation_img
        self.country_name = country_name
        self.likes = likes
        self.vacation_days = vacation_days

    def __str__(self):
        return (
            f"Vacation ID: {self.vacation_id}\n"
            f"Vacation Name: {self.vacation_name}\n"
            f"Description: {self.vacation_description}\n"
            f"Start Date: {self.start_date}\n"
            f"End Date: {self.end_date}\n"
            f"Price: {self.price}\n"
            f"Photo: {self.vacation_img}\n"
            f"Country name: {self.country_name}\n"
            f"Total Likes: {str(self.likes)}"
            f"Vacation Days: {str(self.vacation_days)}"
        )

    @staticmethod
    def dict_to_vacation(dict):
        return VacationModel(
            dict["vacation_id"],
            dict["vacation_name"],
            dict["vacation_description"],
            dict["start_date"],
            dict["end_date"],
            dict["price"],
            dict["vacation_img"],
            dict["country_name"],
            dict["likes"],
            dict["vacation_days"]
        )

    @staticmethod
    def dicts_to_vacations(dicts_list):
        return [VacationModel.dict_to_vacation(item) for item in dicts_list]

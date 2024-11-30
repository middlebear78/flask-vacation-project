from datetime import datetime

from src.models.vacation_model import VacationModel
from src.utils.dal import DAL
from src.utils.image_handler import ImageHandler


class VacationLogic:
    def __init__(self):
        self.dal = DAL()
        self.vacation_model = VacationModel

    def get_all_vacations(self):
        query = """
            SELECT v.*, c.country_name
            FROM project3.vacations v
            JOIN countries c ON v.country_id = c.country_id
            ORDER BY v.start_date ASC
        """
        results = self.dal.get_table(query)
        if results:
            vacations = VacationModel.dicts_to_vacations(results)
            if vacations:
                return vacations
        raise ValueError("Failed to retrieve vacations.")

    def get_one_vacation(self, vacation_id):
        query = """
            SELECT v.*, c.country_name
            FROM project3.vacations v
            JOIN countries c ON v.country_id = c.country_id
            WHERE v.vacation_id = %s
            ORDER BY v.start_date ASC
        """
        result = self.dal.get_scalar(query, (vacation_id,))
        if result:
            vacation = VacationModel.dict_to_vacation(result)
            if vacation:
                print(f"Retrieving vacation with id {vacation_id}:")
                return vacation
        raise ValueError(f"Failed to retrieve vacation with id {vacation_id}.")

    def add_vacation(self, vacation_name, vacation_description, start_date, end_date, price, image, country, likes=0):
        try:
            image_name = ImageHandler.save_image(image)
            query = """
            INSERT INTO project3.vacations
            (
                vacation_name,
                vacation_description,
                start_date,
                end_date,
                price,
                vacation_img,
                country_id,
                likes,
                vacation_days
            )
            VALUES
            (
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                (SELECT country_id FROM countries WHERE country_name = %s), 
                %s, 
                (DATEDIFF(%s, %s) + 1)
            )
            """
            params = (
                vacation_name, vacation_description, start_date, end_date, price, image_name, country, likes, end_date,
                start_date)
            result = self.dal.insert(query, params)
            if result:
                print("Vacation added to the database!")
                return result
            else:
                print("Failed to add vacation to the database.")
                return None
        except Exception as e:
            print(f"Error adding vacation: {str(e)}")
            return None

    def update_vacation(self, vacation_id, vacation_name, vacation_description, start_date, end_date, price, image,
                        country):

        old_image_name = self.get_old_image_name(vacation_id)

        image_name = ImageHandler.update_image(old_image_name, image)

        try:
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
            vacation_days = (end_date_obj - start_date_obj).days + 1
        except ValueError as ve:
            print(f"Date format error: {ve}")
            vacation_days = 0

        query = """
            UPDATE project3.vacations
            SET vacation_name = %s,
                vacation_description = %s,
                start_date = %s,
                end_date = %s,
                price = %s,
                vacation_img = %s,
                country_id = (SELECT country_id FROM countries WHERE country_name = %s),
                vacation_days = %s
            WHERE vacation_id = %s
        """
        params = (vacation_name, vacation_description, start_date, end_date, price, image_name, country, vacation_days,
                  vacation_id)
        result = self.dal.update(query, params)
        if result:
            print(f"Vacation with id {vacation_id} updated successfully.")
            return result
        else:
            print("Failed to update vacation.")
            return None

    def del_vacation(self, vacation_id):
        query = "DELETE FROM project3.vacations WHERE vacation_id = %s"
        params = (vacation_id,)
        result = self.dal.delete(query, params)
        if result:
            print(f"Vacation with id {vacation_id} deleted from the database.")
            return result
        else:
            print("Failed to delete vacation.")
            return None

    def get_old_image_name(self, vacation_id):
        query = "SELECT vacation_img FROM project3.vacations WHERE vacation_id = %s"
        result = self.dal.get_scalar(query, (vacation_id,))
        print(f"Result for vacation_id {vacation_id}: {result}")  # Debugging line
        if result:
            return result.get("vacation_img")  # Use .get() to handle missing keys safely
        else:
            print(f"No image found for vacation with id {vacation_id}.")
            return None

    # ----------------------------------------------------------------------------------

    def check_vacation_exists(self, vacation_id):
        query = "SELECT * FROM project3.vacations WHERE vacation_id = %s"
        params = (vacation_id,)
        result = self.dal.get_scalar(query, params)
        return bool(result)

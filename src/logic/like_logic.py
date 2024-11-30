from src.logic.vacation_logic import VacationLogic
from src.utils.dal import DAL


class LikeLogic:
    def __init__(self):
        self.vacation_logic = VacationLogic()
        self.dal = DAL()

    def add_to_vacation_count_of_likes(self, vacation_id):
        query = "UPDATE vacations SET likes = likes + 1 WHERE vacation_id = %s"
        params = (vacation_id,)
        result = self.dal.update(query, params)

        if result is not None:
            print("Like Added to vacation total sum of likes.")
            return result
        else:
            raise ValueError("Failed to add Like to vacation total sum of likes.")

    def like_vacation(self, user_id, vacation_id):

        query = "INSERT INTO likes (user_id, vacation_id) VALUES (%s, %s)"
        params = (user_id, vacation_id)
        result = self.dal.insert(query, params)

        if result is not None:
            print("Like Added to 👍!")
            return result
        else:
            raise ValueError("Failed to add Like.")

    def unlike_vacation(self, user_id, vacation_id):
        params = (user_id, vacation_id)
        query = "DELETE FROM likes WHERE user_id = %s AND vacation_id = %s"
        result = self.dal.delete(query, params)
        if result is not None:
            print("Like Deleted!")
            return result
        else:
            raise ValueError("Failed to delete Like.")

    def increment_vacation_count_of_likes(self, vacation_id):
        query = "UPDATE vacations SET likes = likes - 1 WHERE vacation_id = %s"
        params = (vacation_id,)
        result = self.dal.update(query, params)

        if result is not None:
            print("Like incremented from vacation total sum of likes!")
            return result
        else:
            raise ValueError("Failed to increment Like from vacation total sum of likes.")

    # def check_user_exists(self, user_id):  # ✅
    #     query = "SELECT * FROM users WHERE user_id = %s"
    #     params = (user_id,)
    #     result = self.dal.get_scalar(query, params)
    #     return bool(result)
    #
    # def check_like_exists(self, user_id, vacation_id):  # ✅
    #     query = "SELECT * FROM likes WHERE user_id = %s AND vacation_id = %s"
    #     params = (user_id, vacation_id)
    #     result = self.dal.get_scalar(query, params)
    #     return bool(result)

    def get_all_likes_for_user(self, user_id):
        query = "SELECT vacation_id FROM likes WHERE user_id = %s"
        params = (user_id,)
        liked_vacations = self.dal.get_table(query, params)
        print(liked_vacations)
        return liked_vacations

    def get_all_likes_for_vacation(self, vacation_id):
        query = "SELECT user_id FROM likes WHERE vacation_id = %s"
        params = (vacation_id,)
        result = self.dal.get_table(query, params)

        # Calculate the number of likes by determining the length of the result list
        liked_vacations_sum = len(result) if result else 0
        print(liked_vacations_sum)
        return liked_vacations_sum

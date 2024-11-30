from src.logic.like_logic import LikeLogic


class LikeFacade:
    def __init__(self):
        self.logic = LikeLogic()

    def add_like(self, user_id, vacation_id):
        self.logic.like_vacation(user_id, vacation_id)
        self.logic.add_to_vacation_count_of_likes(vacation_id)
        updated_like_number = self.logic.get_all_likes_for_vacation(vacation_id)
        return updated_like_number

    def del_like(self, user_id, vacation_id):
        self.logic.unlike_vacation(user_id, vacation_id)
        self.logic.increment_vacation_count_of_likes(vacation_id)
        updated_like_number = self.logic.get_all_likes_for_vacation(vacation_id)
        return updated_like_number

    def get_all_likes_for_user(self, user_id):
        likes = self.logic.get_all_likes_for_user(user_id)
        return likes

    def get_all_likes_for_vacation_user(self, vacation_id):
        likes_sum = self.logic.get_all_likes_for_vacation_user(vacation_id)
        return likes_sum

    # class LikeFacade:
    # PARAM_COUNT = 2
    #
    # def __init__(self):
    #     self.params = {"user_id": None, "vacation_id": None}
    #     self.like_logic = LikesLogic()
    #     self.vacation_logic = VacationLogic()
    #     self.user_logic = UsersLogic()
    #     self.dal = DAL()
    #
    # def validate_params(self):
    #     self._check_param_count()
    #     self._check_param_types()
    #     return True
    #
    # def _check_param_count(self):  # ✅
    #     if len(self.params) != self.PARAM_COUNT:
    #         raise ValueError(
    #             "Exactly two parameters (user ID and vacation ID) are required to handle likes.\n"
    #         )
    #
    # def _check_param_types(self):  # ✅
    #     if not all(isinstance(param, int) for param in self.params.values()):
    #         raise ValueError("Both user ID and vacation ID must be integers!\n")
    #
    # def add_like(self):  # ✅
    #     if self.validate_params():
    #         if self.like_logic.check_user_exists(
    #                 self.params["user_id"]
    #         ) and self.vacation_logic.check_vacation_exists(self.params["vacation_id"]):
    #             if not self.like_logic.check_like_exists(*self.params.values()):
    #                 self.like_logic.add_like(*self.params.values())
    #                 self._clear_params()
    #             else:
    #                 raise ValueError(
    #                     "Like already exists for this user and vacation.\n"
    #                 )
    #         else:
    #             raise ValueError("User or Vacation do not exist.\n")
    #
    #
    # #
    # # def del_like(self):  # ✅
    # #     if self.validate_params():
    # #         if self.like_logic.check_like_exists(*self.params.values()):
    # #             self.like_logic.del_like(*self.params.values())
    # #             self._clear_params()
    # #         else:
    # #             raise ValueError("Like does not exist.\n")
    # #
    # # def _clear_params(self):
    # #     self.params = {"user_id": "", "vacation_id": ""}
    #
    # class LikeFacade:
    #     def __init__(self):
    #         self.logic = LikeLogic()
    #         self.dal = DAL()
    #
    #     def like(self, user_id, vacation_id):
    #         return (
    #             self.logic.add_to_vacation_count_of_likes(vacation_id),
    #             self.logic.like(user_id, vacation_id)
    #         )
    #
    #     def unlike(self, user_id, vacation_id):
    #         return (
    #             self.logic.unlike(user_id, vacation_id),
    #             self.logic.increment_vacation_count_of_likes(vacation_id))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dal.close()

from datetime import datetime

from flask import request

from src.facades.auth_facade import AuthFacade
from src.logic.vacation_logic import VacationLogic
from src.models.client_error import ValidationError
from src.utils.dal import DAL


class VacationFacade:
    PARAM_COUNT = 8

    def __init__(self):

        self.params = {
            "vacation_id": None,
            "vacation_name": None,
            "vacation_description": None,
            "start_date": "",
            "end_date": "",
            "price": 0,
            "vacation_img": None,
            "country_name": None,
        }

        self.dal = DAL()
        self.vacation_logic = VacationLogic()
        self.current_date = datetime.now().date()  # Use date object
        self.auth = AuthFacade()

    def _check_param_fill(self):

        required_fields = [
            "vacation_name", "vacation_description",
            "start_date", "end_date", "price", "vacation_img", "country_name"
        ]

        # Collect missing fields
        missing_fields = [field for field in required_fields if not self.params.get(field)]

        if missing_fields:
            raise ValidationError(f"The following fields are required: {', '.join(missing_fields)}")

    def _check_param_fill_to_update(self):

        required_fields = [
            "vacation_id", "vacation_name", "vacation_description",
            "start_date", "end_date", "price", "country_name"
        ]

        updated_missing_fields = [field for field in required_fields if not self.params.get(field)]
        if updated_missing_fields:
            raise ValidationError(f"The following fields are required: {', '.join(updated_missing_fields)}")

    def _check_price_range(self):
        if not (0 <= self.params["price"] <= 10000):
            raise ValidationError("Price must be between 0 and 10,000.")

    def _check_date_order(self):
        start_date = datetime.strptime(self.params["start_date"], "%Y-%m-%d").date()
        end_date = datetime.strptime(self.params["end_date"], "%Y-%m-%d").date()
        if start_date > end_date:
            raise ValidationError("Start date cannot exceed end date.")

    def _check_date_past(self):
        start_date = datetime.strptime(self.params["start_date"], "%Y-%m-%d").date()
        end_date = datetime.strptime(self.params["end_date"], "%Y-%m-%d").date()
        if start_date < self.current_date or end_date < self.current_date:
            raise ValidationError("Vacation dates cannot start or end in the past.")

    def get_all_vacations(self):
        # self.auth.block_anonymous()
        return self.vacation_logic.get_all_vacations()

    def get_one_vacation(self, id):
        return self.vacation_logic.get_one_vacation(id)

    def add_vacation(self):
        self.auth.block_non_admin()

        # Retrieve form data
        vacation_name = request.form.get("vacation_name")
        vacation_description = request.form.get("vacation_description")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        price = request.form.get("price")
        image = request.files.get("vacation_image")
        country = request.form.get("country")

        # Validate and convert price
        if price:
            try:
                self.params["price"] = float(price)
            except ValueError:
                raise ValidationError("Price must be a valid number.")
        else:
            raise ValidationError("Price is required.")

        self.params.update({
            "vacation_name": vacation_name,
            "vacation_description": vacation_description,
            "start_date": start_date,
            "end_date": end_date,
            "price": self.params["price"],
            "vacation_img": image,
            "country_name": country,
        })

        self._check_param_fill()
        self._check_price_range()
        self._check_date_order()
        self._check_date_past()

        self.vacation_logic.add_vacation(
            vacation_name, vacation_description, start_date, end_date, self.params["price"], image, country)

    def update_vacation(self):
        self.auth.block_non_admin()

        vacation_id = request.form.get("vacation_id")
        vacation_name = request.form.get("vacation_name")
        vacation_description = request.form.get("vacation_description")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        price = request.form.get("price")
        image = request.files.get("vacation_image")  # Use get() to handle missing files gracefully
        country = request.form.get("country")

        # Validate and convert price
        if price:
            try:
                self.params["price"] = float(price)
            except ValueError:
                raise ValidationError("Price must be a valid number.")
        else:
            raise ValidationError("Price is required.")

        self.params.update({
            "vacation_id": vacation_id,
            "vacation_name": vacation_name,
            "vacation_description": vacation_description,
            "start_date": start_date,
            "end_date": end_date,
            "price": self.params["price"],
            "vacation_img": image,
            "country_name": country,
        })


        self._check_param_fill_to_update()
        self._check_price_range()
        self._check_date_order()
        # self._check_date_past()

        try:
            if not vacation_id:
                raise ValidationError("Vacation ID is required for update.")

            self.vacation_logic.update_vacation(
                vacation_id, vacation_name, vacation_description, start_date, end_date, self.params["price"],
                self.params["vacation_img"],
                country
            )
        except ValidationError as e:
            raise ValidationError(str(e))

    def delete_vacation(self, id):
        self.auth.block_non_admin()
        if self.vacation_logic.check_vacation_exists(id):
            self.vacation_logic.del_vacation(id)
        else:
            raise ValueError("Vacation does not exist in the Database.\n")

    def _clear_params(self):
        self.params = {
            "vacation_id": None,
            "vacation_name": None,
            "vacation_description": None,
            "start_date": "",
            "end_date": "",
            "price": 0,
            "vacation_img": None,
            "country_name": None,
        }

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.dal.close()
        except Exception as err:
            print(f"Error closing connection: {err}")

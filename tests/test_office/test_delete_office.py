import json

from tests.base import BaseTestCase, CommonTestCases
from helpers.database import engine, db_session
from fixtures.office.update_delete_office_fixture import (
    delete_office_mutation,
    delete_office_mutation_response,
    delete_non_existent_office_mutation,
    delete_unauthorised_location_mutation,
    response_for_delete_office_with_database_error
)
from fixtures.token.token_fixture import ADMIN_TOKEN


class TestDeleteOffice(BaseTestCase):
    def test_delete_office(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            delete_office_mutation,
            delete_office_mutation_response
        )

    def test_delete_non_existent_office(self):
        CommonTestCases.admin_token_assert_in(
            self,
            delete_non_existent_office_mutation,
            "Office not found"
        )

    def test_delete_unautorised_location(self):
        headers = {"Authorization": "Bearer" + " " + ADMIN_TOKEN}
        response = self.app_test.post('mrm?query='+delete_unauthorised_location_mutation,  # noqa: E501
                                      headers=headers)
        expected_response = json.loads(response.data)
        self.assertIn("Office not found", expected_response['errors'][0]['message'])  # noqa: E501

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            delete_office_mutation,
            "The database cannot be reached"
            )

    def test_delete_office_without_office_model(self):
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE offices CASCADE")
        CommonTestCases.admin_token_assert_equal(
            self,
            delete_office_mutation,
            response_for_delete_office_with_database_error
        )

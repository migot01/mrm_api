import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from helpers.database import engine, db_session
from fixtures.wing.wing_fixtures import (
    update_wing_mutation,
    update_duplicate_wing_mutation,
    update_wing_response,
    wing_update_no_name,
    update_duplicate_wing_mutation_response,
    update_wing_id_not_found
)

sys.path.append(os.getcwd())


class TestCreateWing(BaseTestCase):

    def test_wing_update(self):
        """
        Testing for wing creation
        """
        CommonTestCases.lagos_admin_token_assert_equal(
            self,
            update_wing_mutation,
            update_wing_response
        )

    def test_wing_update_duplication(self):
        """
        Testing for wing duplication
        """
        CommonTestCases.lagos_admin_token_assert_equal(
            self,
            update_duplicate_wing_mutation,
            update_duplicate_wing_mutation_response
        )

    def test_wing_update_no_name(self):
        """
        Testing for wing update with no name
        """
        CommonTestCases.lagos_admin_token_assert_in(
            self,
            wing_update_no_name,
            "name is required field"
        )

    def test_wing_update_other_location(self):
        """
        Testing for wing update in other location apart from Lagos
        """
        CommonTestCases.admin_token_assert_in(
            self,
            update_wing_mutation,
            "This action is restricted to Lagos Office admin"
        )

    def test_update_wing_id_notfound(self):
        """
        Testing for wing creation when floor is not found
        """
        CommonTestCases.lagos_admin_token_assert_in(
            self,
            update_wing_id_not_found,
            "Wing not found"
        )

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            update_wing_mutation,
            "The database cannot be reached"
            )

    def test_wing_update_without_wings_model(self):
        """
        Test awing cannot be updated without a wings model
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE wings CASCADE")
        CommonTestCases.lagos_admin_token_assert_in(
            self,
            update_wing_mutation,
            "does not exist"
        )

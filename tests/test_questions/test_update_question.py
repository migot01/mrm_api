import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from helpers.database import engine, db_session
from fixtures.questions.create_questions_fixtures import (
   update_question_mutation,
   update_question_response,
   update_question_invalidId,
   query_update_total_views_of_questions
)


sys.path.append(os.getcwd())


class TestUpdateQuestion(BaseTestCase):

    def test_question_update(self):
        """
        Testing for question update

        """
        CommonTestCases.admin_token_assert_equal(
            self,
            update_question_mutation,
            update_question_response
        )

    def test_question_update_with_invalid_id(self):
        """
        Test question creation with field empty
        """
        CommonTestCases.admin_token_assert_in(
            self,
            update_question_invalidId,
            "Question not found"
        )

    def test_increment_total_views_of_questions(self):
        """
        Testing for incrementing the number of views
        for a room's feedback qustion

        """
        CommonTestCases.user_token_assert_in(
            self,
            query_update_total_views_of_questions,
            '1'
        )
        CommonTestCases.user_token_assert_in(
            self,
            query_update_total_views_of_questions,
            '2'
        )

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            update_question_mutation,
            "The database cannot be reached"
            )

    def test_update_question_without_question_model(self):
        """
        test question cannot be updated without questions model
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE questions CASCADE")
        CommonTestCases.admin_token_assert_in(
            self,
            update_question_mutation,
            "does not exist"
        )

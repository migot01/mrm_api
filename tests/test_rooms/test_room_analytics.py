import json

from tests.base import BaseTestCase
from fixtures.token.token_fixture import (admin_api_token)
from fixtures.room.room_analytics_fixtures import (
    get_least_used_room_per_week_query,
    get_least_used_room_per_week_response,
    get_least_used_room_without_event_query,
    get_least_used_room_without_event_response

)


class QueryRoomsAnalytics(BaseTestCase):

    api_headers = {'token': admin_api_token}

    def test_analytics_for_least_used_room_weekly(self):
        analytics_query = self.app_test.post(
            '/mrm?query=' + get_least_used_room_per_week_query, headers=self.api_headers)  # noqa: E501
        actual_response = json.loads(analytics_query.data)
        expected_response = get_least_used_room_per_week_response
        self.assertEquals(actual_response, expected_response)

    def test_analytics_for_least_used_room_without_event_weekly(self):
        analytics_query = self.app_test.post(
            '/mrm?query=' + get_least_used_room_without_event_query, headers=self.api_headers)  # noqa: E501
        actual_response = json.loads(analytics_query.data)
        expected_response = get_least_used_room_without_event_response
        self.assertEquals(actual_response, expected_response)
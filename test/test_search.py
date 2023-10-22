import unittest
from unittest.mock import patch

from app import create_app


class TestSearchBlueprint(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    @patch('utility.database.SQLHelper.get_connection_pool')
    def test_get_event_start_with(self, mock_get_connection_pool):
        mock_connection = mock_get_connection_pool.return_value.getconn.return_value
        mock_cursor = mock_connection.cursor.return_value

        expected_data = [{'event_id': 1, 'event_name': 'Test Event'}]
        mock_cursor.fetchall.return_value = expected_data

        mock_cursor.execute.return_value = None

        mock_start_with = 'Mocked'

        response = self.client.get('/search/event_start_with', query_string={'start_with': mock_start_with})
        data = response.get_json()

        mock_cursor.execute.assert_called_once()
        self.assertEqual(data, expected_data)

    


if __name__ == '__main__':
    unittest.main()

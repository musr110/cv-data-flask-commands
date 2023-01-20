import unittest

from app import app


class TestCVAPI(unittest.TestCase):

    # set up test client
    def setUp(self):
        self.app = app.test_client()

    # test the personal endpoint
    def test_get_personal(self):
        response = self.app.get("/personal")
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["name"], "John Doe")
        self.assertEqual(data["email"], "johndoe@email.com")
        self.assertEqual(data["phone"], "555-555-5555")
        self.assertEqual(data["location"], "New York, NY")

    # test the experience endpoint without year parameter
    def test_get_experience(self):
        response = self.app.get("/experience")
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["title"], "Software Developer")
        self.assertEqual(data[1]["title"], "Senior Software Engineer")

    # test the experience endpoint with year parameter
    def test_get_experience_year(self):
        response = self.app.get("/experience?year=2018")
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["title"], "Senior Software Engineer")

    # test the experience endpoint with invalid year parameter
    def test_get_experience_year_invalid(self):
        response = self.app.get("/experience?year=2017")
        data = response.get_json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["error"], "Invalid year")

    # test the experience endpoint by year
    def test_get_experience_by_year(self):
        response = self.app.get("/experience/2018")
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["title"], "Senior Software Engineer")

    # test the education endpoint
    def test_get_education(self):
        response = self.app.get("/education")
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["degree"], "Bachelor of Science in Computer Science")
        self.assertEqual(data[1]["degree"], "Master of Science in Computer Science")


if __name__ == "__main__":
    unittest.main()

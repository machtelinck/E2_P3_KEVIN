from django.test import TestCase
from django.urls import reverse
from .utils import make_prediction


class TestUtils(TestCase):
    def test_good_prediction(self):
        good_input = {
            'Year_Built': '1990',
            'Total_Bsmt_SF': '1000',
            '1st_Flr_SF': '1200',
            'Gr_Liv_Area': '1800',
            'Garage_Area': '500',
            'Overall_Qual': '8',
            'Full_Bath': '2',
            'Exter_Qual': 'TA',
            'Kitchen_Qual': 'Gd',
            'Neighborhood': 'CollgCr'
        }

        prediction = make_prediction(good_input)
        self.assertEqual(prediction, 220863)

    def test_wrong_prediction(self):
        wrong_input = {
            'Year_Built': '1990',
            'Total_Bsmt_SF': '1000',
            '1st_Flr_SF': '1200',
            'Gr_Liv_Area': '1800',
            'Garage_Area': '500',
            'Overall_Qual': '8',
            'Full_Bath': '2',
            'Exter_Qual': 24,
            'Kitchen_Qual': 'Gd',
            'Neighborhood': 'CollgCr'
        }

        prediction = make_prediction(wrong_input)
        self.assertEqual(prediction, 0)


class TestViews(TestCase):
    def test_index_view(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_predict_view_post_method(self):
        url = reverse('predict')
        data = {
            'Year_Built': '1990',
            'Total_Bsmt_SF': '1000',
            '1st_Flr_SF': '1200',
            'Gr_Liv_Area': '1800',
            'Garage_Area': '500',
            'Overall_Qual': '8',
            'Full_Bath': '2',
            'Exter_Qual': 'TA',
            'Kitchen_Qual': 'Gd',
            'Neighborhood': 'CollgCr'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertEqual(int(response.context['data']), 220863)

    def test_predict_view_post_method(self):
        url = reverse('predict')
        data = {
            'Year_Built': '1990',
            'Total_Bsmt_SF': '1000',
            '1st_Flr_SF': '1200',
            'Gr_Liv_Area': '1800',
            'Garage_Area': '500',
            'Overall_Qual': '8',
            'Full_Bath': '2',
            'Exter_Qual': '24',
            'Kitchen_Qual': 'Gd',
            'Neighborhood': 'CollgCr'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"The Input is not Correct")

    def test_predict_view_get_method(self):
        url = reverse('predict')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Method Not Allowed")

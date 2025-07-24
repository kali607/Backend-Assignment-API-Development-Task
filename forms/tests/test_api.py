from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from forms.models import BogieForm, WheelForm

class BogieAPITestCase(APITestCase):
    def test_create_bogie_form(self):
        url = reverse('bogie-form-list-create')
        data = {
            "form_number": "B002",
            "inspection_by": "Inspector Mani",
            "inspection_date": "2025-07-23",
            "bogie_no": "BG456",
            "date_of_ioh": "2025-07-01",
            "deficit_components": "Brake pads",
            "incoming_div_and_date": "SC-2025-07-20",
            "maker_year_built": "XYZ Ltd - 2021",
            "axle_guide": "Fair",
            "bogie_frame_condition": "Good",
            "bolster": "Needs Inspection",
            "bolster_suspension_bracket": "Slightly Worn",
            "lower_spring_seat": "OK",
            "adjusting_tube": "Loose",
            "cylinder_body": "OK",
            "piston_trunnion": "Rusty",
            "plunger_spring": "Old"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BogieForm.objects.count(), 1)
        self.assertEqual(BogieForm.objects.get().form_number, "B002")

class WheelAPITestCase(APITestCase):
    def test_create_wheel_form(self):
        url = reverse('wheel-form-list-create')
        data = {
            "form_number": "W002",
            "submitted_by": "Inspector Bala",
            "submitted_date": "2025-07-23",
            "axle_box_housing_bore_dia": "82mm",
            "bearing_seat_diameter": "102mm",
            "condemning_dia": "111mm",
            "intermediate_wwp": "96mm",
            "last_shop_issue_size": "106mm",
            "roller_bearing_bore_dia": "122mm",
            "roller_bearing_outer_dia": "152mm",
            "roller_bearing_width": "52mm",
            "tread_diameter_new": "842mm",
            "variation_same_axle": "1mm",
            "variation_same_bogie": "2mm",
            "variation_same_coach": "3mm",
            "wheel_disc_width": "36mm",
            "wheel_gauge": "1678mm",
            "wheel_profile": "Re-profiled"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(WheelForm.objects.count(), 1)
        self.assertEqual(WheelForm.objects.get().form_number, "W002")

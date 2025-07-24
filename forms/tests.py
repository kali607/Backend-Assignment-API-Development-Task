from django.test import TestCase
from forms.models import BogieChecksheetForm, WheelSpecificationForm

class BogieChecksheetFormTest(TestCase):
    def test_create_bogie_form(self):
        form = BogieChecksheetForm.objects.create(
            form_number="B001",
            inspection_by="Inspector Ram",
            inspection_date="2025-07-23",
            bogie_no="1234",
            date_of_ioh="2025-07-01",
            deficit_components="None",
            incoming_div_and_date="SCR/2025-07-20",
            maker_year_built="ICF/2015",
            axle_guide="OK",
            bogie_frame_condition="Good",
            bolster="New",
            bolster_suspension_bracket="Tight",
            lower_spring_seat="Aligned",
            adjusting_tube="Checked",
            cylinder_body="Good",
            piston_trunnion="Clean",
            plunger_spring="OK"
        )
        self.assertEqual(BogieChecksheetForm.objects.count(), 1)
        self.assertEqual(form.form_number, "B001")

class WheelSpecificationFormTest(TestCase):
    def test_create_wheel_form(self):
        form = WheelSpecificationForm.objects.create(
            form_number="W001",
            submitted_by="Inspector Sita",
            submitted_date="2025-07-23",
            axle_box_housing_bore_dia="80mm",
            bearing_seat_diameter="100mm",
            condemning_dia="110mm",
            intermediate_wwp="95mm",
            last_shop_issue_size="105mm",
            roller_bearing_bore_dia="120mm",
            roller_bearing_outer_dia="150mm",
            roller_bearing_width="50mm",
            tread_diameter_new="840mm",
            variation_same_axle="1mm",
            variation_same_bogie="2mm",
            variation_same_coach="3mm",
            wheel_disc_width="35mm",
            wheel_gauge="1676mm",
            wheel_profile="Standard"
        )
        self.assertEqual(WheelSpecificationForm.objects.count(), 1)
        self.assertEqual(form.form_number, "W001")

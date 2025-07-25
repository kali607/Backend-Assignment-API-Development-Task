# KPA Backend Assignment — Bogie and Wheel Form APIs

This is a Django REST Framework project developed for the KPA backend assignment. It includes two core APIs for managing Bogie Checksheet Forms and Wheel Specification Forms, with PostgreSQL as the backend database.

## 🚀 Tech Stack

- Python 3.x  
- Django 4.x  
- Django REST Framework  
- PostgreSQL  
- Postman (for API testing)

## 📦 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/kpa-backend.git
   cd kpa-backend
   ```

2. **Create virtual environment and install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up PostgreSQL database**
   - Create a PostgreSQL database (e.g., `kpa_db`)
   - Update your `.env` or `settings.py` with database credentials

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## 📮 API Endpoints

### Bogie Checksheet Form API

| Method | Endpoint              | Description               |
|--------|-----------------------|---------------------------|
| POST   | `/api/bogie/create/`  | Create a new bogie form   |
| GET    | `/api/bogie/list/`    | List all bogie forms      |

# Sample request:
    
  {
   "form_number": "B001",
   "inspection_by": "Inspector Raj",
   "inspection_date": "2025-07-23",
   "bogie_no": "BG123",
   "date_of_ioh": "2025-06-01",
   "deficit_components": "None",
   "incoming_div_and_date": "HYD-2025-06-20",
   "maker_year_built": "ABC Ltd - 2020",
   "axle_guide": "Good",
   "bogie_frame_condition": "Excellent",
   "bolster": "OK",
   "bolster_suspension_bracket": "OK",
   "lower_spring_seat": "OK",
   "adjusting_tube": "Fitted",
   "cylinder_body": "OK",
   "piston_trunnion": "Tight",
   "plunger_spring": "New"
}



### Wheel Specification Form API

| Method | Endpoint              | Description                   |
|--------|-----------------------|-------------------------------|
| POST   | `/api/wheel/create/`  | Create a new wheel form       |
| GET    | `/api/wheel/list/`    | List all wheel forms          |

# sample request:

    {
  "form_number": "W001",
  "submitted_by": "Inspector Sita",
  "submitted_date": "2025-07-23",
  "axle_box_housing_bore_dia": "80mm",
  "bearing_seat_diameter": "100mm",
  "condemning_dia": "110mm",
  "intermediate_wwp": "95mm",
  "last_shop_issue_size": "105mm",
  "roller_bearing_bore_dia": "120mm",
  "roller_bearing_outer_dia": "150mm",
  "roller_bearing_width": "50mm",
  "tread_diameter_new": "840mm",
  "variation_same_axle": "1mm",
  "variation_same_bogie": "2mm",
  "variation_same_coach": "3mm",
  "wheel_disc_width": "35mm",
  "wheel_gauge": "1676mm",
  "wheel_profile": "Standard"
}        
  

## ✅ Features Implemented

- Full Create + List APIs for Bogie and Wheel forms
- PostgreSQL integration
- Validation using DRF serializers
- Tested using Swagger and Postman
- Clean code structure with modular design


# Note:
      This project connects to a PostgreSQL instance running via Docker (manually started). Make sure your PostgreSQL container is running and accessible.

 # Assumptions & Notes
      ->All fields are required for form submission unless mentioned optional.

      ->Dates are expected in YYYY-MM-DD format.

      ->Currently, no file upload or user login is implemented.

## 📂 Postman Collection

The updated Postman collection with working API responses is included in the `backend_assignment_postman_collection.json` file.

# Author
     ->Created by Kali Krishna Mohan Kasani

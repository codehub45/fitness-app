#About App
- Create and manage fitness classes and time slots
- Book a slot for a specific class
- View available classes
- View bookings
- Admin panel for managing everything
- Sample Postman collection with test data

#Create and Activate Virtual Environment
- python -m venv env
- env\Scripts\activate

#install django
- pip install django

#Migrations
- python manage.py makemigrations
- python manage.py migrate

#git link is below
- https://github.com/codehub45/fitness-app/

#postman collection
- postman collection were added in json format

#sample API & Input
#classes
- Api:http://127.0.0.1:8001/fit/classes
- method: GET
- sample_output: { 
    "Yoga": [
        {
            "classes_id": 1,
            "slots": 1,
            "timing": "10:00:00-11:00:00",
            "instructor": "Instructor1"
        },
        {
            "classes_id": 1,
            "slots": 4,
            "timing": "14:00:00-15:00:00",
            "instructor": "Instructor1"
        }
    ],
    "Zumba": [
        {
            "classes_id": 2,
            "slots": 2,
            "timing": "11:00:00-12:00:00",
            "instructor": "Instructor2"
        },
        {
            "classes_id": 2,
            "slots": 5,
            "timing": "15:00:00-16:00:00",
            "instructor": "Instructor2"
        }
    ],
    "HITT": [
        {
            "classes_id": 3,
            "slots": 3,
            "timing": "12:00:00-13:00:00",
            "instructor": "Instructor3"
        },
        {
            "classes_id": 3,
            "slots": 6,
            "timing": "16:00:00-17:00:00",
            "instructor": "Instructor3"
        }
    ]
}

#book

- API :http://127.0.0.1:8001/fit/book
- method : POST
- sample_input: {
    "class_id":2,
    "client_name":"client1",
    "client_email":"client1@gmail.com",
    "slot":1,
    "date":"2025-06-07"
}

- sample output = {
    "Message": "success"

}

#bookings

- API : http://127.0.0.1:8001/fit/bookings?email=client1@gmail.com
- method : GET
- sample_output:{
    "client_name": "client1",
    "client_email": "client1@gmail.com",
    "classes": [
        {
            "class_id": 1,
            "class_name": "Yoga",
            "instructor": "Instructor1",
            "slot_timing": "10:00:00-11:00:00",
            "date": "2025-06-06"
        },
        {
            "class_id": 2,
            "class_name": "Zumba",
            "instructor": "Instructor2",
            "slot_timing": "15:00:00-16:00:00",
            "date": "2025-06-06"
        },
        {
            "class_id": 3,
            "class_name": "HITT",
            "instructor": "Instructor3",
            "slot_timing": "12:00:00-13:00:00",
            "date": "2025-06-07"
        },
        {
            "class_id": 2,
            "class_name": "Zumba",
            "instructor": "Instructor2",
            "slot_timing": "11:00:00-12:00:00",
            "date": "2025-06-07"
        }
    ]
}

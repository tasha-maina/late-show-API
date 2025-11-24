# Late Show API  
A Flask-based RESTful API for managing episodes, guests, and appearances for a Late Night TV show.

This project was built following an MVC architecture and includes full CRUD functionality, model relationships, validations, and RESTful routes.

## 📁 Project Structure

late-show-api/
│
├── server/
│ ├── app.py
│ ├── models.py
│ ├── routes.py
│ ├── seed.py
│ └── testing/
│ ├── conftest.py
│ ├── models_test.py
│ └── app_test.py
├── migrations/
├── app.db
├── requirements.txt
└── README.md

##  Technologies Used
- Python
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- Flask-Migrate
- SQLAlchemy Serializer
- SQLite (development database)
- Postman / Thunder Client (API testing)


## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone <https://github.com/tasha-maina/late-show-API.git>
cd late-show-api
2. Create and Activate Virtual Environment
python3 -m venv env
source env/bin/activate  
3. Install Dependencies
pip install -r requirements.txt
4. Run Database Migrations
Inside the server/ directory:
export FLASK_APP=app.py
flask db init
flask db revision --autogenerate -m "initial"
flask db upgrade
5. Seed the Database
python seed.py
6. Run the Server
bash
Copy code
python app.py
Go to:
👉 http://localhost:5555

🗂️ Database Models
Episode
id

date

number

Relationship: has many appearances → guests

Guest
id

name

occupation

Relationship: has many appearances → episodes

Appearance
id

rating

episode_id (FK)

guest_id (FK)

Validation: rating must be between 1 and 5

📡 API Endpoints
🔹 GET /episodes
Returns all episodes.

Example Response:

json
Copy code
[
  { "id": 1, "date": "1/11/99", "number": 1 },
  { "id": 2, "date": "1/12/99", "number": 2 }
]
🔹 GET /episodes/<id>
Returns one episode with its appearances.

404 Response:

json
{ "error": "Episode not found" }
🔹 DELETE /episodes/<id>
Deletes an episode and its appearances.

204 Response:
Empty JSON body.

🔹 GET /guests
Returns all guests.

🔹 POST /appearances
Creates a new appearance.

Request Body

json
Copy code
{
  "rating": 5,
  "episode_id": 1,
  "guest_id": 1
}
Validation Error Response

json
{ "errors": ["validation errors"] }
🧪 Testing
Run all tests using:
pytest -x
📌 Summary
This API implements:

MVC architecture

Complete RESTful routing

Many-to-many relationships through a join table

SQLAlchemy validations

Error handling (404, 400)

JSON serialization

Database migrations and seeding

Author

Built by Natasha Maina
For the Phase 4 Flask Code Challenge.


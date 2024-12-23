# Django Airline Booking System API

## **Project Description**
This is a simplified API for an airline booking system developed using the Django framework and Django Rest Framework (DRF). The API supports the management of flights and passengers, allowing users to perform CRUD (Create, Retrieve, Update, Delete) operations on these entities.

---

## **Setup Instructions**

Follow these steps to set up and run the project on your local machine:

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd airline_booking_system
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Database Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```
   The server will start on `http://127.0.0.1:8000/`.

---

## **API Endpoints**

Here are the main API endpoints:

### **Flights**

- **List All Flights**
  - URL: `/api/flights/`
  - Method: `GET`
  - Description: Retrieves a list of all flights.

- **Retrieve a Single Flight**
  - URL: `/api/flights/<id>/`
  - Method: `GET`
  - Description: Retrieves details of a specific flight by its ID.

- **Create a Flight**
  - URL: `/api/flights/`
  - Method: `POST`
  - Body Example:
    ```json
    {
        "flight_number": "AB123",
        "departure": "2024-12-25T08:00:00Z",
        "arrival": "2024-12-25T12:00:00Z",
        "origin": "Nairobi",
        "destination": "Mombasa",
        "capacity": 150
    }
    ```

- **Update a Flight**
  - URL: `/api/flights/<id>/`
  - Method: `PUT`
  - Body Example:
    ```json
    {
        "flight_number": "CD456",
        "departure": "2024-12-30T10:00:00Z",
        "arrival": "2024-12-30T14:00:00Z",
        "origin": "Kisumu",
        "destination": "Nairobi",
        "capacity": 100
    }
    ```

- **Delete a Flight**
  - URL: `/api/flights/<id>/`
  - Method: `DELETE`

### **Passengers**

- **List All Passengers**
  - URL: `/api/passengers/`
  - Method: `GET`
  - Description: Retrieves a list of all passengers.

- **Retrieve a Single Passenger**
  - URL: `/api/passengers/<id>/`
  - Method: `GET`
  - Description: Retrieves details of a specific passenger by their ID.

- **Create a Passenger**
  - URL: `/api/passengers/`
  - Method: `POST`
  - Body Example:
    ```json
    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "phone_number": "0712345678",
        "flight": 1
    }
    ```

- **Update a Passenger**
  - URL: `/api/passengers/<id>/`
  - Method: `PUT`
  - Body Example:
    ```json
    {
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "janesmith@example.com",
        "phone_number": "0723456789",
        "flight": 2
    }
    ```

- **Delete a Passenger**
  - URL: `/api/passengers/<id>/`
  - Method: `DELETE`

---

## **Postman Testing**

Use Postman to test the API endpoints. Here’s how:

1. **Base URL**: Use `http://127.0.0.1:8000/api/` as the base URL for all endpoints.

2. **Authentication**: No authentication is required for this exercise.

3. **Examples**:
   - **GET Request to List All Flights**:
     - URL: `/api/flights/`
     - Response:
       ```json
       [
           {
               "id": 1,
               "flight_number": "AB123",
               "departure": "2024-12-25T08:00:00Z",
               "arrival": "2024-12-25T12:00:00Z",
               "origin": "Nairobi",
               "destination": "Mombasa",
               "capacity": 150
           }
       ]
       ```

   - **POST Request to Create a Passenger**:
     - URL: `/api/passengers/`
     - Body:
       ```json
       {
           "first_name": "Alice",
           "last_name": "Johnson",
           "email": "alice.johnson@example.com",
           "phone_number": "0734567890",
           "flight": 1
       }
       ```
     - Response:
       ```json
       {
           "id": 1,
           "first_name": "Alice",
           "last_name": "Johnson",
           "email": "alice.johnson@example.com",
           "phone_number": "0734567890",
           "flight": {
               "id": 1,
               "flight_number": "AB123",
               "departure": "2024-12-25T08:00:00Z",
               "arrival": "2024-12-25T12:00:00Z",
               "origin": "Nairobi",
               "destination": "Mombasa",
               "capacity": 150
           }
       }
       ```

4. **Screenshots**: Use Postman’s "Send" button to test endpoints and capture screenshots of the results.

---

## **Design Decisions**

1. **Models**:
   - Used `ForeignKey` to relate `Passenger` to `Flight` to enforce the constraint that a passenger must be associated with exactly one flight.

2. **Serializers**:
   - `PassengerSerializer` includes flight details for easier data representation in responses.

3. **ViewSets**:
   - Simplified implementation using `ModelViewSet` for CRUD operations.

4. **Filtering and Pagination**:
   - Added filtering for flights and passengers to enhance usability.
   - Implemented pagination for better performance when dealing with large datasets.

---

## **Future Enhancements**

- Add user authentication and permissions for secure access to endpoints.
- Include flight seat availability management.
- Implement a booking system for passengers to reserve seats.


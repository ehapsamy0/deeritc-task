# Writing the README content to a file for download

readme_content = """


### Database Diagrams

![Database Diagrams](https://github.com/ehapsamy0/deeritc-task/blob/main/book-mang_task/erd/WhatsApp%20Image%202024-10-30%20at%2000.50.26.jpeg)



# Book Management API

This API provides a way to manage books and book-related bookings. It includes endpoints for creating, updating, and deleting books, as well as for creating and retrieving bookings. Authentication is required for certain operations.

## Table of Contents

1. [Authentication](#authentication)
2. [Book Operations](#book-operations)
3. [Booking Operations](#booking-operations)
4. [Examples](#examples)
5. [Setup and Running Locally](#setup-and-running-locally)

---

### Base URL

All API routes are prefixed by `/api`. For example, the login endpoint is `/api/auth/login`.

---

## Authentication

**Endpoint:** `/api/auth`

Authentication is required for certain book operations (create, update, and delete). This API uses JWT (JSON Web Tokens) for authentication.

- **POST** `/api/auth/login` - Login a user and receive a token.
  - **Request Body:** 
    ```json
    {
      "email": "string",
      "password": "string"
    }
    ```
  - **Response:** 
    ```json
    {
      "access_token": "your_jwt_token"
    }
    ```

- **POST** `/api/auth/register` - Register a new user.
  - **Request Body:** 
    ```json
    {
      "username": "string",
      "email": "string",
      "password": "string"
    }
    ```
  - **Response:** 
    ```json
    {
      "message": "User registered successfully."
    }
    ```

Use the token received from the `/login` endpoint in the `Authorization` header with the `Bearer` prefix for authenticated requests.

---

## Book Operations

**Endpoint:** `/api/books`

### 1. **POST** `/api/books/` - Create a new book

- **Authorization Required:** Yes
- **Request Body:**
  ```json
  {
    "title": "string",
    "description": "string",
    "author_id": "integer",
    "isbn": "string",
    "pages": "integer"
  }



- **Response**

 ```json
 {
  "book": {
    "id": "integer",
    "title": "string",
    "description": "string",
    "isbn": "string",
    "pages": "integer",
    "author": {
      "id": "integer",
      "username": "string",
      "email": "string"
    }
  }
}
```


### 2. **GET** `/api/books/` - Get all books with pagination and author details

- **Authorization Required: No**
- **Query Parameters:***
    - `page` - Page number (optional, default is 1)
    - `per_page` - Number of books per page (optional, default is 10)

- **Response**

```json

{
  "books": [
    {
      "id": "integer",
      "title": "string",
      "description": "string",
      "isbn": "string",
      "pages": "integer",
      "author": {
        "id": "integer",
        "username": "string",
        "email": "string"
      }
    }
  ],
  "total": "integer",
  "page": "integer",
  "pages": "integer",
  "per_page": "integer"
}
```


### 3. PUT /api/books/{book_id} - Update a book by ID

- **Authorization Required:** Yes
- **Path Parameter:**
  - `book_id` - ID of the book to update
- **Request Body:**

    ```json
    {
      "title": "string",
      "description": "string"
    }
    ```

- **Response:**

    ```json
    {
      "message": "Book updated successfully!"
    }
    ```

### 4. DELETE /api/books/{book_id} - Delete a book by ID

**Authorization Required**: Yes

**Path Parameter**:
- `book_id` - ID of the book to delete

**Response**:
```json
{
  "message": "Book deleted successfully!"
}
```
----

## Booking Operations

### Endpoint: `/api/books/{book_id}/booking`

#### 1. `POST /api/books/{book_id}/booking` - Create a booking for a book

- **Authorization Required**: Yes
- **Path Parameter**:
    - `book_id` - ID of the book to book

- **Request Body**:
    ```json
    {
      "customer_name": "string",
      "customer_contact": "string",
      "start_date": "YYYY-MM-DD",
      "end_date": "YYYY-MM-DD"
    }
    ```

- **Response**:
    ```json
    {
      "booking": {
        "id": "integer",
        "customer_name": "string",
        "customer_contact": "string",
        "start_date": "YYYY-MM-DD",
        "end_date": "YYYY-MM-DD",
        "book": {
          "id": "integer",
          "title": "string"
        }
      }
    }
    ```

### 2. GET /api/books/{book_id}/booking - Get all bookings for a specific book with pagination

- **Authorization Required**: Yes

- **Path Parameter**:
    - `book_id` - ID of the book

- **Query Parameters**:
    - `page` - Page number (optional, default is 1)
    - `per_page` - Number of bookings per page (optional, default is 10)

- **Response**:

    ```json
    {
      "bookings": [
        {
          "id": "integer",
          "customer_name": "string",
          "customer_contact": "string",
          "start_date": "YYYY-MM-DD",
          "end_date": "YYYY-MM-DD",
          "book": {
            "id": "integer",
            "title": "string"
          }
        }
      ],
      "total": "integer",
      "page": "integer",
      "pages": "integer",
      "per_page": "integer"
    }
    ```
----

## Examples

### Register a New User
```bash
curl -X POST http://localhost:5000/api/auth/register -H "Content-Type: application/json" -d '{"username": "newuser", "email": "newuser@example.com", "password": "password123"}'
```


### Login and Get Token
```bash
curl -X POST http://localhost:5000/api/auth/login -H "Content-Type: application/json" -d '{"email": "newuser@example.com", "password": "password123"}'
```

### Create a Book (Authenticated)
```bash
curl -X POST http://localhost:5000/api/books/ -H "Authorization: Bearer <your_jwt_token>" -H "Content-Type: application/json" -d '{"title": "Sample Book", "description": "A great book", "author_id": 1, "isbn": "1234567890123", "pages": 200}'
```


### Get All Books (No Authentication)
```bash
curl -X GET http://localhost:5000/api/books/

```
----

## Setup and Running Locally

1. **Clone the repository.**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up environment variables (e.g., DATABASE_URL, SECRET_KEY) in a .env file.**
4. **Run migrations:**
    ```bash
    flask db upgrade
    ```
5. **Start the server:**

```bash
flask run
```

## Using Docker

You can also run the application using Docker. There are two ways to do this:

### Option 1: Using `flask run`

This requires setting up a local Python environment and using `flask run` as described above.

### Option 2: Using Docker Compose

1. Build and run the containers:

    ```bash
    docker-compose up --build
    ```

    Access the API at [http://localhost:5000](http://localhost:5000).

2. To stop the containers, use:

    ```bash
    docker-compose down
    ```

## API Documentation

You can access the Swagger API documentation at:

[http://localhost:5000/swagger](http://localhost:5000/swagger)



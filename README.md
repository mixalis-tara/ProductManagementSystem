# CRUD System API's

ProductManagementSystem is a Python application designed to manage a collection of products. It allows users to view a list of products, add new products, update product details, delete products, manage stock levels, and calculate product statistics.

## Features:

- **View Products**: Browse through a list of products in the collection.
- **View Product by name**: Browse a product by name in the collection.
- **Add New Products**: Easily add new products to the collection with details such as name, description, price, and quantity.
- **Update Product Details**: Update information about a specific product.
- **Delete Products**: Remove products from the collection.
- **Manage Stock**: Increase or decrease the stock levels of products.
- **Calculate Statistics**: Calculate statistics such as the total number of products, the average price, and total quantity of products.

## Technologies Used:

- **Python**: Programming language used for building the application.
- **FastAPI**: Web framework for building APIs.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **PostgreSQL**: Database system for storing product information.
- **psycopg2**: PostgreSQL database adapter for Python.
- **SQL**: Query language for interacting with the database.

## How to Run:

1. **Clone the repository to your local machine**:
    ```sh
    git clone https://github.com/yourusername/ProductManagementSystem.git
    ```

2. **Navigate to the project directory**:
    ```sh
    cd ProductManagementSystem
    ```

3. **Set up a virtual environment and activate it**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Set up the PostgreSQL database**:
    - Ensure you have PostgreSQL installed and running.
    - Create a database named `productdb`:
      ```sql
      CREATE DATABASE productsdb;
      ```

6. **Create the database schema and insert sample data**:
    - Run the provided SQL script `setup.sql`:
      ```sh
      psql -U postgres -d productsdb -f setup.sql
      ```

7. **Run the FastAPI application**:
    ```sh
    uvicorn main:app --reload
    ```

8. **Interact with the API**:
    - Open your browser and navigate to `http://localhost:8000/docs` to access the interactive API documentation.
    - Use the endpoints to manage products, update stock, and calculate statistics.

## File Structure:

- `main.py`: The main Python script to run the FastAPI application.
- `domain/product.py`: Contains the Pydantic models and data schemas.
- `repositories/`: Contains repository classes for database interactions.
  - `databaseConnection.py`: Handles the database connection.
  - `product_repository.py`: Defines methods for CRUD operations on products.
- `services/`: Contains service classes for business logic.
  - `product_service.py`: Defines methods for managing products, stock, and statistics.
  - `mapper.py`: Contains functions for mapping database results to domain objects.
- `controllers/`: Contains FastAPI route handlers.
  - `product_controller.py`: Defines the API endpoints for product management.
- `setup.sql`: SQL script to create the database schema and insert sample data.

## Example Usage:

1. **View Products**: GET `/all`
   - Retrieve a list of all products in the collection.
   
2. **View Products by name**: GET `/specific/{name}`
   - Retrieve a product by name in the collection.

3. **Add New Product**: POST `/create`
   - Add a new product to the collection with JSON payload:
     ```json
     {
       "name": "iPhone 14",
       "description": "Latest model of iPhone",
       "price": 999.99,
       "quantity": 50
     }
     ```

4. **Update Product**: PUT `/update/{name}`
   - Update the details of an existing product with JSON payload.

5. **Delete Product**: DELETE `/delete/{name}`
   - Remove a product from the collection.

6. **Manage Stock**: PUT `/manage_stock/{name}`
   - Increase or decrease the stock of a product with JSON payload:
     ```json
     {
       "action": "increase",
       "quantity": 50
     }
     ```

7. **Product Statistics**: GET `/product_statistics`
   - Retrieve statistics such as the total number of products, average price, and total quantity.

## Additional Information:

- Ensure PostgreSQL is running and accessible.
- Update database connection details in `database.py` if necessary.
- Follow best practices for security and error handling when deploying the application.

Feel free to customize and extend this application as needed for your specific use case.

-- Create the products table
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    price NUMERIC(10, 2) NOT NULL,
    quantity INT NOT NULL
);

-- Insert sample data into the products table
INSERT INTO products (name, description, price, quantity) VALUES
('iPhone 14', 'smartphone', 999.99, 50),
('Samsung Galaxy S21', 'smartphone', 899.99, 30),
('Google Pixel 6', 'smartphone', 799.99, 20),
('OnePlus 9', 'smartphone', 699.99, 15),
('Sony Xperia 5 ', 'smartphone', 799.99, 25);

-- Verify the data
SELECT * FROM products;
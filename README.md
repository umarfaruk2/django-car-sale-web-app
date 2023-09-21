# Car Sales Website

This is a fully functional car sales website that allows users to list cars for sale and facilitates car orders. It includes features for both users and administrators, providing a seamless experience for buying and selling cars.

## User-Facing Features:

### 1. Car Listings

- Users can create car listing.
- Car listings are displayed in an organized and appealing manner for easy browsing.

### 2. User Registration and Authentication

- Implement a user registration and login system to ensure secure access.
- Users can create accounts, log in, and maintain their profiles.

### 3. Placing Orders

- Users can place orders for the cars they want to buy.
- Orders have a default status of "Pending" upon submission.

### 4. Order History

- Users have access to view their order history.
- Users can see the status of their orders and track their purchasing history.

### 5. User Review

- Users can provide reviews and ratings for the products they have ordered.
- This feature allows for feedback and ratings on the purchased cars.

## Admin-Facing Features:

### 1. Admin Dashboard

- A separate dashboard is provided for administrators to manage cars and orders.
- Access to the admin dashboard is restricted to users with admin privileges (e.g., "is_staff" flag).

### 2. Order Management

- Admins can view and manage all orders placed by users.
- The admin has the ability to change the status of orders, such as updating from "Pending" to "Deliver."

## Technologies Used:

- Backend: Python (Django Framework)
- Frontend: HTML, Tailwind CSS
- Database: SQLite (Can be upgraded to other databases for production)
- Authentication: Django Authentication System
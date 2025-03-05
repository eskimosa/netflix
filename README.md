Intro
--

This Netflix clone is built using Django REST Framework on the backend and React.js on the frontend, fetching data from a third-party API and storing each category in a dedicated PostgreSQL database, ensuring efficient data management.

User authentication is managed with Django and JWT for secure login and session handling.
On the frontend, a custom AuthProvider and useAuth() hook handle session management, storing the JWT securely and dynamically updating the app’s state to protect routes and maintain user sessions.

The entire project is fully Dockerized, simplifying deployment and scaling for production environments.

Installation
--

1. Clone the repository:
```shall
git clone https://github.com/eskimosa/netflix.git
cd netflix
```
2. Install dependencies and start the application:
```shall
docker-compose -f docker-compose.yml up -d --build
```
3. Access the application: Navigate to http://localhost:3000 in your web browser.

Author
--

[eskimosa](https://github.com/eskimosa/)

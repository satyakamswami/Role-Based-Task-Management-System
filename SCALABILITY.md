# Scalability & Security Notes

## Scalability
If this application were to scale to handle thousands of concurrent users, the following architectural changes would be implemented:
1. **Load Balancing:** Deploy FastAPI across multiple servers behind a load balancer (like Nginx or AWS ALB) using Gunicorn with Uvicorn workers.
2. **Managed Database:** Migrate from a self-hosted PostgreSQL instance to a managed solution like Amazon RDS or Aurora for automated backups, read-replicas, and high availability.
3. **Caching Layer:** Introduce Redis to cache frequent read operations (like user tasks) to reduce database load.

## Security
1. **Password Hashing:** Passwords are never stored in plain text. They are hashed using `bcrypt` before database insertion.
2. **JWT Authentication:** Stateful sessions are avoided. We use stateless JSON Web Tokens for secure authorization across API endpoints.
3. **Input Validation:** FastAPI and Pydantic automatically sanitize and validate incoming request payloads, rejecting bad data with HTTP 422 Unprocessable Entity errors.

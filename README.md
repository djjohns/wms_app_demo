# wms_app

This is a demo app to showcase a [Docker](https://www.docker.com/) containerized
[Django](https://www.djangoproject.com/) webapp. That uses
[Python](https://www.python.org/), [Postgres](https://www.postgresql.org/),
[bootstrap5](https://getbootstrap.com/), and
[particlesjs](https://vincentgarreau.com/particles.js/) for the front and
backend. Along with offering an API using the
[django rest framework](https://www.django-rest-framework.org/).
All to render some forms to an authenticated user to do some basic CRUD
operations.

This is a constant work in progress, and will be added to and remixed with other
tech stacks that I wish to explore.

# To replicate this Dockerized Repo:

- Clone the repository:
  ```
  git clone https://github.com/djjohns/wms_app_demo.git
  ```
- Create the .env file in the app directory.
  ```
  touch app/.env
  ```
- Create you secrets in the **app/.env** file.

  ```
  DJANGO_SECRET_KEY='YourSecretsHere'
  DJANGO_DEBUG=True
  # postgres://{user}:{password}@{hostname}:{port}/{database-name}
  DATABASE_URL='postgres://postgres:postgres@db:5432/postgres'
  SOCIAL_AUTH_AZUREAD_OAUTH2_KEY= "YourSecretsHere",
  SOCIAL_AUTH_AZUREAD_OAUTH2_SECRET= "YourSecretsHere",
  SOCIAL_AUTH_GITHUB_KEY="YourSecretsHere",
  SOCIAL_AUTH_GITHUB_SECRET="YourSecretsHere",
  EMAIL_HOST_KEY="YourSecretsHere",
  EMAIL_HOST_SECRET="YourSecretsHere"
  ```

* Build and initialize the docker container instance:
  ```
  docker-compose up --build
  ```
* With a running docker container, you can open another shell in the same working
  directory and run the command **docker ps** as shown below to get the container
  id:

  ```
  docker ps
  ```

      We can then use the **docker exec** command to run ad hoc commands needed for
      django such as:

      ```
      docker exec -it container_id python manage.py makemigrations
      ```

      ```
      docker exec -it container_id python manage.py migrate
      ```

      ```
      docker exec -it container_id python manage.py collectstatic
      ```

      ```
      docker exec -it container_id python manage.py createsuperuser
      ```

---

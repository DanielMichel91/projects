# Ecommerce Shop Project

This project is an ecommerce shop built by Dennis Ivy. You can find the tutorial playlist [here](https://www.youtube.com/playlist?list=PL-51WBLyFTg0omnamUjL1TCVov7yDTRng).

## Usage

To use this project, you need to have Docker installed. If you haven't installed Docker yet, you can do so by running:

```
pip install docker
```

Once Docker is installed, navigate to the project folder where the `Dockerfile` file is located. Than you have to build the Docker image with the following command:

```
docker build -t #name of the image# .
```

To run the server on your local machine, use the following command:

```
docker run -p 8000:8000 #name of the image#
```

To add products to the shop, you have the option to create an admin user. To create a superuser, run the following command:

```
docker exec -it container_id python manage.py createsuperuser
```

Follow the prompts to set up your credentials. Once you've created the superuser, you can log in to the admin interface via your localhost. The admin interface can be accessed at `http://127.0.0.1:8000/admin`. From there, you can manage and add products through the GUI.

---

Feel free to customize further or add additional information as needed.
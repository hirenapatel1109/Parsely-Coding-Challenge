# Use the Python3.8.12 image
FROM python:3.8.12

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

EXPOSE 5000 

# Install the dependencies
RUN pip install -r requirements.txt

ENV FLASK_APP codetest.py

# run the command to start flask server
# CMD ["python", "-m", "flask", "run"]
CMD ["python", "codetest.py"]

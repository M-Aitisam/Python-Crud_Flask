


# Python Flask Crud Application Deployment with Jenkins and Docker

This project demonstrates  that how to deploy a full· fleg working  Python Flask Crud ( nurse/patient application) using Jenkins and Docker. 
Also  In  this code you  add the patient or update the patient and view the patient it can  also  add the data intp  Database (Sql Server). Same as add the nurse or update the nurse and view the nurse it can  also  add the data into Database (Sql Server).
The Flask Crud Application is containerized using Docker and  all  the Deployment is managed using  Jenkins pipeline.


```
Also  Change the Db mane  which  database you  are using means MySql  ServerServer   etc. if you can  use Sql Server Authentication option
Example :

# SQL Server configuration
server = 'localhost'
database = 'Python_Flask_Crud_db'
username = 'you db name'
password = 'your db password '

app.config['SQL_SERVER'] = {
    'driver': '{ODBC Driver 17 for SQL Server}',
    'server': server,
    'database': database,
    'username': username,
    'password': password
}


```
## Installation Step:

- Install  the Docker Desktop to the official  website. https://www.docker.com/products/docker-desktop/
- Installed  the Jenkins  to  thew official  website  and  then  setup  your plugin and then  working on  it.

  ###In Code:
- Flask library installed
- Add the pyodbc (this library  is use to  connect Sql  Server)
- flask-cors library  installed

## My Application Project Structure:

|___ Dockerfile
├___Jenkinsfile
├___App.py
├___requirements.txt
|__ Sql File
|___ Index.html


```

### Files Description

1. **Dockerfile**
   - Defines a Docker image that uses the FROM python:latest base
   - Installs Python 3 and Flask.
   - Copies the application code (`/app.py`) into the Docker image.
   - Runs the Flask application on port `5000`.
   - Pytohn App.py check the code.
 
2. **Jenkinsfile**
  This Jenkins File s the CI/CD process for building, pushing, and deploying the Dockerized Flask application.
   - A declarative Jenkins pipeline that defines four stages:
     - **Code**: Clones the code from a GitHub repository to  ensure the latest code is used to build process.
     - **Build**: Builds a Docker image for the Flask Crud Application in  the Docker File.
     - **Push to Docker Hub**: Jenkins Tags the Docker Image and pushes the Docker Hub.
     - **Deploy**:It  Deploys the Docker container to run the Flask Crud Appication using  port 5000. http://localhost:5000.

3. **App.py**
   Using Api  All the Data  get Insert Update View  Delete Rest Api created in this file.  
Example:
@app.route('/patient', methods=['POST'])
def submit_patient():
    data = request.json
    id = data.get('id')
    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')
    nurse_id = data.get('nurse_id')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO patient (id, name, age, gender, nurse_id) VALUES (?, ?, ?, ?, ?)", (id, name, age, gender, nurse_id))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Patient added successfully"}), 201


4. **requirements.txt**
   - Contain all  the dependency  use in  App.py 
pyodbc
flask-cors
Flask


## Getting Started

### 1. Build and Run Locally

You can build and run the Flask app locally using Docker:

```bash
# Build Docker image
docker build -t flask-pyodbc-app .

# Run the container
docker run -p 5000:5000 flask-pyodbc-app

```

Access the web application at: `http://localhost:5000`

### 2. Jenkins Pipeline Setup

1. **Code Stage**: Jenkins willutomatically  fetch/clone the code from a GitHub repository.

2. **Build Stage**: Jenkins will  start building a Docker Image from Dockerfile. The Dockerfile contain all the steyto prepare  application to run  inside my  Docker Container.

3. **Push to Docker Hub Stage**: Jenkins  Push the Built Image in  Docker Hub repository . The Docker Hub is a place  where my  Docker Images can  be stroed and shared. You  can need credential (username and password ) in Jenkins.

4. **Deploy Stage**: Jenkins will run the Docker container  and  expose tne container port 5000.

### Jenkins Configuration

Make sure to configure the following in Jenkins:

- **GitHub repository**: IN Jenkins Pipeline  make sure to  replace the Git url in the Jenkinsfile with your own Github repository if necessary.

## Flask Allication 

The Flask  Crud Application  has the following routes:
@app.route('/')
@app.route('/nurse', methods=['POST'])
@app.route('/nurses', methods=['GET'])
@app.route('/nurse/<int:id>', methods=['PUT']
@app.route('/nurse/<int:id>', methods=['DELETE'])

@app.route('/patient', methods=['POST'])
@app.route('/patients', methods=['GET'])
@app.route('/patient/<int:id>', methods=['PUT'])
@app.route('/patient/<int:id>', methods=['DELETE'])

## Docker Hub

Once the image is built, it is pushed to Docker Hub with the tag `flask-pyodbc-app:latest`.

You can pull and run the image from Docker Hub as follows:

```
#### Bash Run  Commands:
docker pull <dockerHubUser>/flask-pyodbc-app:latest

docker run -d -p 5000:5000 <dockerHubUser>/flask-pyodbc-app:latest


##Last Update the Image:
docker build -t <dockerHubUser>/flask-pyodbc-app:latest .
docker push <dockerHubUser>/flask-pyodbc-app:latest


```

# Bishop
A Metadata API built using Python 3, FastAPI and backed by S3

# Why
Bishop is a fit for situations where you want to store quick bits of facts without
setting up in an entire database for it. Services like lambdas or cron jobs are a good
fit since they normaly do not maintain state between runs or client app that
just need to know quick facts about a user or customer.

Below are some examples of the kinds of data you would use Bishop for.

   - User preferences or facts ( should be emailed, has profile picture)
   - Have we already emailed this account ?
   - Did we already process this file ?
   - How many times has an action/process occured

## Quick Start

To get this project up and running locally on your computer:
1. Set up a [Python development environment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment). This project uses pipenv

2. Change `sample.env` to `.env` and add your S3 credentials

3. Assuming you have Python setup, run the following commands:
   ```
   pipenv install
   cd app
   uvicorn main:app --reload

   # Running the tests
   pipenv install --dev
   pytest
   ```

4. Build and run the via docker
   ```
   docker build -t bishop_image .
   docker run --name bishop_container -p 80:80 bishop_image

   # Go to http://localhost/
   ```

5. API docs can be found here http://127.0.0.1:8000/redoc basic features are CRUD actions like
   - Create or update metadata given an existing key
   - Retrieve metadata payload given a specific key
   - Delete metadata given a specific key

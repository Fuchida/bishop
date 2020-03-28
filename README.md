# Bishop
A Metadata API built using Python 3 and FastAPI

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

## API Overview
   ```
   GET: Get information about and existing key
       <url>/<collection_name>/key/<key_id>
           {
               'created':<utc-datetime>
               'last_updated':<utc-datetime>
               'payload':{
                   <your-data-payload>
               }
           }

   PUT: Create a new or replace existing metadata for key
       <url>/<collection_name>/key/<key_id>
           {
               <your-data-payload>
           }
   ```

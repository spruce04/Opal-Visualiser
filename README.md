# Opal-Visualiser

Opal Visualiser uses open-source data provided by Transport For New South Wales to visualise public transport usage across New South Wales. 

Please note that this is currently an active **work in progress**, and the readme will be updated as the project progresses. 
When complete, the project will feature an interactive map, showing tap on and tap off volumes at stations around NSW, with customisable date filtering.

## Current Functionalities

### Backend
* Follow steps in ```schema.sql``` to set up the postgresql database
* Create a ```.env``` file in ```backend```, with variable ```DATABASE_URL=X```
  * Example - ```DATABASE_URL=postgresql://{username}:{password}@localhost:5432/opal```
* Start the FastAPI server by entering ```uvicorn main:app --reload``` in the ```backend``` folder
* Going to the url outputted in the terminal, total and net data of taps can be accessed through the urls ```http://127.0.0.1:8000/nettaps``` and ```http://127.0.0.1:8000/totaltaps``` (front end is a work in progress).

### Frontend (Work in Progress)
* Ensure the backend server is running first
* Navigate to the ```frontend``` folder and install dependencies by entering ```npm install```
* Start the development server by entering ```npm run dev```
* Open ```http://localhost:3000``` in your browser to view the interactive map (the current map is not the final version).

## 🛠️ Planned Final Stack
* **Frontend:** Next.js (React) + TypeScript + Tailwind CSS
* **Backend:** FastAPI (Python)
* **Database:** PostgreSQL
# Opal-Visualiser

Opal Visualiser uses open-source tap-on/tap-off data provided by Transport For New South Wales, and visualises this data on an interactive leaflet-based map.


## Current Functionalities

### Backend
* Follow steps in ```schema.sql``` to set up the postgresql database
* Create a ```.env``` file in ```backend```, with variable ```DATABASE_URL=X```
  * Example - ```DATABASE_URL=postgresql://{username}:{password}@localhost:5432/opal```
* Start the FastAPI server by entering ```uvicorn main:app --reload``` in the ```backend``` folder
* Going to the url outputted in the terminal, total and net data of taps can be accessed through the urls ```http://127.0.0.1:8000/net_taps``` and ```http://127.0.0.1:8000/total_taps``` (front end is a work in progress).

### Frontend
* Ensure the backend server is running first
* Navigate to the ```frontend``` folder and install dependencies by entering ```npm install```
* Start the development server by entering ```npm run dev```
* Open ```http://localhost:3000``` in your browser to view the interactive map
* Use the date selection component to select the range of months from which to draw data, and the toggle mode component to switch between total and net tap mode

## 🛠️ Final Stack
* **Frontend:** React (vite) + TypeScript
* **Backend:** FastAPI (Python)
* **Database:** PostgreSQL
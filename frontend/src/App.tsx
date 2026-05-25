import { CircleMarker, MapContainer, TileLayer, Tooltip } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import { useEffect, useState } from "react";
import ToggleMode from "./components/ToggleMode";

interface Station {
  station_name: string,
  station_type: string,
  total_taps: number,
  lat: number,
  lon: number
}

export default function App() {
  const [stations, set_stations] = useState<Station[]>([]);
  const [display, set_display] = useState<string>("total_taps"); //track if we want total or net taps

  useEffect(() => {
    //make a request to the API (returns a promise)
    fetch("http://127.0.0.1:8000/"+display)
    //parse the response as JSON
    .then((res) => res.json())
    //Store the data (an array of stations) in state
    .then((data: Station[]) => set_stations(data));
  }, [display]);

  //Mathematical formula to normalise the radius of the circles - we need to take the absolute value for net taps
  const max_taps = Math.max(...stations.map((s) => Math.abs(s[display])));
  const min_taps = Math.min(...stations.map((s) => Math.abs(s[display])));
  const normalise = (value: number) => {
    const r_min = 4;
    const r_max = 50;
    return r_min + ((value - min_taps) / (max_taps - min_taps)) * (r_max - r_min);
  }

  //A map to return the correct colour based on a station type
  const colours = new Map<string, string>();
  colours.set("Train", "#F6891F");
  colours.set("Metro", "#168388");
  colours.set("Light rail", "#EE343F");
  colours.set("Metro Shared", "yellow");


  //leaflate boilerplate
  //we need to wrap in a div to force it to take up the whole screen
  return (
    <div style={{ width: "100%", height: "100vh", position: "relative" }}>
      <MapContainer
        center={[-33.87, 150.90]}
        zoom={11}
        style={{ width: "100%", height: "100%" }}
      >
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; OpenStreetMap contributors'
        />
        
        {stations.map((station) => (
          <CircleMarker className="circle" key={station.station_name} center={[station.lat, station.lon]} radius={normalise(Math.abs(station[display]))} color={colours.get(station.station_type)}>
            <Tooltip>
            <div>Name: {station.station_name}</div>
            <div>{display}: {station[display]}</div>
            <div>Station Type: {station.station_type}</div>
            </Tooltip>
          </CircleMarker>
        ))}
      </MapContainer>
      <ToggleMode on_toggle={set_display} active_mode={display}></ToggleMode>
    </div>
  );
}
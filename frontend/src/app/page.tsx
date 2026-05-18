//Imports / client side rendering
"use client";
import { useEffect, useState } from "react";
import { MapContainer, TileLayer, CircleMarker, Tooltip } from "react-leaflet";
import "leaflet/dist/leaflet.css";

//Type to define station returned by API
type Station = {
  station_name: string;
  station_type: string;
  total_taps: number;
  lat: number;
  lon: number;
};

//?
export default function Home() {
  //Store stations set by backend, dates for filtering
  const [stations, setStations] = useState<Station[]>([]);
  const [start, setStart] = useState("2026-04-01");
  const [end, setEnd] = useState("2026-04-01");

  //Get the data from the backend, with dynamic date setting enabled for future functionality
  useEffect(() => {
    fetch(`http://127.0.0.1:8000/totaltaps?start=${start}&end=${end}`)
      .then((res) => res.json())
      .then((json) => setStations(json));
  }, [start, end]);

  //Render the map, with a circle marker for each station
  return (
    <div style={{ position: "relative", height: "100vh", width: "100%" }}>
      <MapContainer
        center={[-33.8688, 151.2093]}
        zoom={11}
        style={{ height: "100vh", width: "100%" }}
      >
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        {stations.map((station) => (
          <CircleMarker
            key={station.station_name}
            center={[station.lat, station.lon]}
            radius={Math.sqrt(station.total_taps / 1000)}
            color="blue"
            fillOpacity={0.6}
          >
            <Tooltip>{station.station_name}: {station.total_taps.toLocaleString()} total taps</Tooltip>
          </CircleMarker>
        ))}
      </MapContainer>
    </div>
  );
}
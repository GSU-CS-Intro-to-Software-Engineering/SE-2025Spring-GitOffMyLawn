import React, { useEffect, useRef } from "react";

const MapCanvas = () => {
  const mapRef = useRef(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/map/initialize")
      .then((response) => response.json())
      .then((data) => {
        mapRef.current.innerHTML = data.map_html;
      })
      .catch((error) => console.error("Error initializing map:", error));
  }, []);

  return <div ref={mapRef} style={{ height: "100%", width: "100%" }} />;
};

export default MapCanvas;

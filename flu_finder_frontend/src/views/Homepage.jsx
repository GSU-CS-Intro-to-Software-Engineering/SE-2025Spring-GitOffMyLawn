import React, { useEffect, useState } from "react";
import { Typography } from "@mui/material";
import MapCanvas from "../components/MapCanvas";
import MainCanvas from "../components/MainCanvas";

const Homepage = () => {
  const [status, setStatus] = useState("Fetching data...");
  const backendUrl = import.meta.env.VITE_BACKEND_URL;

  useEffect(() => {
    fetch(`${backendUrl}/api/cdc/data`)
      .then((response) => response.json())
      .then((data) => setStatus(data.status))
      .catch((error) => console.error("Error fetching data:", error));
  }, [backendUrl]);

  return (
    <div
      style={{
        marginTop: "60px",
        marginLeft: "270px",
        padding: "40px",
        width: "calc(100% - 270px)",
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-between",
        height: "calc(100vh - 60px)"
      }}
    >
      <MainCanvas />
    </div>
  );
};

export default Homepage;

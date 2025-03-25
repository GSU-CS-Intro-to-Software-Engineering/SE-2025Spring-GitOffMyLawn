import React, { useEffect, useState } from "react";
import { Typography } from "@mui/material";
import { useEnv } from "vite-plugin-env-compatible";


const Homepage = () => {
  const [status, setStatus] = useState("Fetching data...");
  const backendUrl = useEnv("VITE_BACKEND_URL");

  useEffect(() => {
    fetch(`${backendUrl}/api/cdc/data`)
      .then((response) => response.json())
      .then((data) => setStatus(data.status))
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  return (
    <div
      style={{
        marginTop: "60px",
        marginLeft: "270px",
        padding: "40px",
        width: "calc(100% - 270px)",
      }}
    >
      <Typography variant="h4" fontWeight="bold">
        Flu Finder Frontend
      </Typography>
      <Typography variant="body1">Backend Response: {status}</Typography>
    </div>
  );
};

export default Homepage;

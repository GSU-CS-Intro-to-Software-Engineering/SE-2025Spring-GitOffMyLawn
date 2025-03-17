import React, { useEffect, useState } from "react";
import { Typography } from "@mui/material";

const Homepage = () => {
  const [status, setStatus] = useState("Fetching data...");

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/cdc/data")
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

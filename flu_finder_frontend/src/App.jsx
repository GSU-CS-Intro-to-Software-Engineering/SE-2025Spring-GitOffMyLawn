import { useEffect, useState } from "react";

function App() {
  const [status, setStatus] = useState("Fetching data...");

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/fetch-data") // Call your Flask API
      .then((response) => response.json()) // Convert response to JSON
      .then((data) => setStatus(data.status)) // Update state with API response
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  return (
    <div>
      <h1>Flu Finder Frontend</h1>
      <p>Backend Response: {status}</p>
    </div>
  );
}

export default App;

import React from "react";

const LatestInfections = () => {
  return (
    <div style={{ padding: "10px", overflowY: "auto" }}>
      <h2>Latest Infections</h2>
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Location</th>
            <th># Infected</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>12/31/2024</td>
            <td>Ottawa, Michigan</td>
            <td>23400</td>
          </tr>
          <tr>
            <td>12/30/2024</td>
            <td>Johnson, Nebraska</td>
            <td>20910</td>
          </tr>
          <tr>
            <td>12/30/2024</td>
            <td>Twinfalls, Idaho</td>
            <td>30</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default LatestInfections;

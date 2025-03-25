// src/components/Sidebar.jsx
import React from "react";
import {
  Box,
  List,
  ListItem,
  ListItemText,
  ListItemIcon,
  Switch,
} from "@mui/material";
import HomeIcon from "@mui/icons-material/Home";
import MapIcon from "@mui/icons-material/Room";
import BarChartIcon from "@mui/icons-material/BarChart";
import palette from "../theme/palette";

const Sidebar = () => {
  return (
    <Box
      sx={{
        width: "250px",
        height: "calc(100vh - 60px)",
        backgroundColor: palette.sidebar,
        color: palette.textPrimary,
        padding: "20px",
        position: "fixed",
        top: "60px", // Starts below the navbar
        left: 0,
      }}
    >
      <h2>Quick Access</h2>
      <List>
        <ListItem button>
          <ListItemIcon>
            <HomeIcon sx={{ color: palette.textPrimary }} />
          </ListItemIcon>
          <ListItemText primary="Dashboard" />
        </ListItem>
        <ListItem button>
          <ListItemIcon>
            <MapIcon sx={{ color: palette.textPrimary }} />
          </ListItemIcon>
          <ListItemText primary="Interactive Map" />
        </ListItem>
        <ListItem>
          <ListItemText primary="Wild Birds" />
          <Switch defaultChecked color="primary" />
        </ListItem>
        <ListItem>
          <ListItemText primary="Domestic Poultry" />
          <Switch defaultChecked color="primary" />
        </ListItem>
        <ListItem>
          <ListItemText primary="Dairy Cows" />
          <Switch defaultChecked color="primary" />
        </ListItem>
        <ListItem>
          <ListItemText primary="Humans" />
          <Switch defaultChecked color="primary" />
        </ListItem>
        <ListItem button>
          <ListItemIcon>
            <BarChartIcon sx={{ color: palette.textPrimary }} />
          </ListItemIcon>
          <ListItemText primary="Charts" />
        </ListItem>
      </List>
    </Box>
  );
};

export default Sidebar;

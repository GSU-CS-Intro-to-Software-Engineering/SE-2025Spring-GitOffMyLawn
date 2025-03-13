import React from "react";
import { Box, InputBase, Typography } from "@mui/material";
import palette from "../theme/palette";

const Navbar = () => {
  return (
    <Box
      sx={{
        height: "60px",
        backgroundColor: palette.primary,
        display: "flex",
        alignItems: "center",
        padding: "0 20px",
        width: "100%",
        position: "fixed",
        top: 0,
        left: 0,
        zIndex: 1000,
      }}
    >
      <Typography
        variant="h6"
        sx={{
          color: palette.textPrimary,
          fontWeight: "bold",
          marginRight: "20px",
        }}
      >
        FLUVIEW
      </Typography>
      <InputBase
        placeholder="Type Any Location"
        sx={{
          backgroundColor: "white",
          borderRadius: "20px",
          padding: "5px 10px",
          width: "250px",
          marginLeft: "20%",
          marginRight: "20px",
        }}
      />
    </Box>
  );
};

export default Navbar;

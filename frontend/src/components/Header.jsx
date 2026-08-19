import {
  AppBar,
  Toolbar,
  Typography,
  Box,
  Avatar,
} from "@mui/material";

import ShieldOutlinedIcon from "@mui/icons-material/ShieldOutlined";

function Header() {
  return (
    <AppBar
      position="static"
      elevation={1}
      sx={{
        background: "#ffffff",
        color: "#111827",
      }}
    >
      <Toolbar sx={{ py: 1 }}>

        <ShieldOutlinedIcon
          sx={{
            fontSize: 42,
            color: "#2563eb",
            mr: 2,
          }}
        />

        <Box sx={{ flexGrow: 1 }}>

          <Typography
            variant="h5"
            sx={{
              fontWeight: 700,
            }}
          >
            AI Configuration Validator
          </Typography>

          <Typography
            variant="body2"
            color="text.secondary"
          >
            Secure Infrastructure Validation using AI
          </Typography>

        </Box>

        <Avatar sx={{ bgcolor: "#2563eb" }}>
          J
        </Avatar>

      </Toolbar>
    </AppBar>
  );
}

export default Header;
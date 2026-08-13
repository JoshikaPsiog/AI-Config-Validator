import { useState } from "react";

import {
  Card,
  CardContent,
  Typography,
  TextField,
  Button,
  Stack,
} from "@mui/material";

import GitHubIcon from "@mui/icons-material/GitHub";

import { scanRepository } from "../services/api";

function RepositoryCard({ setResult }) {

  const [repoUrl, setRepoUrl] = useState("");
  const [loading, setLoading] = useState(false);

  const handleScan = async () => {

    if (!repoUrl) {
      alert("Enter a GitHub repository URL");
      return;
    }

    try {

      setLoading(true);

      const response = await scanRepository(repoUrl);

      setResult(response.data);

    } catch (err) {

      console.error(err);

      if (err.response) {
        alert(JSON.stringify(err.response.data));
      }

    } finally {

      setLoading(false);

    }

  };

  return (

    <Card elevation={3} sx={{ borderRadius: 4 }}>

      <CardContent sx={{ p: 4 }}>

        <Typography variant="h5" fontWeight="bold">

          GitHub Repository Scanner

        </Typography>

        <Typography
          color="text.secondary"
          sx={{ mb: 3 }}
        >

          Scan a GitHub repository containing Terraform or Azure Bicep files.

        </Typography>

        <Stack spacing={3}>

          <TextField
            fullWidth
            label="Repository URL"
            value={repoUrl}
            onChange={(e) =>
              setRepoUrl(e.target.value)
            }
          />

          <Button
            variant="contained"
            startIcon={<GitHubIcon />}
            onClick={handleScan}
            disabled={loading}
          >

            {loading
              ? "Scanning..."
              : "Scan Repository"}

          </Button>

        </Stack>

      </CardContent>

    </Card>

  );

}

export default RepositoryCard;
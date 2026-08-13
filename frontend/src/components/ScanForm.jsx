import { useState } from "react";
import {
  Card,
  CardContent,
  Typography,
  Button,
  Stack,
  Chip,
  LinearProgress,
} from "@mui/material";

import CloudUploadIcon from "@mui/icons-material/CloudUpload";
import CheckCircleIcon from "@mui/icons-material/CheckCircle";

import { uploadFile, validateFiles } from "../services/api";

function ScanForm({ setResult }) {
  const [selectedFile, setSelectedFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!selectedFile) {
      alert("Please choose a Terraform or Bicep file.");
      return;
    }

    try {
      setLoading(true);

      const formData = new FormData();
      formData.append("file", selectedFile);

      await uploadFile(formData);

      const response = await validateFiles();

      setResult(response.data);
    } catch (err) {
      console.error(err);

      if (err.response) {
        alert(JSON.stringify(err.response.data));
      } else {
        alert("Backend not running.");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <Card
      elevation={3}
      sx={{
        borderRadius: 4,
        mb: 4,
      }}
    >
      <CardContent sx={{ p: 4 }}>

        <Typography variant="h5" fontWeight="bold">
          Upload Infrastructure File
        </Typography>

        <Typography
          color="text.secondary"
          sx={{ mt: 1, mb: 3 }}
        >
          Upload a Terraform (.tf) or Azure Bicep (.bicep) file for AI-powered
          security validation.
        </Typography>

        {loading && (
          <LinearProgress sx={{ mb: 3 }} />
        )}

        <Stack
          direction={{ xs: "column", md: "row" }}
          spacing={2}
          alignItems="center"
        >
          <Button
            variant="outlined"
            component="label"
            startIcon={<CloudUploadIcon />}
          >
            Choose File

            <input
              hidden
              type="file"
              accept=".tf,.bicep"
              onChange={(e) =>
                setSelectedFile(e.target.files[0])
              }
            />
          </Button>

          {selectedFile && (
            <Chip
              color="primary"
              icon={<CheckCircleIcon />}
              label={selectedFile.name}
            />
          )}

          <Button
            variant="contained"
            size="large"
            onClick={handleUpload}
            disabled={loading}
            sx={{
              ml: { md: "auto" },
            }}
          >
            {loading
              ? "Validating..."
              : "Upload & Validate"}
          </Button>

        </Stack>

      </CardContent>
    </Card>
  );
}

export default ScanForm;
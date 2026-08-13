import { useState } from "react";

import {
  Container,
  Box,
  Typography,
  Tabs,
  Tab,
} from "@mui/material";

import Header from "../components/Header";
import ScanForm from "../components/ScanForm";
import RepositoryCard from "../components/RepositoryCard";
import SummaryCards from "../components/SummaryCards";
import ResultCard from "../components/ResultCard";

function Dashboard() {
  const [result, setResult] = useState(null);
  const [tab, setTab] = useState(0);

  return (
    <>
      <Header />

      <Container maxWidth="lg" sx={{ mt: 4, mb: 6 }}>

        <Tabs
          value={tab}
          onChange={(e, newValue) => {
            setTab(newValue);
            setResult(null);
          }}
          sx={{ mb: 4 }}
        >
          <Tab label="Upload File" />
          <Tab label="GitHub Repository" />
        </Tabs>

        {tab === 0 && (
          <ScanForm setResult={setResult} />
        )}

        {tab === 1 && (
          <RepositoryCard setResult={setResult} />
        )}

        {result && (
          <>
            <SummaryCards result={result} />

            <Box mt={5}>
              <Typography
                variant="h5"
                fontWeight="bold"
                mb={3}
              >
                Validation Results
              </Typography>

              <ResultCard result={result} />
            </Box>
          </>
        )}

      </Container>
    </>
  );
}

export default Dashboard;
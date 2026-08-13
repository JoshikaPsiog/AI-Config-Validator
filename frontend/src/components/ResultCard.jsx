import {
  Card,
  CardContent,
  Typography,
  Chip,
  Stack,
  Accordion,
  AccordionSummary,
  AccordionDetails,
  Paper,
  Divider,
} from "@mui/material";

import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import DescriptionIcon from "@mui/icons-material/Description";
import SmartToyIcon from "@mui/icons-material/SmartToy";

function ResultCard({ result }) {
  if (!result) return null;

  const cleanOutput = (text) =>
    text ? text.replace(/\x1B\[[0-9;]*m/g, "") : "";

  return (
    <Stack spacing={3}>
      {result.results.map((item, index) => (
        <Card
          key={index}
          elevation={3}
          sx={{
            borderRadius: 3,
          }}
        >
          <CardContent>

            {/* Header */}

            <Stack
              direction="row"
              justifyContent="space-between"
              alignItems="center"
              mb={2}
            >

              <Stack direction="row" spacing={2} alignItems="center">

                <DescriptionIcon color="primary" />

                <div>
                  <Typography variant="h6" fontWeight="bold">
                    {item.file}
                  </Typography>

                  <Chip
                    label={item.type}
                    size="small"
                    color="info"
                    sx={{ mt: 1 }}
                  />
                </div>

              </Stack>

              <Chip
                label={item.status}
                color={item.status === "PASS" ? "success" : "error"}
                sx={{ fontWeight: "bold" }}
              />

            </Stack>

            <Divider sx={{ mb: 2 }} />

            {/* Validation Output */}

            <Typography
              variant="subtitle1"
              fontWeight="bold"
              gutterBottom
            >
              Validation Output
            </Typography>

            <Paper
              variant="outlined"
              sx={{
                p: 2,
                background: "#f8fafc",
                whiteSpace: "pre-wrap",
                fontFamily: "Consolas",
              }}
            >
              {cleanOutput(item.output)}
            </Paper>

            {/* AI Recommendation */}

            {item.ai_explanation && (

              <Accordion sx={{ mt: 3 }}>

                <AccordionSummary
                  expandIcon={<ExpandMoreIcon />}
                >
                  <Stack
                    direction="row"
                    spacing={1}
                    alignItems="center"
                  >

                    <SmartToyIcon color="primary" />

                    <Typography fontWeight="bold">
                      AI Recommendation ({item.ai_provider})
                    </Typography>

                  </Stack>
                </AccordionSummary>

                <AccordionDetails>

                  <Typography
                    sx={{
                      whiteSpace: "pre-wrap",
                      lineHeight: 1.8,
                    }}
                  >
                    {item.ai_explanation}
                  </Typography>

                </AccordionDetails>

              </Accordion>

            )}

          </CardContent>
        </Card>
      ))}
    </Stack>
  );
}

export default ResultCard;
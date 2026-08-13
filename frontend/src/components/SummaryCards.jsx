import {
  Grid,
  Card,
  CardContent,
  Typography,
} from "@mui/material";

import {
  FileText,
  CheckCircle,
  XCircle,
  ShieldAlert,
} from "lucide-react";

function SummaryCards({ result }) {

  if (!result) return null;

  const cards = [
    {
      title: "Total Files",
      value: result.total_files,
      icon: <FileText size={30} />,
      color: "#2563eb",
    },
    {
      title: "Passed",
      value: result.passed,
      icon: <CheckCircle size={30} />,
      color: "#16a34a",
    },
    {
      title: "Failed",
      value: result.failed,
      icon: <XCircle size={30} />,
      color: "#dc2626",
    },
    {
      title: "Status",
      value: result.overall_status,
      icon: <ShieldAlert size={30} />,
      color: "#f59e0b",
    },
  ];

  return (
    <Grid container spacing={3} mt={2}>

      {cards.map((card) => (

        <Grid item xs={12} md={3} key={card.title}>

          <Card
            sx={{
              borderRadius: 3,
              boxShadow: 3,
            }}
          >

            <CardContent>

              <div
                style={{
                  color: card.color,
                  marginBottom: 12,
                }}
              >
                {card.icon}
              </div>

              <Typography
                variant="h4"
                fontWeight="bold"
              >
                {card.value}
              </Typography>

              <Typography color="text.secondary">
                {card.title}
              </Typography>

            </CardContent>

          </Card>

        </Grid>

      ))}

    </Grid>
  );
}

export default SummaryCards;
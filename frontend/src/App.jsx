import { useState } from "react";
import axios from "axios";
import Header from "./components/Header";
import "./App.css";
import ScanForm from "./components/ScanForm";
import SummaryCards from "./components/SummaryCards";
import RepositoryCard from "./components/RepositoryCard";
import ResultCard from "./components/ResultCard";
function App() {
  const [repoUrl, setRepoUrl] = useState("");
  const [result, setResult] = useState(null);

  const scanRepository = async () => {
    try {
      const response = await axios.post(
  "http://127.0.0.1:8000/scan-repository",
  {
    repo_url: repoUrl,
  }
);

      setResult(response.data);

console.log(response.data);
    } catch (error) {
  console.log(error);

  if (error.response) {
    console.log(error.response.data);
    alert(JSON.stringify(error.response.data));
  } else {
    alert(error.message);
  }
}
  };

  return (<>
    <Header />

    <div className="container">

        <ScanForm
            repoUrl={repoUrl}
            setRepoUrl={setRepoUrl}
            scanRepository={scanRepository}
        />
<SummaryCards result={result} />
<RepositoryCard result={result} />
<ResultCard result={result} />
    </div>

</>
  );
}

export default App;
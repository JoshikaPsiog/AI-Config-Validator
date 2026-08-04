import { Search } from "lucide-react";
function ScanForm({
    repoUrl,
    setRepoUrl,
    scanRepository
}) {

    return (

        <div className="scan-form">

            <h2>Repository Scanner</h2>

            <p>
                Enter the GitHub Repository URL
            </p>

            <input
                type="text"
                placeholder="https://github.com/username/repository"
                value={repoUrl}
                onChange={(e)=>setRepoUrl(e.target.value)}
            />

            <button onClick={scanRepository}>
    <Search size={20} />
    Scan Repository
</button>

        </div>

    );

}

export default ScanForm;
import { FileCode, CheckCircle, XCircle } from "lucide-react";

function ResultCard({ result }) {

    if (!result) return null;

    return (

        <div className="results-section">

            <h2>Validation Results</h2>

            {result.results.map((item, index) => (

                <div className="result-card" key={index}>

                    <div className="result-header">

                        <FileCode size={24} />

                        <h3>{item.file}</h3>

                    </div>

                    <div
                        className={
                            item.status === "PASS"
                                ? "status pass-status"
                                : "status fail-status"
                        }
                    >

                        {item.status === "PASS" ? (
                            <CheckCircle size={18} />
                        ) : (
                            <XCircle size={18} />
                        )}

                        {item.status}

                    </div>

                    {item.reason && (

                        <div className="reason">

                            <strong>Reason</strong>

                            <p>{item.reason}</p>

                        </div>

                    )}

                </div>

            ))}

        </div>

    );

}

export default ResultCard;
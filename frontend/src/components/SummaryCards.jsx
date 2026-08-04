function SummaryCards({ result }) {

    if (!result) return null;

    return (
        <div className="summary-cards">

            <div className="summary-card total">
                <h3>Total Files</h3>
                <h1>{result.terraform_files_found}</h1>
            </div>

            <div className="summary-card pass">
                <h3>Passed</h3>
                <h1>{result.passed}</h1>
            </div>

            <div className="summary-card fail">
                <h3>Failed</h3>
                <h1>{result.failed}</h1>
            </div>

        </div>
    );

}

export default SummaryCards;
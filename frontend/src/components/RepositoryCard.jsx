import { FolderGit2 } from "lucide-react";

function RepositoryCard({ result }) {

  if (!result) return null;

  return (
    <div className="repository-card">

      <div className="repo-header">
        <FolderGit2 size={28} />
        <h2>Repository Information</h2>
      </div>

      <div className="repo-body">

        <div className="repo-item">
          <label>Repository URL</label>

          <p>{result.repository}</p>
        </div>

        <div className="repo-item">
          <label>Terraform Files Found</label>

          <p>{result.terraform_files_found}</p>
        </div>

      </div>

    </div>
  );

}

export default RepositoryCard;
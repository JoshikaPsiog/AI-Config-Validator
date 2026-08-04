import { ShieldCheck } from "lucide-react";

function Header() {
  return (
    <header className="header">
      <div className="header-content">
        <ShieldCheck size={40} className="logo" />

        <div>
          <h1>AI Configuration Validator</h1>
          <p>Secure Infrastructure Validation using AI</p>
        </div>
      </div>
    </header>
  );
}

export default Header;
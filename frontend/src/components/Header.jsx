import { ShieldCheck } from "lucide-react";
import "./header.css";

function Header() {
  return (
    <header className="header">
      <div className="header-content">
        <ShieldCheck size={42} className="logo" />

        <div>
          <h1>AI Configuration Validator</h1>
          <p>Secure Infrastructure Validation using AI</p>
        </div>
      </div>
    </header>
  );
}

export default Header;
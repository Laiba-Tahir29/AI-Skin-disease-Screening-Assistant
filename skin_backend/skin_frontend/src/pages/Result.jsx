import { useLocation, Link } from 'react-router-dom';
import './Result.css';
import { useEffect } from 'react';

function Result() {
  const location = useLocation();
  const data = location.state;
  useEffect(() => {
    if (data?.result?.disease) {
      sessionStorage.setItem('lastCondition', data.result.disease);
    }
  }, [data]);

  if (!data) {
    return (
      <div className="container result-empty">
        <p>No result to show yet.</p>
        <Link to="/screen" className="cta">Start a screening →</Link>
      </div>
    );
  }

  const { result, preview } = data;

  const riskClass = {
    HIGH: 'risk-high',
    MEDIUM: 'risk-medium',
    LOW: 'risk-low',
  }[result.risk_level] || 'risk-low';

  const riskLabel = {
    HIGH: 'Higher concern — see a dermatologist soon',
    MEDIUM: 'Worth monitoring — a check-up is a good idea',
    LOW: 'Lower concern based on this screening',
  }[result.risk_level];

  return (
    <div className="result container">
      <p className="eyebrow">Step 2 of 2</p>
      <h1>Screening result</h1>

      <div className="result-card">
        {preview && <img src={preview} alt="Analyzed" className="result-img" />}

        <div className="result-body">
          <span className={`risk-pill ${riskClass}`}>{result.risk_level} RISK</span>
          <h2>{result.disease}</h2>

          <div className="confidence-row">
            <div className="confidence-bar-track">
              <div
                className="confidence-bar-fill"
                style={{ width: `${result.confidence}%` }}
              ></div>
            </div>
            <span className="confidence-value">{result.confidence}%</span>
          </div>
          <p className="confidence-label">Model confidence</p>

          <p className="risk-explainer">{riskLabel}</p>
        </div>
      </div>

      <div className="disclaimer-card">
        <strong>Not a diagnosis.</strong> {result.disclaimer}
      </div>

      <Link to="/screen" className="cta secondary">Screen another photo</Link>
    </div>
  );
}

export default Result;
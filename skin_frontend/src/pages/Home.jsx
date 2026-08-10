import { Link } from 'react-router-dom';
import heroImage from '../assets/hero.png';
import './Home.css';

function Home() {
  return (
    <div className="home">
      <section className="hero container">
        <div className="hero-copy">
          <p className="eyebrow">AI-powered skin screening</p>
          <h1>See what your skin might be telling you.</h1>
          <p className="hero-sub">
            Upload a clear photo of the affected area. Our model screens across
            23 common skin conditions and flags anything that may need a
            dermatologist's attention.
          </p>

          <div className="hero-actions">
            <Link to="/screen" className="cta">Start a screening →</Link>
            <span className="hero-note">Fast, guided, and built for clear photos</span>
          </div>
        </div>

        <div className="hero-visual">
          <div className="hero-card">
            <img src={heroImage} alt="Animated skin screening preview" className="hero-image" />
            <div className="hero-overlay hero-overlay-bottom">Powered by AI screening</div>
          </div>
          <div className="scan-demo">
            <div className="scan-demo-copy">Animated scan preview</div>
            <div className="scan-frame">
              <div className="scan-line"></div>
            </div>
          </div>
        </div>
      </section>

      <section className="how container">
        <div className="how-item">
          <span className="how-num">Upload</span>
          <p>Take or choose a clear, well-lit photo of the skin area you're concerned about.</p>
        </div>
        <div className="how-item">
          <span className="how-num">Screen</span>
          <p>The model checks the image and estimates the most likely condition.</p>
        </div>
        <div className="how-item">
          <span className="how-num">Review</span>
          <p>See the result, confidence, and risk level — then decide your next step.</p>
        </div>
      </section>

      <section className="features container">
        <div className="features-head">
          <span className="section-kicker">Why DermaScan</span>
          <h2>Built to guide, not replace, your doctor</h2>
          <p>
            DermaScan gives you a clearer picture before your appointment —
            not a diagnosis. It's a first step, not the final word.
          </p>
        </div>

        <div className="features-grid">
          <div className="feature-card">
            <span className="feature-icon">🧠</span>
            <h3>23 conditions screened</h3>
            <p>Trained across a broad range of common skin conditions to give a well-rounded first read.</p>
          </div>
          <div className="feature-card">
            <span className="feature-icon">📊</span>
            <h3>Confidence & risk level</h3>
            <p>Every result comes with a confidence score and a Low, Medium, or High risk rating.</p>
          </div>
          <div className="feature-card">
            <span className="feature-icon">💬</span>
            <h3>Chat for guidance</h3>
            <p>Ask our assistant follow-up questions and get general advice — no medication, no diagnosis.</p>
          </div>
          <div className="feature-card">
            <span className="feature-icon">⚡</span>
            <h3>Fast, one-photo start</h3>
            <p>No sign-up hurdles — upload a photo and get your screening result in moments.</p>
          </div>
        </div>
      </section>

      <section className="disclaimer-banner container">
        <p><span className="disclaimer-mark">⚠</span> This tool screens, it doesn't diagnose. Always confirm results with a certified dermatologist.</p>
      </section>
    </div>
  );
}

export default Home;
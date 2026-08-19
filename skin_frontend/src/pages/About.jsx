import { Link } from 'react-router-dom';
import './About.css';
import chatbotpic from '../assets/chatbot.png';
import skinDetailTwo from '../assets/pic2.png';
import skinDetail1 from '../assets/pic1.png';

function About() {
  return (
    <section className="about container">
      <div className="about-hero">
        <div className="about-hero-text">
          <p className="eyebrow">ABOUT THE ASSISTANT</p>
          <h1>
            AI-powered skin screening,
            <span> made simple.</span>
          </h1>
          <p className="about-intro">
            Our assistant helps you understand a skin concern by analyzing an
            uploaded image and giving a preliminary screening result in a simple,
            easy-to-follow way.
          </p>
        </div>

        <div className="about-hero-visual">
          <img src={skinDetail1} alt="Skin detail illustration" />
        </div>
      </div>

      <div className="about-layout">
        <div className="about-info">
          <p className="section-label">HOW IT WORKS</p>
          <h2>
            A simple way to get
            <span> an initial insight.</span>
          </h2>
          <p>
            Upload a clear photo of the skin area you are concerned about. The AI
            model studies the image and looks for patterns that may be linked to
            common skin conditions.
          </p>
          <p>
            You then receive a result with a risk level that helps explain the
            screening in a clearer way.
          </p>

          <div className="steps">
            <div className="step">
              <span>01</span>
              <div>
                <h3>Upload</h3>
                <p>Choose a clear image of the skin concern.</p>
              </div>
            </div>
            <div className="step">
              <span>02</span>
              <div>
                <h3>Analyze</h3>
                <p>The AI looks for visual patterns linked to common conditions.</p>
              </div>
            </div>
            <div className="step">
              <span>03</span>
              <div>
                <h3>Understand</h3>
                <p>Review the screening result and risk level.</p>
              </div>
            </div>
          </div>

          <div className="about-mini-stats">
            <div className="mini-stat">
              <span className="mini-stat-num">3</span>
              <span className="mini-stat-label">Risk levels</span>
            </div>
            <div className="mini-stat">
              <span className="mini-stat-num">2 min</span>
              <span className="mini-stat-label">Screening time</span>
            </div>
            <div className="mini-stat">
              <span className="mini-stat-num">24/7</span>
              <span className="mini-stat-label">Chatbot help</span>
            </div>
          </div>
        </div>

        <div className="risk-sidebar">
          <p className="section-label">RISK LEVELS</p>
          <h2>What the colors mean</h2>
          <p className="risk-sidebar-intro">
            These levels are meant to make your result easier to understand.
            They are not medical diagnoses.
          </p>

          <div className="risk-visual">
            <img src={skinDetailTwo} alt="Skin irritation detail" />
          </div>

          <div className="risk-line low">
            <span className="risk-dot"></span>
            <div>
              <h3>Low Risk</h3>
              <p>Usually linked to more common and less urgent concerns.</p>
            </div>
          </div>

          <div className="risk-line medium">
            <span className="risk-dot"></span>
            <div>
              <h3>Medium Risk</h3>
              <p>May need closer attention or a professional check-up.</p>
            </div>
          </div>

          <div className="risk-line high">
            <span className="risk-dot"></span>
            <div>
              <h3>High Risk</h3>
              <p>May require prompt medical review by a qualified professional.</p>
            </div>
          </div>
        </div>
      </div>


      <div className="chatbot-block">
        <div className="chatbot-text">
          <p className="section-label">AI CHATBOT</p>
          <h2>
            Your skin health
            <span> companion.</span>
          </h2>
          <p>
            Need help understanding your result? The built-in chatbot can offer
            advice and recommendations to guide you until you're able to consult
            a proper dermatologist.
          </p>
          <Link to="/screen" className="cta">
            Start a screening →
          </Link>
        </div>
        <div className="chatbot-image-wrap">
          <img src={chatbotpic} alt="Chatbot illustration" className="chatbot-image" />
        </div>
      </div>

      <div className="about-disclaimer">
        <p className="section-label">IMPORTANT</p>
        <h2>Screening, not diagnosis.</h2>
        <p>
          This app is a screening tool for preliminary guidance only. It is not a
          diagnosis tool and should not replace advice from a qualified doctor or
          dermatologist.
        </p>
      </div>
    </section>
  );
}

export default About;

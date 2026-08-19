import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { predictSkinDisease } from '../services/api';
import './Screen.css';

function Screen() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState(null);
  const navigate = useNavigate();

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setSelectedImage(file);
      setPreview(URL.createObjectURL(file));
      setErrorMsg(null);
    }
  };

  const handleAnalyze = async () => {
    if (!selectedImage) {
      setErrorMsg('Please choose an image first.');
      return;
    }

    setLoading(true);
    setErrorMsg(null);

    try {
      const data = await predictSkinDisease(selectedImage);

      if (data.error) {
        setErrorMsg(data.message);
        setLoading(false);
        return;
      }

      navigate('/result', { state: { result: data, preview } });
    } catch (error) {
      console.error(error);
      setErrorMsg('Something went wrong. Please check that the backend server is running.');
      setLoading(false);
    }
  };

  return (
    <div className="screen container">
      <p className="eyebrow">Step 1 of 2</p>
      <h1>Upload a photo</h1>
      <p className="screen-sub">
        Choose a clear, close-up photo of the affected skin area. Good lighting
        helps the model give a more reliable screening.
      </p>

      <label className="upload-box" htmlFor="file-input">
        {preview ? (
          <img src={preview} alt="Selected" className="preview-img" />
        ) : (
          <>
            <div className="scan-frame small">
              <div className="scan-line"></div>
            </div>
            <span className="upload-text">Click to choose an image</span>
            <span className="upload-hint">Clear and well-lit</span>
          </>
        )}
      </label>
      <input
        id="file-input"
        type="file"
        accept="image/*"
        onChange={handleImageChange}
        style={{ display: 'none' }}
      />

      {errorMsg && <div className="error-box">{errorMsg}</div>}

      <section className="risk-guide" aria-label="Risk level guide">
        <div className="risk-guide-heading">
          <span className="risk-guide-kicker">Risk levels</span>
          <h2>Know what the result means</h2>
        </div>

        <div className="risk-list">
          <div className="risk-item low">
            <span className="risk-label">Low</span>
            <p>Usually common and less urgent. Keep an eye on it and follow up if it changes.</p>
          </div>
          <div className="risk-item medium">
            <span className="risk-label">Medium</span>
            <p>Worth paying attention to. A dermatologist visit is a good next step.</p>
          </div>
          <div className="risk-item high">
            <span className="risk-label">High</span>
            <p>More concerning. Please seek medical review soon.</p>
          </div>
        </div>
      </section>

      <button
        className="cta full-width"
        onClick={handleAnalyze}
        disabled={loading || !selectedImage}
      >
        {loading ? 'Analyzing…' : 'Analyze Image'}
      </button>
    </div>
  );
}

export default Screen;
import { useState } from 'react';
import './App.css';

function App() {
  const [userInput, setUserInput] = useState('');
  const [nOutput, setNOutput] = useState(1);
  const [jsonData, setJsonData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleGenerate = async () => {

    if (nOutput < 1 || nOutput > 10) {
      setError('Only 1 - 10 output allowed');
      setJsonData(null);
      return; // Do not send request if invalid
    }

    setLoading(true);
    setError('');
    setJsonData(null);
    try {
      const response = await fetch(
        `http://localhost:8000/gen?user_prompt=${encodeURIComponent(userInput)}&n_output=${nOutput}`
      );
      if (!response.ok) {
        throw new Error('API Error: ' + response.statusText);
      }
      const data = await response.json();
      setJsonData(data);
    } catch (e) {
      setError('Failed to fetch prompts');
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  const inputStyle = {
    height: '40px',
    padding: '0 12px',
    fontSize: '16px',
    borderRadius: '4px',
    border: '1px solid #ccc',
    marginRight: '10px',
    flexGrow: 1,
    boxSizing: 'border-box'
  };

  const smallInputStyle = {
    ...inputStyle,
    flexGrow: 0,
    width: '80px',
    marginRight: '10px',
  };

  const buttonStyle = {
    height: '40px',
    padding: '0 16px',
    fontSize: '16px',
    borderRadius: '4px',
    cursor: 'pointer',
    flexShrink: 0,
  };

  return (
    <div style={{ maxWidth: '700px', margin: '40px auto', fontFamily: 'Arial, sans-serif' }}>
      <h1 style={{ fontSize: '3rem', marginBottom: '20px', textAlign: 'center' }}>
        Prompt Generator
      </h1>
      <div style={{ display: 'flex', alignItems: 'center', marginBottom: '20px' }}>
        <input
          type="text"
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          placeholder="Enter prompt"
          style={inputStyle}
        />
        <input
          type="number"
          value={nOutput}
          onChange={(e) => setNOutput(Number(e.target.value))}
          min="1"
          max="10"
          style={smallInputStyle}
        />
        <button onClick={handleGenerate} disabled={loading} style={buttonStyle}>
          {loading ? 'Loading...' : 'Generate'}
        </button>
      </div>
      {error && <div style={{ color: 'red', marginBottom: '20px' }}>{error}</div>}
      <div style={{ marginTop: '1rem' }}>
        {jsonData?.prompts?.map((prompt, index) => (
          <div 
            key={index} 
            style={{ 
              border: '1px solid #ccc',
              borderRadius: '4px',
              padding: '1rem',
              marginBottom: '1rem',
              backgroundColor: 'transparent',
              whiteSpace: 'pre-wrap',
              wordWrap: 'break-word',
              textAlign: 'left',
              position: 'relative'
            }}
          >
            {/* Copy Button at top right corner */}
            <button
              style={{
                position: 'absolute',
                top: '8px',
                right: '8px',
                backgroundColor: '#transparent',
                border: 'none',
                borderRadius: '4px',
                padding: '4px 8px',
                cursor: 'pointer',
                fontWeight: 'bold',
                fontSize: '0.75rem'
              }}
              onClick={() => navigator.clipboard.writeText(
                prompt.startsWith('"') && prompt.endsWith('"') ? prompt.slice(1, -1) : prompt
              )}
              title="Copy this prompt"
            >
              📋
            </button>
            {prompt.startsWith('"') && prompt.endsWith('"') ? prompt.slice(1, -1) : prompt}
          </div>
        ))}

      </div>
    </div>
  );
}

export default App;

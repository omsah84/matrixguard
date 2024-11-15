import React, { useState } from 'react';

export default function Siva() {
  const [message, setMessage] = useState('');

  const handleInputChange = (e) => {
    setMessage(e.target.value);
  };

  const handleButtonClick = (action) => {
    alert(`${action} button clicked! Message: ${message}`);
    setMessage(''); // Clear the input field after alert
  };

  return (
    <div
      className="d-flex flex-column justify-content-start align-items-center vh-100 pt-5"
      style={{ paddingTop: '100px', fontFamily: 'VT323, monospace' }} // Adding the hacker font
    >
      {/* Heading */}
      <a
        href="https://github.com/omsah84/matrixguard"
        target="_blank"
        rel="noopener noreferrer"
        style={{
          textDecoration: 'none', // Remove default underline
        }}
      >
        <h1
          className="mb-5 fw-bold text-center"
          style={{
            fontSize: '3.5rem',
            color: '#007BFF',
            marginTop: '30px',
            fontFamily: 'VT323, monospace', // Same hacker font for the heading
          }}
        >
          MATRIXGUARD
        </h1>
      </a>

      {/* Input Section */}
      <div className="w-100" style={{ maxWidth: '600px' }}>
        <input
          type="text"
          className="form-control mb-4 p-4 shadow-lg"
          placeholder="Enter your message..."
          value={message}
          onChange={handleInputChange}
          style={{
            borderRadius: '30px',
            border: '1px solid #ddd',
            height: '70px',
            fontSize: '1.2rem',
            transition: 'all 0.3s ease',
            fontFamily: 'Russo One, sans-serif', // Apply hacker-like font to the input box
          }}
        />

        {/* Buttons */}
        <div className="d-flex justify-content-around mt-3">
          <button
            className="btn btn-primary px-5 py-2 shadow-lg"
            onClick={() => handleButtonClick('Encrypt')}
            style={{
              fontSize: '1.2rem',
              borderRadius: '30px',
              transition: 'all 0.3s ease',
            }}
            onMouseEnter={(e) => {
              e.target.style.transform = 'scale(1.05)';
              e.target.style.boxShadow = '0 8px 16px rgba(0, 123, 255, 0.3)';
            }}
            onMouseLeave={(e) => {
              e.target.style.transform = 'scale(1)';
              e.target.style.boxShadow = 'none';
            }}
          >
            Encrypt
          </button>
          <button
            className="btn btn-secondary px-5 py-2 shadow-lg"
            onClick={() => handleButtonClick('Decrypt')}
            style={{
              fontSize: '1.2rem',
              borderRadius: '30px',
              transition: 'all 0.3s ease',
            }}
            onMouseEnter={(e) => {
              e.target.style.transform = 'scale(1.05)';
              e.target.style.boxShadow = '0 8px 16px rgba(108, 117, 125, 0.3)';
            }}
            onMouseLeave={(e) => {
              e.target.style.transform = 'scale(1)';
              e.target.style.boxShadow = 'none';
            }}
          >
            Decrypt
          </button>
        </div>
      </div>
    </div>
  );
}

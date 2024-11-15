import React, { useState } from 'react';

function Ajay() {
    const [text, setText] = useState('');

    // Dummy encryption/decryption functions for now
    const encryptText = () => {
        setText(text.split('').reverse().join('')); // Reverse the text as encryption example
    };

    const decryptText = () => {
        setText(text.split('').reverse().join('')); // Reverse back to original text
    };

    return (


        <>
    
        
        

        <div style={{
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'center',  // Centering vertically
            alignItems: 'center',      // Centering horizontally
            minHeight: '100vh',         // Taking full height of the viewport
            backgroundColor: '#f9f9f9',  // Bright background
            color: '#333',              // Dark text color for contrast
            fontFamily: 'Arial, sans-serif',
            textAlign: 'center',
            padding: '20px',
            width:"100%"
        }}>
            {/* Main Title */}
            <h1 style={{
                fontSize: '3rem',
                marginBottom: '30px',
                color: '#ff6347', // Bright color for heading
                textAlign: 'center',
                marginTop: 0,
            }}>
                MATRIX_GUARD
            </h1>

            {/* Text Area */}
            <textarea
                style={{
                    width: '400px',
                    height: '120px',
                    marginBottom: '30px',
                    padding: '15px',
                    fontSize: '16px',
                    borderRadius: '8px',
                    border: '2px solid #4CAF50', // Green border for text area
                    backgroundColor: '#ffffff', // White background for the text area
                    color: '#333', // Dark text color
                    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
                    marginTop: '20px',
                }}
                value={text}
                onChange={(e) => setText(e.target.value)}
                placeholder="Enter text to encrypt or decrypt..."
            ></textarea>

            {/* Action Buttons */}
            <div style={{
                display: 'flex',
                justifyContent: 'center', // Align buttons in the center
                gap: '20px', // Space between buttons
            }}>
                <button
                    onClick={encryptText}
                    style={{
                        padding: '12px 30px',
                        backgroundColor: '#4CAF50', // Green for Encrypt
                        color: 'white',
                        border: 'none',
                        borderRadius: '5px',
                        cursor: 'pointer',
                        fontSize: '16px',
                        boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
                    }}
                >
                    Encrypt
                </button>
                <button
                    onClick={decryptText}
                    style={{
                        padding: '12px 30px',
                        backgroundColor: '#f44336', // Red for Decrypt
                        color: 'white',
                        border: 'none',
                        borderRadius: '5px',
                        cursor: 'pointer',
                        fontSize: '16px',
                        boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
                    }}
                >
                    Decrypt
                </button>
            </div>
        </div>

        </>
    );
}

export default Ajay;

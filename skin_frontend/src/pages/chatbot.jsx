import { useState, useRef, useEffect } from 'react';
import './chatbot.css';
import chatbotAvatar from '../assets/chatbot.png';

function ChatWidget() {
  const [open, setOpen] = useState(false);
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([
    { from: 'bot', text: "Hi 👋 I'm here to help with general questions about your screening result. I won't diagnose or suggest medication — just guidance before your appointment." }
  ]);
  const bodyRef = useRef(null);


  useEffect(() => {
    if (bodyRef.current) {
      bodyRef.current.scrollTop = bodyRef.current.scrollHeight;
    }
  }, [messages, open]);

  const handleSend = async (e) => {
  e.preventDefault();

  if (!input.trim()) return;

  const userText = input.trim();

  setMessages((prev) => [
    ...prev,
    { from: 'user', text: userText }
  ]);

  setInput('');

  try {
    const response  = await fetch('http://127.0.0.1:8000/chat', { 
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        message: userText,
        condition: sessionStorage.getItem('lastCondition') || '',
      }),
    });

    if (!response.ok) {
      throw new Error(`Server error: ${response.status}`);
    }

    const data = await response.json();

    setMessages((prev) => [
      ...prev,
      {
        from: 'bot',
        text: data.response,
      },
    ]);

  } catch (error) {
    console.error('Chat error:', error);

    setMessages((prev) => [
      ...prev,
      {
        from: 'bot',
        text: 'Sorry, I could not connect to the assistant. Please make sure the backend server is running.',
      },
    ]);
  }
};

  return (
    <>
      {open && <div className="chat-backdrop" onClick={() => setOpen(false)} />}

      <div className={`chat-panel ${open ? 'chat-panel-open' : ''}`}>
        <div className="chat-header">
          <div className="chat-header-info">
            <span className="chat-avatar">
              <img src={chatbotAvatar} alt="Assistant avatar" className="chat-avatar-image" />
            </span>
            <div>
              <p className="chat-title">DermaScan Assistant</p>
              <p className="chat-status">We're online</p>
            </div>
          </div>
          <button className="chat-close" onClick={() => setOpen(false)} aria-label="Close chat">✕</button>
        </div>

        <div className="chat-body" ref={bodyRef}>
          {messages.map((msg, i) => (
            <div key={i} className={`chat-bubble ${msg.from}`}>
              {msg.text}
            </div>
          ))}
        </div>

        <form className="chat-input-row" onSubmit={handleSend}>
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Enter your message..."
          />
          <button type="submit" className="chat-send" aria-label="Send message">➤</button>
        </form>
      </div>

      {!open && (
        <button className="chat-fab" onClick={() => setOpen(true)} aria-label="Open chat">
          💬
        </button>
      )}
    </>
  );
}

export default ChatWidget;
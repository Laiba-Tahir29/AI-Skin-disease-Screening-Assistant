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

  const getBotReply = (text) => {
    const message = text.toLowerCase();
    if (message.includes('low')) return 'Low risk usually means the result looks less concerning. Keep monitoring the area and use the result as general guidance.';
    if (message.includes('medium')) return 'Medium risk means it is worth paying attention to. If the issue persists, a dermatologist visit is a good next step.';
    if (message.includes('high')) return 'High risk is more concerning. Please get a dermatologist or doctor to review it soon.';
    if (message.includes('result') || message.includes('disease')) return 'You can ask me about the risk level, what the result means, or what to do next.';
    if (message.includes('photo') || message.includes('image')) return 'Use a clear, well-lit close-up photo. Blurry or dark images can make the screening less reliable.';
    return 'I can explain low, medium, and high risk, or help you understand how to read the screening result.';
  };

  useEffect(() => {
    if (bodyRef.current) {
      bodyRef.current.scrollTop = bodyRef.current.scrollHeight;
    }
  }, [messages, open]);

  const handleSend = (e) => {
    e.preventDefault();
    if (!input.trim()) return;
    const userText = input.trim();
    setMessages((prev) => [...prev, { from: 'user', text: userText }]);
    setInput('');
    setTimeout(() => {
      setMessages((prev) => [...prev, { from: 'bot', text: getBotReply(userText) }]);
    }, 500);
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
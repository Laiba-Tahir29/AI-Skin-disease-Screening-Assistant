import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Screen from './pages/Screen';
import Result from './pages/Result';
import About from './pages/About';
import ChatWidget from './pages/chatbot';

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/screen" element={<Screen />} />
        <Route path="/result" element={<Result />} />
        <Route path="/about" element={<About />} />
      </Routes>
      <ChatWidget />
    </BrowserRouter>
  );
}

export default App;
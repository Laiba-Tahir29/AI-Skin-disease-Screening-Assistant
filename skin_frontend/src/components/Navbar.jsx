import { useState, useEffect, useRef } from 'react';
import { NavLink } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
  const [hidden, setHidden] = useState(false);
  const lastScrollY = useRef(0);

  useEffect(() => {
    const handleScroll = () => {
      const currentScrollY = window.scrollY;

      if (currentScrollY < 80) {
        // near the top — always show
        setHidden(false);
      } else if (currentScrollY > lastScrollY.current) {
        // scrolling down
        setHidden(true);
      } else {
        // scrolling up
        setHidden(false);
      }

      lastScrollY.current = currentScrollY;
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <nav className={`navbar ${hidden ? 'navbar-hidden' : ''}`}>
      <div className="navbar-inner container">
        <NavLink to="/" className="logo">
          <span className="logo-mark">◐</span> DermaScan
        </NavLink>
        <div className="nav-links">
          <NavLink to="/" end className={({isActive}) => isActive ? 'active' : ''}>Home</NavLink>
          <NavLink to="/about" className={({isActive}) => isActive ? 'active' : ''}>About</NavLink>
          <NavLink to="/screen" className={({isActive}) => isActive ? 'active' : ''}>Screen</NavLink>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
import React from 'react';
import './header.css';
import Logo from './img/nu.png';
import { useEffect, useRef } from 'react';

  

const Header = () => {

  const creditosRef = useRef(null);

  // Función para hacer scroll al componente de créditos cuando la URL es /credito
  useEffect(() => {
    if (window.location.pathname === '/credito' && creditosRef.current) {
      creditosRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, []);
  
  return (
    <header className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="container">
        
        <div className="navbar-brand">
          <img src={Logo} alt="Logo" />
        </div>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav ms-auto">
            <li className="nav-item">
              <a className="nav-link" href="/">Inicio</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="/credito">Creditos</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="/">contacto</a>
            </li>
            
          </ul>
        </div>
      </div>
    </header>
  );
}

export default Header;

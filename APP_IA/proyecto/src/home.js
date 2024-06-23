import React from 'react';
import './home.css'; // Archivo de estilos CSS
import creditos from './img/creditos.jpg'; // Ruta de la imagen de créditos

const Home = () => {
  return (
    <div className="creditos-container">
      
      <div className="creditos-info">
        <div className="creditos-details">
        <h2>Créditos Bancarios</h2>
          <p>
            Los créditos bancarios son préstamos que las entidades financieras otorgan a sus clientes, 
            ya sean individuos o empresas, con el fin de cubrir necesidades financieras específicas.
          </p>
          <p>
            Estos créditos pueden ser utilizados para una variedad de propósitos, como la compra de una 
            vivienda, un automóvil, el financiamiento de estudios, la expansión de un negocio, entre otros.
          </p>
        </div>
        <div className="creditos-images">
          <img src={creditos} alt="Créditos" />
        </div>
      </div>
    </div>
  );
}

export default Home;

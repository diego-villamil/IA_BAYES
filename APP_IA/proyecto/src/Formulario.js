import React, { useState } from 'react';
import axios from 'axios';

const genderOptions = ['Male', 'Female'];
const occupationOptions = ['Engineer', 'Teacher', 'Student', 'Manager', 'Accountant', 'Nurse', 'Lawyer', 'Artist', 'IT', 'Doctor', 'Consultant', 'Analyst', 'Salesman', 'Marketing', 'Architect', 'Designer', 'Pharmacist', 'Researcher', 'Professor', 'Pilot', 'Receptionist', 'Banker', 'Writer', 'Chef', 'Veterinarian', 'Sales', 'HR', 'Electrician', 'Musician', 'Programmer', 'Dentist', 'Photographer', 'Editor', 'Stylist', 'Software', 'Accountant'];
const educationLevelOptions = ["Bachelor's", "Master's", 'High School', "Associate's", 'Doctoral'];
const maritalStatusOptions = ['Married', 'Single'];

function Formulario() {
  const [edad, setEdad] = useState('');
  const [genero, setGenero] = useState('');
  const [ocupacion, setOcupacion] = useState('');
  const [nivelEducativo, setNivelEducativo] = useState('');
  const [estadoCivil, setEstadoCivil] = useState('');
  const [salario, setSalario] = useState('');
  const [puntajeCredito, setPuntajeCredito] = useState('');
  const [resultadoPrediccion, setResultadoPrediccion] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
        const formData = {
            edad: parseInt(edad),
            genero: genero === 'Male' ? 0 : 1,
            ocupacion: occupationOptions.indexOf(ocupacion),
            nivel_educativo: educationLevelOptions.indexOf(nivelEducativo),
            estado_civil: maritalStatusOptions.indexOf(estadoCivil),
            salario: parseInt(salario),
            puntaje_credito: parseInt(puntajeCredito)
        };
        const response = await axios.post('http://127.0.0.1:5000/api/prediccion', formData);
        setResultadoPrediccion(response.data.prediccion);
    } catch (error) {
        console.error('Error al enviar los datos del formulario:', error);
    }
};


  return (
    <form onSubmit={handleSubmit}>
      <div className="content-formulario">
        <h2>Formulario de Solicitud de Crédito</h2>
        <div className='seccion-input'>
          <div className="seccion-formulario">
            <label>Edad:</label>
            <input type="number" value={edad} onChange={(e) => setEdad(e.target.value)} />
          </div>
          <div className="seccion-formulario">
            <label>Género:</label>
            <select value={genero} onChange={(e) => setGenero(e.target.value)}>
              <option value="">Selecciona</option>
              {genderOptions.map((option, index) => (
                <option key={index} value={option}>{option}</option>
              ))}
            </select>
          </div>
          <div className="seccion-formulario">
            <label>Ocupación:</label>
            <select value={ocupacion} onChange={(e) => setOcupacion(e.target.value)}>
              <option value="">Selecciona</option>
              {occupationOptions.map((option, index) => (
                <option key={index} value={option}>{option}</option>
              ))}
            </select>
          </div>
          <div className="seccion-formulario">
            <label>Nivel Educativo:</label>
            <select value={nivelEducativo} onChange={(e) => setNivelEducativo(e.target.value)}>
              <option value="">Selecciona</option>
              {educationLevelOptions.map((option, index) => (
                <option key={index} value={option}>{option}</option>
              ))}
            </select>
          </div>
          <div className="seccion-formulario">
            <label>Estado Civil:</label>
            <select value={estadoCivil} onChange={(e) => setEstadoCivil(e.target.value)}>
              <option value="">Selecciona</option>
              {maritalStatusOptions.map((option, index) => (
                <option key={index} value={option}>{option}</option>
              ))}
            </select>
          </div>
          <div className="seccion-formulario">
            <label>Salario:</label>
            <input type="number" value={salario} onChange={(e) => setSalario(e.target.value)} />
          </div>
          <div className="seccion-formulario">
            <label>Puntaje de Crédito:</label>
            <input type="number" value={puntajeCredito} onChange={(e) => setPuntajeCredito(e.target.value)} />
          </div>
        </div>
        <button className='boton-principal' type="submit">Enviar</button>
        {resultadoPrediccion !== null && (
        <p>Resultado de la predicción: {resultadoPrediccion ? 'Approved' : 'Denied'}</p>
      )}
      </div>
      
    </form>
  );
}

export default Formulario;

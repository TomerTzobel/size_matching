import React from 'react';
import './App.css';
import { Footer } from './components/Footer';
// import Footer from './components/Footer2'
import logo from './logo.png';
import AppBody from './components/AppBody';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
      <AppBody /> 
      <Footer></Footer>
    </div>
  );
}

export default App;

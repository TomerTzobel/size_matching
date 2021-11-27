import React from 'react';
import './App.css';
import { Footer } from './components/Footer';
// import Footer from './components/Footer2'
import Cards from './components/Cards';
import logo from './logo.png';
import Filters from './components/Filters';
import RecommendedSize from './components/RecommendedSize';
import MySizes from './components/MySizes';
import { itemsList } from './data/items';
import { useDispatch } from 'react-redux';

function App() {
  const dispatch = useDispatch();
  dispatch({type: "SET_ITEMS",payload: itemsList});
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
      <Filters />
      <RecommendedSize />
      <Cards />
      <MySizes />
      <Footer></Footer>
    </div>
  );
}

export default App;

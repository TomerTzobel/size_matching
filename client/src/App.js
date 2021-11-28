import React from 'react';
import './App.css';
import { Footer } from './components/Footer';
// import Footer from './components/Footer2'
import Cards from './components/Cards';
import logo from './logo.png';
import RecommendedSize from './components/RecommendedSize';
import MySizes from './components/MySizes';
import { itemsList } from './data/items';
import { useDispatch } from 'react-redux';
import SearchBar from './components/SearchBar';

function App() {
  const dispatch = useDispatch();
  dispatch({type: "SET_ITEMS",payload: itemsList});
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
      <SearchBar />
      <RecommendedSize />
      <Cards />
      <MySizes />
      <Footer></Footer>
    </div>
  );
}

export default App;

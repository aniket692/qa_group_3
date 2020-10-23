import React from 'react';
//import logo from './logo.svg';
import './App.css';
import ConfirmConnection from './ConfirmConnection';
import Login from './LoginPage';
import Header from './Header';


function App(props) {
  return (
      <div className="App">
        <Header ></Header>
          <ConfirmConnection/>
          <Login/>
      </div>

  );
}

export default App;

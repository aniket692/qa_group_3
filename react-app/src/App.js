import React from 'react';
//import logo from './logo.svg';
import './App.css';
import ConfirmConnection from './ConfirmConnection';
import Login from './LoginPage';


function App(props) {
  return (
      <div className="App">
          <ConfirmConnection/>
          <Login/>
      </div>

  );
}

export default App;

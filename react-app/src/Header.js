import React from 'react';
import logo from './llogo.gif'; // Tell webpack this JS file uses this image

function Header() {
  // Import result is the URL of your image
  return (
      <div>
      <h1> The Excited Alpacas </h1>
  <img src={logo} alt="Logo" />
  </div>
  )
}
export default Header;
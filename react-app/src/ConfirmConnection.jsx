import React from 'react';
import axios from 'axios';

const ConfirmConnection = () => {

    //let update =  axios.put("http://localhost:8090", "1");
    let response =  axios.get("https://localhost:8090");

    return (
    <h1>Connection is </h1>
    )
}; 

 export default ConfirmConnection;
import React, { useState } from 'react';
import axios from 'axios';

const ConfirmConnection = (props) => {


    const [connection, setConnection] = useState('Checking...')

    axios.get("http://127.0.0.1:8090/db_connection")
                        .then((response) => {
                            setConnection(response.data)
                            });
   
            
    return (
    <h1>Connection status: {connection} </h1>
    )
}; 

 export default ConfirmConnection;
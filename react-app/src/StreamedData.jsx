import axios from "axios";
import React, {useState, useInterval} from "react";

export default function StreamedData(){

    const [deals, setDeals] = useState([])

    const getDeals = () => {
        axios.get("http://127.0.0.1:8090/deals")
                    .then(result => {
                    setDeals([deals, result])
                    console.log(result)
            
                    })
    };

    // useInterval(getDeals, 1000)
    return (
        <body>

<h2>Streamed Historic Data</h2>

{/* <table style="width:100%">
  <tr>
    <th>Instrument Name</th>
    <th>Counterparty</th> 
    <th>Price</th>
    <th>Type</th>
    <th>Time</th>
  </tr>
  <tr>
    <td>{instrumentName}</td>
    <td>{Counterparty}</td>
    <td>{Price}</td>
    <td>{TypeBuy/sell}</td>
    <td>{Time}</td>
  </tr>
</table> */}

</body>

    );
}
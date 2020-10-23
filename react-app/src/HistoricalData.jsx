import axios from "axios";
import React, {useState} from "react";
import { Button} from "react-bootstrap";

export default function HistoricalData(props){

  const user = props.user
  let [instrument, setInstrument] = useState("");
  let [startPeriod, setStartPeriod] = useState("1997-11-14T08:30");
  let [endPeriod, setEndPeriod] = useState("2060-06-01T08:30"); 

  let [averageBuy, setAverageBuy] = useState(""); 
  let [averageSell, setAverageSell] = useState(""); 

  const [endPosition, setEndPosition] = useState('Checking...')
  const [realised, setRealised] = useState('Checking...')
  const [effective, setEffective] = useState('Checking...')

  axios.get("http://127.0.0.1:8090/dealerdata")
                          .then((response) => {
                            console.log(response)
                          })



  function handleSubmit(event) {
    event.preventDefault()
    axios.post("http://127.0.0.1:8090/instrument", {
      'instrument': instrument,
      'startPeriod': startPeriod,
      'endPeriod': endPeriod
  }).then(result => {
      console.log(result)
  })
  }

  return (
    <div>
<h2> Welcome {user}! </h2>


<h2> Dealer Information </h2>
  <p> End position of dealer: {endPosition} </p>
  <p> Realised profit or loss of dealer: {realised} </p>
  <p> Effective profit or loss of dealer: {effective} </p>
  


<h3>Please enter the instrument name and the period you want to search for historic data</h3>


<form>
  <label for="instrumentName">Instrument Name:</label>
  <input type="text" id="instrumentName" name="instrumentName" value={instrument} onChange={e => setInstrument(e.target.value)}/><br></br>
  <label for="startPeriod">Start Period:</label>
  <input type="datetime-local" id="startPeriod" name="startPeriod" value={startPeriod} onChange={e => setStartPeriod(e.target.value)}/><br></br>
  <label for="endPeriod">End Period:</label>
  <input type="datetime-local" id="endPeriod" name="endPeriod" value={endPeriod} onChange={e => setEndPeriod(e.target.value)}/>
</form>

<p><strong>Note:</strong> This tool is not supported in Firefox, Safari or Internet Explorer 12 (or earlier).</p>

      <Button block bsSize="large" onClick={handleSubmit} type="submit">
          Submit
      </Button>
  
  {!(instrument === "") && 
  <div>
  <h2>Averages for the given instrument {instrument} </h2>
  
  <p> Average buy price in the period: {averageBuy} </p>
  <p> Average end price in the period: {averageSell} </p>
  </div>
}
  
</div>

  
  );
}

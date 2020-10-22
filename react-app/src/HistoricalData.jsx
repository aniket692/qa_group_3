import axios from "axios";
import React from "react";

export default function HistoricalData(props){

  let user = props.user

  return (
    <div>
<h2> Welcome {props.user}! </h2>
<h3>Please enter the instrument name and the period you want to search for historic data</h3>


<form>
  <label for="instrumentName">Instrument Name:</label>
  <input type="text" id="instrumentName" name="instrumentName"/><br></br>
  <label for="startPeriod">Start Period:</label>
  <input type="datetime-local" id="startPeriod" name="startPeriod"/><br></br>
  <label for="endPeriod">End Period:</label>
  <input type="datetime-local" id="endPeriod" name="endPeriod"/>
</form>

<p><strong>Note:</strong> This tool is not supported in Firefox, Safari or Internet Explorer 12 (or earlier).</p>

  <input type="submit"/>
  
  <h2>Historic data report</h2>
  
  <p> Average buy price in the period: $averagebuyprice$ </p>
  <p> Average end price in the period: $averageendprice$ </p>
  <p> End position of dealer: $endposition$ </p>
  <p> Realised profit or loss of dealer: $realisedprofitnloss$ </p>
  <p> Effective profit or loss of dealer: $effectiveprofitnloss$ </p>
  
  
</div>

  
  );
}

import axios from "axios";
import React, {useState } from "react";
import { Button, FormGroup, FormControl, ControlLabel} from "react-bootstrap";
import "./Login.css";

export default function Login() {

  let [user, setUser] = useState("");
  const [password, setPassword] = useState("");

  const [isAuth, setAuth] = useState(false);

  function validateForm() {
    return user.length > 0 && password.length > 0;
  }


  function handleSubmit(event) {
    event.preventDefault()
    axios.post("http://127.0.0.1:8090/login", {
        user,
        password
    }).then(result => {
        if (result.status === 200) {
            setAuth(true);
            alert('Login successful!')
        }
    }).catch(e => {
        alert('Incorrect Username or Password, please try again')
    });
    
  }
  return (
    <div className="Login">
      {!isAuth && <form onSubmit={handleSubmit}>
        <FormGroup controlId="username" bsSize="large">
          <ControlLabel>Username</ControlLabel>
          <FormControl
            autoFocus
            type="username"
            value={user}
            onChange={e => setUser(e.target.value)}
          />
        </FormGroup>
        <FormGroup controlId="password" bsSize="large">
          <ControlLabel>Password</ControlLabel>
          <FormControl
            value={password}
            onChange={e => setPassword(e.target.value)}
            type="password"
          />
        </FormGroup>
        <Button block bsSize="large" disabled={!validateForm()} type="submit">
          Login
        </Button>
        
      </form>}
    </div>
  );
}

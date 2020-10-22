import axios from "axios";
import React, { Component, useState } from "react";
import { Button, FormGroup, FormControl, ControlLabel, Modal } from "react-bootstrap";
import { render } from "react-dom";
import "./Login.css";

export default function Login() {

  let [user, setUser] = useState("");
  const [password, setPassword] = useState("");

  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const [isAuth, setAuth] = useState(false);

  function validateForm() {
    return user.length > 0 && password.length > 0;
  }

    function shouldComponentUpdate(nextProps, nextState) {
    if (this.props.isAuth === nextProps.isAuth) {
        return false;
      } else {
        return true;
      }
    }

  function handleSubmit(event) {
    // axios.post("http://127.0.0.1/login", {
    //     user,
    //     password
    // }).then(result => {
    //     if (result.status === 200) {
    //         setAuth(true);
    //         console.log('200')
    //     }
    // }).catch(e => {
    //     console.log('Got error')
    //     setShow(true);
    // })
    setShow(true);
    event.preventDetfault();
  }
  return (
    <div className="Login">
        <Modal show={show} onHide={handleClose}>
            <Modal.Header closeButton>
            <Modal.Title>Modal heading</Modal.Title>
            </Modal.Header>
            <Modal.Body>Woohoo, you're reading this text in a modal!</Modal.Body>
        </Modal>
      <form onSubmit={handleSubmit}>
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
        
      </form>
    </div>
  );
}
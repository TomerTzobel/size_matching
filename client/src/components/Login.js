import React from "react";
import { authenticate } from "../utils/auth";
import { Form, Button, Container, Card, Row, Col } from "react-bootstrap";
import { useState } from "react";
import RegisterModal from "./RegisterModal";
import { useDispatch } from "react-redux";
import { registerNewUser } from '../utils/register'

export const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [err, setErr] = useState("");

  const onLogin = async () => {
    const isAuthenticated = await authenticate(username, password);
    if (!isAuthenticated) {
      setErr("Something went wrong, please try again");
    }
  };

  const dispatch = useDispatch();
  const isEmptyFields = ! (username && password);

  const onRegisterClick = () => {
    registerNewUser(username, password);
    dispatch({type: "REGISTER_MODAL"});
  }
  return (
    <>
      <Container className="w-50 mt-5 mb-5 p-5">
        <Container className="w-50 mt-5 mb-5">
          <Card className="bg-light">
            <Card.Body>
              <Card.Title className="mb-3">Please Login</Card.Title>

              <Form>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                  <Form.Control
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(event) => setUsername(event.target.value)}
                  />
                </Form.Group>

                <Form.Group className="mb-3" controlId="formBasicPassword">
                  <Form.Control
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(event) => setPassword(event.target.value)}
                  />
                  <Form.Text className="text-muted">{err}</Form.Text>
                </Form.Group>
                <Row>
                  <Col>
                    <Button variant="primary" disabled={isEmptyFields} onClick={onLogin}>
                      Login
                    </Button>
                  </Col>
                  <Col>
                    <Button variant="info" disabled={isEmptyFields} onClick={onRegisterClick}>Register</Button>
                  </Col>
                </Row>
              </Form>
            </Card.Body>
          </Card>
        </Container>
      </Container>
      <RegisterModal newUsername={username} />
    </>
  );
};

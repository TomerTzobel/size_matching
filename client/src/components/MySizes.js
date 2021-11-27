import React from "react";
import { connect } from "react-redux";
import { Table, Accordion, Container } from "react-bootstrap";

const MySizes = (props) => {
  const { sizes } = props;
  let cnt = 0;
  const tableRows = sizes.map((item) => (
    <tr key={cnt++}>
      <td>{cnt}</td>
      <td>{item.product}</td>
      <td>{item.brand}</td>
      <td>{item.size}</td>
    </tr>
  ));
  return (
    <Container className="w-80 justify-content-center mt-3">
      <Accordion>
        <Accordion.Item eventKey="0">
          <Accordion.Header>My sizes</Accordion.Header>
          <Accordion.Body>
            <Table striped bordered hover>
              <thead>
                <tr>
                  <th>#</th>
                  <th>Product</th>
                  <th>Brand</th>
                  <th>Type</th>
                </tr>
              </thead>
              <tbody>{tableRows}</tbody>
            </Table>
          </Accordion.Body>
        </Accordion.Item>
      </Accordion>
    </Container>
  );
};

function mapStateToProps(state) {
  return {
    sizes: state.userSizes,
  };
}

export default connect(mapStateToProps)(MySizes);

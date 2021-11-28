import { React, useState } from "react";
import { useDispatch } from "react-redux";
import { Button, ButtonGroup, Container, Modal, Row } from "react-bootstrap";
import { sizes } from "../data/sizes";
import { selectBrand, selectProduct } from "../selectors";
import Filters from "./Filters";
import MySizes from "./MySizes";
import { connect } from "react-redux";

const RegisterModal = (props) => {
  const { showRegisterModal, product, brand, newUsername } = props;
  const [selectedSize, setSelectedSize] = useState("");

  const dispatch = useDispatch();
  const sizeButtons = sizes.map((size) => (
    <Button key={size} onClick={() => setSelectedSize(size)}>
      {size}
    </Button>
  ));

  const resetSelected = () => {
    dispatch({
      type: "SET_PRODUCT",
      payload: "",
    });
    dispatch({
      type: "SET_BRAND",
      payload: "",
    });
    setSelectedSize("");
  };
  const addSize = () => {
    dispatch({
      type: "ADD_SIZE",
      payload: {
        product: selectProduct(),
        brand: selectBrand(),
        size: selectedSize,
      },
    });
    resetSelected();
  };

  const onSave = () => {
    resetSelected();
    dispatch({
      type: "SET_USER",
      payload: newUsername,
    });
    dispatch({
      type: "HIDE_REGISTER",
    });
  };

  const readyToAdd = selectedSize && product && brand;

  return (
    <>
      <Modal show={showRegisterModal}>
        <Modal.Header>
          <Modal.Title>First, let's get to know you better</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Container>
            <Row className="justify-content-md-center">
              Please add at least 3 products and your sizes
            </Row>
          </Container>
          <Container>
            <Row className="justify-content-md-center">
              <Filters />
              <ButtonGroup className="me-2 p-3" aria-label="First group">
                {sizeButtons}
              </ButtonGroup>
              <Button
                variant="info"
                disabled={!readyToAdd}
                className="m-2 w-25"
                onClick={addSize}
              >
                Add
              </Button>
            </Row>
          </Container>
          <MySizes />
        </Modal.Body>
        <Modal.Footer>
          <Button variant="primary" onClick={onSave}>
            Continue shopping
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
};

function mapStateToProps(state) {
  return {
    showRegisterModal: state.showRegisterModal,
    product: state.product,
    brand: state.brand,
  };
}

export default connect(mapStateToProps)(RegisterModal);

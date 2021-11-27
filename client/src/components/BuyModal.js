import { React , useState} from 'react'
import { connect, useDispatch } from 'react-redux';
import { Button, ButtonGroup, Container, Modal, Row } from 'react-bootstrap';
import { sizes } from '../data/sizes'
import { selectBrand, selectProduct } from '../selectors';

const BuyModal = (props) => {
    const { showModal } = props;
    const [selectedSize, setSelectedSize] = useState("s");
    const dispatch = useDispatch();
    const sizeButtons = sizes.map( size => (
        <Button key={size} onClick={()=>setSelectedSize(size)}>{size}</Button>
    ))
    
    const handleClose = () => dispatch({type: "HIDE"});
    const onSave = () => {
        dispatch({
            type: "ADD_SIZE", 
            payload: {
                product: selectProduct(),
                brand: selectBrand(),
                size: selectedSize
            }
        });
        handleClose();
    };

    return (
        <>
        <Modal show={showModal} onHide={handleClose}>
          <Modal.Header closeButton>
            <Modal.Title>Help us know you better</Modal.Title>
          </Modal.Header>
          <Modal.Body>
          <Container><Row className="justify-content-md-center">Which size fit you the best?</Row></Container>
          <Container><Row className="justify-content-md-center">
          <ButtonGroup className="me-2 p-3" aria-label="First group">
              {sizeButtons}
          </ButtonGroup>
          </Row></Container>
          </Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={handleClose}>
              Close
            </Button>
            <Button variant="primary" onClick={onSave}>
              Save
            </Button>
          </Modal.Footer>
        </Modal>
      </>
      )
}

function mapStateToProps(state) {
    return {
      showModal: state.showModal      
    }
  }
  
export default connect(mapStateToProps)(BuyModal);

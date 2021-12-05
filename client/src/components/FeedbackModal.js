import { React , useState} from 'react'
import { connect, useDispatch } from 'react-redux';
import { Button, ButtonGroup, Container, Modal, Row } from 'react-bootstrap';
import { sizes } from '../data/sizes'
import { postSize } from '../utils/postSize';

const FeedbackModal = (props) => {
    const { showModal, item } = props;
    const [selectedSize, setSelectedSize] = useState("s");
    const { brand, name, product } = item;

    const dispatch = useDispatch();
    const sizeButtons = sizes.map( size => (
        <Button key={size} onClick={()=>setSelectedSize(size)}>{size}</Button>
    ))
    
    const handleClose = () => dispatch({type: "HIDE_MODAL"});
    const onSave = () => {        
        dispatch({
            type: "ADD_SIZE", 
            payload: {
                product,
                brand,
                size: selectedSize
            }
        });
        postSize(product, brand, selectedSize);
        handleClose();
    };

    return (
        <>
        <Modal show={showModal} onHide={handleClose}>
          <Modal.Header closeButton>
            <Modal.Title>Help us know you better</Modal.Title>
          </Modal.Header>
          <Modal.Body>
          <Container><Row className="justify-content-md-center">{`You purchased ${name} by ${brand}.`}</Row></Container>
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
      showModal: state.activeModal === 'feedback',
      item: state.activeCart,    
    }
  }
  
export default connect(mapStateToProps)(FeedbackModal);

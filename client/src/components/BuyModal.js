import { React , useState} from 'react'
import { connect, useDispatch } from 'react-redux';
import { Button, ButtonGroup, Container, Modal, Row } from 'react-bootstrap';
import { sizes } from '../data/sizes'
import { postSize } from '../utils/postSize';
import RecommendedSize from './RecommendedSize'

const BuyModal = (props) => {
    const { showModal, activeItem } = props;
    const [selectedSize, setSelectedSize] = useState("s");
    const dispatch = useDispatch();
    const sizeButtons = sizes.map( size => (
        <Button key={size} onClick={()=>setSelectedSize(size)}>{size}</Button>
    ))
    
    const handleClose = () => dispatch({type: "HIDE_MODAL"});
    const onOrder = () => {
        const { product, brand } = activeItem;
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
        setTimeout(() => {
          dispatch({
            type: "FEEDBACK_MODAL", 
          })
        }, 5000);
    };

    return (
        <>
        <Modal show={showModal} onHide={handleClose}>
          <Modal.Header closeButton>
            <Modal.Title>Purchase {activeItem.name}</Modal.Title>
          </Modal.Header>
          <Modal.Body>
          <RecommendedSize/>
          <Container><Row className="justify-content-md-center">Please choose your size</Row></Container>
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
            <Button variant="primary" onClick={onOrder}>
              Order
            </Button>
          </Modal.Footer>
        </Modal>
      </>
      )
}

function mapStateToProps(state) {
    return {
      showModal: state.activeModal === 'buy',
      activeItem: state.activeCart,
    }
  }
  
export default connect(mapStateToProps)(BuyModal);

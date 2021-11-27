import { React } from "react";
import BuyModal from "./BuyModal";
import { Button } from 'react-bootstrap';
import { useDispatch } from 'react-redux';
import { connect } from 'react-redux';

const Cards = (props) => {
  const { items } = props;
  const dispatch = useDispatch();
  const buyHandler = () => dispatch({type: "SHOW"});


  return (
    <div className="row row-cols-1 row-cols-md-3 g-4">
      {items.map((item) => (
        <div key={item.name} className="col">
          <div className="card">
            <img src={item.imgUrl} className="card-img-top" alt={item.name} />
            <div className="card-body">
              <h5 className="card-title">{item.name}</h5>
              <p className="card-text">bla bla bla</p>
              <Button onClick={buyHandler} >Buy</Button>
            </div>
          </div>
        </div>
      ))}
      <BuyModal />
    </div>
  );
};

function mapStateToProps(state) {
  return {
    items: state.items,
  };
}

export default connect(mapStateToProps)(Cards);

import { React } from "react";
import BuyModal from "./BuyModal";
import FeedbackModal from './FeedbackModal';
import { Button } from 'react-bootstrap';
import { useDispatch } from 'react-redux';
import { connect } from 'react-redux';
import NoResults from "./NoResults";
import { getRecommendation } from '../utils/recommendation'

const capitalize = (s) => s.charAt(0).toUpperCase() + s.slice(1).toLowerCase();

const Cards = (props) => {
  const { items, noResultsMessage } = props;
  const dispatch = useDispatch();
  const buyHandler = (item) => {
    dispatch({type: "SET_CART", payload: item});
    dispatch({type: "BUY_MODAL"});
    getRecommendation();
  };
  
  if (noResultsMessage || !items.length){
    return <NoResults />
  }

  const cards = items.map((item) => (
    <div key={item.name} className="col">
      <div className="card">
        <img src={item.imgUrl} className="card-img-top" alt={item.name} />
        <div className="card-body">
          <h5 className="card-title">{item.name}</h5>
          <p className="card-text">{capitalize(item.brand)}</p>
          <Button variant="secondary" onClick={() => buyHandler(item)} >Buy</Button>
        </div>
      </div>
    </div>
  ))

  return (
    <>
    <div className="row row-cols-1 row-cols-md-3 g-4">
      {cards}
      <BuyModal />
      <FeedbackModal />
    </div>
    </>
  );
};

function mapStateToProps(state) {
  return {
    items: state.items,
    noResultsMessage: state.noResultsMessage
  };
}

export default connect(mapStateToProps)(Cards);

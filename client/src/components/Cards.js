import { React } from "react";
import BuyModal from "./BuyModal";
import { Button } from 'react-bootstrap';
import { useDispatch } from 'react-redux';
import { connect } from 'react-redux';
import RecommendedSize from './RecommendedSize';

const Cards = (props) => {
  const { items, search } = props;
  const dispatch = useDispatch();
  const buyHandler = () => dispatch({type: "SHOW"});

  if (!search){
    return (
      <div className='m-5 p-5'>
        <h1 className='m-5 p-5'>Please search for items</h1>
      </div>
    )

  }
  if (!items.length) {
    return (
      <div className='m-5 p-5'>
        <h1 className='m-5 p-5'>Couln't find matching items...</h1>
      </div>
    )
  }
  const cards = items.map((item) => (
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
  ))

  return (
    <>
    <RecommendedSize />
    <div className="row row-cols-1 row-cols-md-3 g-4">
      {cards}
      <BuyModal />
    </div>
    </>
  );
};

function mapStateToProps(state) {
  return {
    items: state.items,
    search: state.searchText
  };
}

export default connect(mapStateToProps)(Cards);

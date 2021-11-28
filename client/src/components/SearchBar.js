import React from "react";
import { Row, Col, Container } from "react-bootstrap";
import Form from "react-bootstrap/Form";

import { connect, useDispatch } from "react-redux";
import { brandList } from "../data/brands";
import { productList } from '../data/products'
import { fetchData } from '../data/fetchData';

const SearchBar = (props) => {
  const { searchText } = props;
  const dispatch = useDispatch();
  const textChangeHandler = (value) =>
    dispatch({ type: "SET_SEARCH", payload: { text: value } });
  const onSearch = (searchKey) => {
      console.log("fetching ...");
      const words = searchKey.split(' ');
      if (words.length !== 2) {
          notFound('length != 2');
          return;
      }
      const input_1 = words[0].toLowerCase();
      const input_2 = words[1].toLowerCase();
      if (brandList.includes(input_1) && productList.includes(input_2)){
        getCards(input_1, input_2);        
      } else if (brandList.includes(input_2) && productList.includes(input_1)){
        getCards(input_2, input_1);
      } else {
        notFound('no matching brand/product');
        return;
      }      
  }

  const notFound = (err) => {
      dispatch({ type: "ITEMS_NOT_FOUND" });
      console.log(err);
  }

  const getCards = (brand, productType) => {      
      fetchData(productType, brand);
      dispatch({type: `SET_BRAND`, payload: brand});
      dispatch({type: `SET_PRODUCT`, payload: productType})
}

  return (
    <Container fluid className="w-50 mt-4">
      <Row>
        <Col>
          <Form.Control
            type="text"
            placeholder="Normal text"
            value={searchText}
            onChange={(e) => textChangeHandler(e.target.value)}
          />
        </Col>
        <Col className="col-1">
          <button type="button" className="btn btn-warning align-left" onClick={() => onSearch(searchText)}>
            <svg width="15px" height="15px">
              <path d="M11.618 9.897l4.224 4.212c.092.09.1.23.02.312l-1.464 1.46c-.08.08-.222.072-.314-.02L9.868 11.66M6.486 10.9c-2.42 0-4.38-1.955-4.38-4.367 0-2.413 1.96-4.37 4.38-4.37s4.38 1.957 4.38 4.37c0 2.412-1.96 4.368-4.38 4.368m0-10.834C2.904.066 0 2.96 0 6.533 0 10.105 2.904 13 6.486 13s6.487-2.895 6.487-6.467c0-3.572-2.905-6.467-6.487-6.467 "></path>
            </svg>
          </button>
        </Col>
      </Row>
    </Container>
  );
};

function mapStateToProps(state) {
  return {
    searchText: state.searchText,
  };
}

export default connect(mapStateToProps)(SearchBar);
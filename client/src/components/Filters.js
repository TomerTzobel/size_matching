import React from "react";
import { Dropdown } from './Dropdown';
import { brandList } from '../data/brands'
import { productList } from '../data/products';
import { connect } from 'react-redux';
import { fetchData } from '../data/fetchData';

const Filters = (props) => {
  const {activeBrand, activeProduct} = props;
  
  if (activeProduct && activeBrand) {
      fetchData(activeProduct, activeBrand);
  }
  return (
    <div className="container m-5">
      <div className="row justify-content-center">
        <div className="col-2">
          <Dropdown filter="PRODUCT" options={productList} triggerText={ activeProduct || "Product"} />
        </div>
        <div className="col-2">
          <Dropdown filter="BRAND" options={brandList} triggerText={ activeBrand || "Brand"} />
        </div>
      </div>
    </div>
  );
};

function mapStateToProps(state) {
    return {
      activeProduct: state.product,
      activeBrand: state.brand
    };
  }
  
  export default connect(mapStateToProps)(Filters);
  
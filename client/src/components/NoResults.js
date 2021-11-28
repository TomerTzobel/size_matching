import React from "react";
import { connect } from "react-redux";

const NoResults = (props) => {
  const { searchResult } = props;

  return (
    <div className='m-5 p-5'>
    <h1 className='m-5 p-5'>{searchResult}</h1>
  </div>
);
};

function mapStateToProps(state) {
  return {
    searchResult: state.searchResult,
  };
}

export default connect(mapStateToProps)(NoResults);

import React from "react";
import { connect } from "react-redux";

const NoResults = (props) => {
  const { noResultsMessage } = props;

  return (
    <div className='m-5 p-5'>
    <h1 className='m-5 p-5'>{noResultsMessage}</h1>
  </div>
);
};

function mapStateToProps(state) {
  return {
    noResultsMessage: state.noResultsMessage,
  };
}

export default connect(mapStateToProps)(NoResults);

import React from "react";
import SearchBar from "./SearchBar";
import { Login } from "./Login";
import MySizes from "./MySizes";
import Cards from "./Cards";
import { connect } from "react-redux";

export const AppBody = (props) => {
  const { user } = props;
  return (
    <div>
      {!user && <Login />}
      {user && (
        <>
          <SearchBar />
          <Cards />
          <MySizes />
        </>
      )}
    </div>
  );
};

function mapStateToProps(state) {
  return {
    user: state.user,
  };
}

export default connect(mapStateToProps)(AppBody);

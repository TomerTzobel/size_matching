import React from "react";
import { ProgressBar, Container, Row, Col } from "react-bootstrap";
import { connect } from 'react-redux';

const RecommendedSize = (props) => {
  const { recommendedSize } = props; //todo - get from server
  return (
    <div>
      <Container
        fluid
        className="w-50 p-2 mt-3 mb-2 border border-secondary rounded bg-light"
      >
        <h2> We think the best size for you is: </h2>
        <Row>
          <Col> XS </Col>
          <Col> S </Col>
          <Col> M </Col>
          <Col> L </Col>
          <Col> XL </Col>
        </Row>
        <Row>
          <Col>
            <ProgressBar now={recommendedSize} />
          </Col>
        </Row>
      </Container>
    </div>
  );
};

function mapStateToProps(state) {
    return {
        recommendedSize: state.recommendedSize,
    };
  }
  
export default connect(mapStateToProps)(RecommendedSize);
  
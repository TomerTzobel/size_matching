import React from "react";
import { ProgressBar, Container, Row, Col } from "react-bootstrap";
import { connect } from 'react-redux';

const RecommendedSize = (props) => {
  const { recommendedSize } = props;

  if (recommendedSize === -1) {
    return (
      <h5>Unfortunately we don't have enough information to match your size</h5>
    )
  }
  return (
    <div>
      <Container
        fluid
        className="p-3 mt-3 mb-3 border border-secondary rounded bg-light"
      >
        <h4> Based on your shopping history, the best fit for you is: </h4>
        <Row className='mt-3 text-center'>
          <Col> XS </Col>
          <Col></Col>
          <Col> S </Col>
          <Col></Col>
          <Col> M </Col>
          <Col></Col>
          <Col> L </Col>
          <Col></Col>
          <Col> XL </Col>
        </Row>
        <Row className='mb-3'>
          <Col>
            <ProgressBar now={recommendedSize}/>
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
  
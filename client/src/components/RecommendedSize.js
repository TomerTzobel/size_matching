import React from "react";
import { ProgressBar, Container, Row, Col } from "react-bootstrap";
import { connect } from 'react-redux';

const RecommendedSize = (props) => {
  const { recommendedSize } = props; //todo - get from server
  return (
    <div>
      <Container
        fluid
        className="w-50 p-2 mt-3 mb-3 border border-secondary rounded bg-light"
      >
        <h3> Based on your shopping history, we think the best fit for you is: </h3>
        <Row className='mt-3'>
          <Col> XS </Col>
          <Col> S </Col>
          <Col> M </Col>
          <Col> L </Col>
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
  
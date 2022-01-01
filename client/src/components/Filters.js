import React from "react";
import { Dropdown } from "./Dropdown";
import { productList } from "../data/products";
import { connect } from "react-redux";
import { Container, Row, Col } from "react-bootstrap";
import { getBrandsByProductType } from "../utils/getBrandsByProductType";

const Filters = (props) => {
  const { activeBrand, activeProduct } = props;

  return (
    <Container className="mt-3">
      <Row>
        <Col md={7} lg={7} sm={7} xl={7} xxl={7}>
          <Row>
            <Col>
              <Dropdown
                filter="PRODUCT"
                options={productList}
                triggerText={activeProduct || "Product"}
              />
            </Col>
            <Col>
              <Dropdown
                filter="BRAND"
                options={getBrandsByProductType(activeProduct)}
                triggerText={activeBrand || "Brand"}
              />
            </Col>
          </Row>
        </Col>

        <Col md={5} lg={5} sm={5} xl={5} xxl={5}></Col>
      </Row>
    </Container>
  );
};

function mapStateToProps(state) {
  return {
    activeProduct: state.product,
    activeBrand: state.brand,
  };
}

export default connect(mapStateToProps)(Filters);

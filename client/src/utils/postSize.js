import axios from "axios";
import { selectUsername, selectUserSizes } from "../selectors";

export const postSizesOnRegister = () => {
  const sizes = selectUserSizes();
  console.log(sizes);
  sizes.forEach(({ product, brand, size }) => {
    postSize(product, brand, size);
  });
};

export const postSize = (product, brand, size) => {
  const username = selectUsername();
  const record = {
    username,
    product,
    brand,
    size,
  };
  axios.post("http://localhost:5000/addsize", record);
};

//todo - test
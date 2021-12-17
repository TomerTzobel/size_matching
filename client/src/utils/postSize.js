import axios from "axios";
import { selectUsername, selectUserSizes } from "../selectors";

export const postSizesOnRegister = () => {
  const sizes = selectUserSizes();
  sizes.forEach(({ product, brand, size }) => {
    postSize(product, brand, size);
  });
};

export const postSize = (product, brand, size) => {
  const username = selectUsername();
  const record = {
    username,
    type: product,
    brand,
    size,
  };
  axios.post("http://localhost:5000/add", record);
};


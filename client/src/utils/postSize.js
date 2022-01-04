import axios from "axios";
import { selectUsername } from "../selectors";

export const postSize = (product, brand, size, newUsername = null) => {
  const username = newUsername ? newUsername : selectUsername();
  const record = {
    username,
    type: product,
    brand,
    size,
  };
  axios.post("http://localhost:5000/add", record);
};


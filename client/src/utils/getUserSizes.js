import { store } from "../store";
import axios from "axios";

export const getUserSizes = async (username) => {
  const { data } = await axios.get(`http://localhost:5000/history/${username}`);
  const sizeHistory = Object.values(data).map((element) => {
    return {
      product: element.type,
      brand: element.brand,
      size: element.size,
    };
  });
  console.log(sizeHistory);
  store.dispatch({
    type: "SET_SIZES",
    payload: sizeHistory,
  });
};

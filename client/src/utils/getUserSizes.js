import { store } from '../store';
import axios from "axios";

export const getUserSizes = async (username) => {
    const { data } = await axios.get(`http://localhost:5000/history/${username}`);
    Object.values(data).forEach(element => {
        store.dispatch({
            type: "ADD_SIZE",
            payload: {
              product: element.type,
              brand: element.brand,
              size: element.size,
            },
          });
    });
}
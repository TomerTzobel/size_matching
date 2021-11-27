import axios from "axios";
import { selectUserSizes } from "../selectors";
import { store } from '../store';
import { itemsList } from "../data/items";

export const fetchData = async (product, brand) => {
    try {
        const { data } = await axios.get(`http://localhost:5000/cards/${product}/${brand}`);
        store.dispatch({type: "SET_ITEMS", payload: data})
    } catch {
        store.dispatch({type: "SET_ITEMS", payload: itemsList} )
    }
    try {

        const response = await axios.get("http://localhost:5000", {
            params: {
                brand,
                product,
                userSizes: selectUserSizes()
            }
        });
        store.dispatch({type: "SET_RECOMMENDATION", payload: response.data})
    } catch {
        store.dispatch({type: "SET_RECOMMENDATION", payload: 60})
    }
}
import axios from "axios";
import { selectUsername, selectActiveCart} from "../selectors";
import { store } from '../store';

export const getRecommendation = async () => {
    try {
        const { product, brand } = selectActiveCart();
        const user = selectUsername();
        let { data } = await axios.get(`http://localhost:5000/recommend/${user}/${brand}/${product}`);
        store.dispatch({type: "SET_RECOMMENDATION", payload: data})
    } catch {
        store.dispatch({type: "SET_RECOMMENDATION", payload: 55})
    }
};

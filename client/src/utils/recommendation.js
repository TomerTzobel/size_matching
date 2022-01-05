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
        store.dispatch({type: "SET_RECOMMENDATION", payload: -1})
    }
};

export const getRoundedSize = (size) => {
    if (size < 12.5) {
        return 'XS'
    }
    if (size < 37.5) {
        return 'S'
    }
    if (size < 62.5) {
        return 'M'
    }
    if (size < 85.5) {
        return 'L'
    }
    return 'XL'
}
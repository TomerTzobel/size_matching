import axios from "axios";
import { selectUsername, selectActiveCart} from "../selectors";
import { store } from '../store';

export const getRecommendation = async () => {
    try {
        const { product, brand } = selectActiveCart();
        const user = selectUsername();
        let { data } = await axios.get(`http://localhost:5000/recommend/${user}/${brand}/${product}`);
        if (data === 0){ // todo - remove when server returns a num
            data = Math.floor(Math.random() * 100);
        }
        store.dispatch({type: "SET_RECOMMENDATION", payload: data})
    } catch {
        store.dispatch({type: "SET_RECOMMENDATION", payload: 55})
    }
};

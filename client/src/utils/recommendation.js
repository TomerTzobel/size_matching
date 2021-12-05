import axios from "axios";
import { selectUsername, selectActiveCart} from "../selectors";
import { store } from '../store';

export const getRecommendation = async () => {
    try {
        const { product, brand } = selectActiveCart();
        const user = selectUsername();
        console.log(`recommend product ${product}, brand ${brand}, user: ${user}`);
        let { data } = await axios.get(`http://localhost:5000/recommend/${brand}/${product}`);
        console.log(data);
        if (data === 0){ // todo - remove when server returns a num
            data = Math.floor(Math.random() * 100);
        }
        store.dispatch({type: "SET_RECOMMENDATION", payload: data})
    } catch {
        store.dispatch({type: "SET_RECOMMENDATION", payload: 55})
    }
};

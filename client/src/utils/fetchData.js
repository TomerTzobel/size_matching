import axios from "axios";
import { store } from '../store';

export const fetchProductAndBrand = async (product, brand) => {
    try {
        const { data } = await axios.get(`http://localhost:5000/get/${brand}/${product}`);
        const items = Object.values(data).map(item => ({
            brand: item.Brand,
            product: item.Type,
            imgUrl: item.imgURL,
            name: item.Name
        }));
        if (items.length) {
            store.dispatch({type: "SET_ITEMS", payload: items});
        } else {
            store.dispatch({ type: "SET_NOT_FOUND" });
            store.dispatch({type: "SET_ITEMS", payload: []} );
        }
    } catch {
        store.dispatch({type: "SET_ITEMS", payload: []} )
    }
}

export const fetchProduct = async (product) => {
    try {
        const { data } = await axios.get(`http://localhost:5000/get/${product}`);
        const items = Object.values(data).map(item => ({
            brand: item.Brand,
            product: item.Type,
            imgUrl: item.imgURL,
            name: item.Name
        }));
        store.dispatch({type: "SET_ITEMS", payload: items});
    } catch {
        store.dispatch({type: "SET_ITEMS", payload: []} )
    }
}

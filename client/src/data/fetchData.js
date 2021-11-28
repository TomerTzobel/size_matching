import axios from "axios";
import { store } from '../store';

export const fetchData = async (product, brand) => {
    try {
        const { data } = await axios.get(`http://localhost:5000/get/${brand}/${product}`);
        const items = Object.values(data).map(item => ({
            brand: brand,
            imgUrl: item.imgURL,
            name: item.Name
        }));
        store.dispatch({type: "SET_ITEMS", payload: items});
    } catch {
        store.dispatch({type: "SET_ITEMS", payload: []} )
    }
    try {
        let { data } = await axios.get(`http://localhost:5000/recommend/${brand}/${product}`);
        console.log(data);
        if (data === 0){ // todo - remove when server returns a num
            data = Math.floor(Math.random() * 100);
        }
        store.dispatch({type: "SET_RECOMMENDATION", payload: data})
    } catch {
        store.dispatch({type: "SET_RECOMMENDATION", payload: 55})
    }
}
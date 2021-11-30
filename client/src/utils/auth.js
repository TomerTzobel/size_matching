import { store } from '../store';
import axios from "axios";


export const authenticate = async (username, password) => {
    try {
        const { data } = await axios.get('http://localhost:5000/login', {
            params: {
                username,
                password
            }
        });
        if (data === 1){ 
            store.dispatch({ type: 'SET_USER', payload: username })
            return true;
        } else {
            return false;
        }
    } catch {
        return false;
    }
}
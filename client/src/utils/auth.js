import { store } from '../store';
import axios from "axios";
import { getUserSizes } from './getUserSizes';

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
            getUserSizes(username);
            return true;
        } else {
            return false;
        }
    } catch {
        return false;
    }
}
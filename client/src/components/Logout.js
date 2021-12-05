import React from 'react'
import { Button } from 'react-bootstrap';
import { useDispatch } from 'react-redux';

export default function Logout() {
    const dispatch = useDispatch();

    const onLogOut = () => {
        dispatch({ type: 'SET_USER', payload: "" });
        dispatch({ type: 'SET_CART', payload: {} });
        dispatch({ type: 'SET_BRAND', payload: "" });
        dispatch({ type: 'SET_PRODUCT', payload: "" });
        dispatch({ type: 'SET_ITEMS', payload: [] });
        dispatch({ type: 'SET_EMPTY_SEARCH' });
        dispatch({ type: 'SET_SEARCH', payload: { text: "" }});
        dispatch({ type: 'RESET_SIZES' });       
    }

    return (
        <Button variant="outline-dark" size="sm" className="position-absolute top-0 end-0" onClick={onLogOut}>log out</Button>
    )
}

import React from 'react'
import { Button } from 'react-bootstrap';
import { useDispatch } from 'react-redux';

export default function Logout() {
    const dispatch = useDispatch();

    return (
        <Button variant="outline-dark" size="sm" className="position-absolute top-0 end-0" onClick={()=>{dispatch({ type: 'SET_USER', payload: "" })}}>log out</Button>
    )
}

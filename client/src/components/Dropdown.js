import React from 'react'
import { useDispatch } from 'react-redux';

export const Dropdown = (props) => {
    const { filter, options, triggerText }  = props;
    const dispatch = useDispatch();
    const onFilter = (payload) => dispatch({type: `SET_${filter}`, payload})

    return (
        <div>
            <div className="dropdown">
            <button className="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                {triggerText}
            </button>
            <ul className="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                {options.map((item) => (
                    <li key={item}>
                        <button className="dropdown-item" type="button" onClick={()=>onFilter(item)}>{item}</button>
                    </li>
                ))}
            </ul>
            </div>
        </div>
    )
}


import { store } from '../store';


export const selectBrand = () => store.getState().brand;

export const selectProduct = () => store.getState().product;

export const selectUserSizes = () => store.getState().userSizes;

export const selectUsername = () => store.getState().user;

export const selectActiveCart = () => store.getState().activeCart;

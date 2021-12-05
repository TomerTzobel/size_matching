
export default function activeCart(state = {}, action) {
    switch (action.type) {
      case 'SET_CART':
          return action.payload;
      default:
        return state
    }
  }
  
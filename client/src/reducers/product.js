
export default function product(state = "", action) {
    switch (action.type) {
      case 'SET_PRODUCT':
          return action.payload;
      default:
        return state
    }
  }
  
export default function items(state = [], action) {
    switch (action.type) {
      case 'SET_ITEMS':
        return action.payload
      default:
        return state
    }
  }
  
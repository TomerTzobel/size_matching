export default function items(state = [], action) {
    switch (action.type) {
      case 'SET_ITEMS':
        return action.payload
      case 'ITEMS_NOT_FOUND':
        return []
      default:
        return state
    }
  }
  
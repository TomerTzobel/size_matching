
export default function userSizes(state = [], action) {
    switch (action.type) {
      case 'ADD_SIZE':
          return state.concat([{ ...action.payload }]);
      default:
        return state
    }
  }
  
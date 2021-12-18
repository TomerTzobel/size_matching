
export default function userSizes(state = [], action) {
    switch (action.type) {
      case 'ADD_SIZE':
          return state.concat([{ ...action.payload }]);
      case 'SET_SIZES':
          return action.payload;
      case 'RESET_SIZES':
          return [];
      default:
        return state
    }
  }
  
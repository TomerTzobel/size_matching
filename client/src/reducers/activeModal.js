export default function activeModal(state = "", action) {
    switch (action.type) {
      case 'BUY_MODAL':
        return 'buy';
      case 'REGISTER_MODAL':
        return 'register';
      case 'FEEDBACK_MODAL':
        return 'feedback';
      case 'HIDE_MODAL':
        return "";
      default:
        return state
    }
  }
  
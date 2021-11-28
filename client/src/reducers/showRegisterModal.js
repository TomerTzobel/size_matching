export default function showRegisterModal(state = false, action) {
    switch (action.type) {
      case 'SHOW_REGISTER':
        return true;
      case 'HIDE_REGISTER':
        return false;
      default:
        return state
    }
  }
  
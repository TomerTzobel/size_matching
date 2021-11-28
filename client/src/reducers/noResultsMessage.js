
export default function noResultsMessage(state = "Start searching and shopping", action) {
    switch (action.type) {
      case 'SET_NOT_FOUND':
          return "Oops, we can't find any match. Please try another search";
      case 'SET_EMPTY_SEARCH':
            return "Start searching and shopping";
      default:
        return state
    }
  }
  
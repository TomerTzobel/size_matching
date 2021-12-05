import { combineReducers } from 'redux'
import activeModal from './activeModal'
import items from './items'
import userSizes from './userSizes'
import brand from './brand'
import product from './product'
import recommendedSize from './recommendedSize'
import searchText from './searchText'
import user from './user'
import noResultsMessage from './noResultsMessage'
import activeCart from './activeCart'

export default combineReducers({
  activeModal,
  items,
  userSizes,
  brand,
  product,
  recommendedSize,
  searchText,
  user,
  noResultsMessage,
  activeCart,
})

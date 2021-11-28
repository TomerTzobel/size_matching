import { combineReducers } from 'redux'
import showModal from './showModal'
import items from './items'
import userSizes from './userSizes'
import brand from './brand'
import product from './product'
import recommendedSize from './recommendedSize'
import searchText from './searchText'
import user from './user'
import showRegisterModal from './showRegisterModal'

export default combineReducers({
  showModal,
  items,
  userSizes,
  brand,
  product,
  recommendedSize,
  searchText,
  user,
  showRegisterModal,
})

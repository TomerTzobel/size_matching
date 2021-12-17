import axios from "axios";

export const registerNewUser = async (username, password) => {
  const record = {
    username,
    password,
  };
  const { data } = await axios.post("http://localhost:5000/login", record);
  if (data === 0){
    return true
  }
  return false;
};

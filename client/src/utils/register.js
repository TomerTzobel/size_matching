import axios from "axios";

export const registerNewUser = (username, password) => {
  const record = {
    username,
    password,
  };
  axios.post("http://localhost:5000/register", record);
};

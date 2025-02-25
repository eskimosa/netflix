import baseUrl from "../components/shared/baseUrl";
import axios from "axios";

const LOGIN_URL = `${baseUrl}/auth/token/`;
const SIGNUP_URL = `${baseUrl}/auth/signup/`;
const REFRESH_URL = `${baseUrl}/auth/token/refresh`;

export const login = async (email, password) => {
  try {
    const response = await axios.post(
      LOGIN_URL,
      { email: email, passwped: password },
      { withCredentials: true }
    );
    return response.data.success;
  } catch (error) {
    console.error("Login failed:", error);
    return false;
  }
};
/* 
export const refsresh_token = () => {
  const response = axios.post(REFRESH_URL, { withCredentials: true });
  return response.data;
};

call_refresh = async (error, func) => {
  if (error.response && error.response.status == 401) {
    const tokenRefreshed = await refsresh_token();

    if (tokenRefreshed) {
      const retryResponse = await func();
      return retryResponse.data;
    }
  }
  return false;
};
 */
export const signup = async (email, password) => {
  try {
    const response = await axios.post(
      SIGNUP_URL,
      { email: email, passwped: password },
      { withCredentials: true }
    );
    return response.data.success;
  } catch (error) {
    console.error("Signup failed:", error);
    return false;
  }
};

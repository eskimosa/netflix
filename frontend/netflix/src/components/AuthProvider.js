import { useState, useEffect, useContext, createContext } from "react";
import axiosInstance from "./axiosConfig";

const AuthContext = createContext();

export function useAuth() {
  return useContext(AuthContext);
}

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  const login = async (username, password) => {
    try {
      const response = await axiosInstance.post("/auth/login/", {
        username,
        password,
      });
      const token = response.data.access; // JWT token from backend response

      localStorage.setItem("token", token);

      // Decode JWT to extract user information if needed
      const userInfo = parseJwt(token);
      setUser(userInfo);
    } catch (error) {
      console.error("Login failed:", error);
    }
  };

  const signup = async (username, email, password, password2) => {
    try {
      const response = await axiosInstance.post("/auth/signup/", {
        username,
        email,
        password,
        password2,
      });
      const token = response.data.access;

      localStorage.setItem("token", token);

      const userInfo = parseJwt(token);
      setUser(userInfo);
    } catch (error) {
      console.error("Login failed:", error);
    }
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem("token");
  };

  // Auto-login on app start (if token exists in localStorage)
  useEffect(() => {
    try {
      const token = localStorage.getItem("token");
      if (token) {
        const userInfo = parseJwt(token);
        setUser(userInfo);
      }
    } catch (error) {
      console.error("Error parsing token:", error);
      logout();
    }
    setLoading(false);
  }, []);

  // JWT Parsing
  const parseJwt = (token) => {
    try {
      const base64Url = token.split(".")[1];
      const base64 = base64Url.replace(/-/g, "+").replace(/_/g, "/");
      const jsonPayload = decodeURIComponent(
        atob(base64)
          .split("")
          .map(function (c) {
            return "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2);
          })
          .join("")
      );

      return JSON.parse(jsonPayload);
    } catch (e) {
      return null;
    }
  };

  return (
    <AuthContext.Provider value={{ user, signup, login, logout }}>
      {!loading && children}
    </AuthContext.Provider>
  );
}

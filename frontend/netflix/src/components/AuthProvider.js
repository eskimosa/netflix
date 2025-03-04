import { useState, useEffect, useContext, createContext } from "react";
import api from "./axiosConfig";

const AuthContext = createContext();

export function useAuth() {
  return useContext(AuthContext);
}

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const login = async (username, password) => {
    try {
      const response = await api.post("/auth/login/", {
        username,
        password,
      });

      const token = response.data.access; // JWT token from backend response

      localStorage.setItem("access_token", token);

      // Decode JWT to extract user information if needed
      const userInfo = parseJwt(token);
      setUser(userInfo);
      return response;
    } catch (error) {
      console.error("Login failed:", error);
      if (error.response) {
        // If there's a response (error from the backend)
        return {
          errorMessage: error.response.data.detail || "An error occurred.",
        };
      } else if (error.request) {
        // If there's no response (network error)
        return { errorMessage: "Network error, please try again later." };
      } else {
        return { errorMessage: "An unexpected error occurred." };
      }
    }
  };

  const signup = async (username, email, password, password2) => {
    try {
      const response = await api.post("/auth/signup/", {
        username,
        email,
        password,
        password2,
      });
      const token = response.data.access;

      localStorage.setItem("access_token", token);

      const userInfo = parseJwt(token);
      setUser(userInfo);
      return response;
    } catch (error) {
      console.error("Signup failed:", error);
      if (error.response) {
        return { errorMessage: error.response.data.detail || "An error occurred." };
      } else if (error.request) {
        return { errorMessage: "Network error, please try again later." };
      } else {
        return { errorMessage: "An unexpected error occurred." };
      }
    }
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem("access_token");
  };

  // Auto-login on app start (if token exists in localStorage)
  useEffect(() => {
    try {
      const token = localStorage.getItem("access_token");
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
    <AuthContext.Provider value={{ user, signup, login, logout, error }}>
      {!loading && children}
    </AuthContext.Provider>
  );
}

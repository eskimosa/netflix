import React from "react";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import baseUrl from "./shared/baseUrl";

const Navbar = () => {
  const username = localStorage.getItem("username");
  const token = localStorage.getItem("access_token");

  const navigate = useNavigate();

  const handleLogout = async () => {
    try {
        const refreshToken = localStorage.getItem("refresh_token");
        if (refreshToken) {
            await axios.post(`${baseUrl}/auth/logout/`, {
                refresh: refreshToken
            });
        }
            localStorage.removeItem('access_token');
            localStorage.removeItem('refresh_token');
            localStorage.removeItem('username');

            navigate('/');

        } catch (error) {
            console.error(error.response ? error.response.data : error.message);
            if (error.response && error.response.data.detail === "Token is invalid or expired") {
                alert("Session expired, please log in again.");

                navigate("/");
            } else {
                console.error(error.response ? error.response.data : error.message);
            }
        }
    };

  return (
    <div className="flex items-center justify-between p-4 z-[100] w-full absolute">
      <Link to="/">
        <h1 className="text-red-600 text-4xl font-bold cursor-pointer">
          NETFLIX
        </h1>
      </Link>
      <div>
        {token ? (
          <>
            <button className="text-white pr-4" onClick={handleLogout}>
              Logout
            </button>
            <Link to="/account">
              <button className="bg-red-600 px-6 py-2 rounded cursor-pointer text-white">
                Account
              </button>
            </Link>
          </>
        ) : (
          <>
            <Link to="/login">
              <button className="text-white pr-4">Sign In</button>
            </Link>
            <Link to="/signup">
              <button className="bg-red-600 px-6 py-2 rounded cursor-pointer text-white">
                Sign Up
              </button>
            </Link>
          </>
        )}
      </div>
    </div>
  );
};

export default Navbar;

import React from "react";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../components/AuthProvider";

const NavbarAuth = () => {
  const { user, logout } = useAuth();

  const navigate = useNavigate();

  const handleLogout = async (e) => {
    e.preventDefault();
    await logout();
    navigate("/");
  };

  return (
    <div className="flex items-center justify-between p-4 z-[100] w-full absolute">
      <Link to="/">
        <h1 className="text-red-600 text-4xl font-bold cursor-pointer">
          NETFLIX
        </h1>
      </Link>
      <div>
        {user ? (
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

export default NavbarAuth;

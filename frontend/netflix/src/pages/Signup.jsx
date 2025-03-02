import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import baseUrl from "../components/shared/baseUrl";
import axios from "axios";

const Signup = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [password2, setPassword2] = useState("");
  const navigate = useNavigate();

  const handleSignup = async (e) => {
    e.preventDefault();
        if (password !== password2) {
            alert('Passwords do not match');
            return;
        }
        console.log('Submitting sign-up form with data:', { username, email, password, password2 });
        try {
            const response = await axios.post(`${baseUrl}/auth/signup/`, {
                username: username,
                password: password,
                password2: password2,
                email: email,
            });
            await axios.post(`${baseUrl}/auth/login/`, {
                username: username,
                password: password,
        });

        localStorage.setItem('access_token', response.data.access);
        localStorage.setItem('refresh_token', response.data.refresh);
        localStorage.setItem("username", username);

        setPassword('');
        setPassword2('');

        navigate('/');
        } catch (error) {
            console.error(error.response.data);
        }
    };

  return (
    <>
      <div className="w-full h-screen">
        <img
          className="hidden sm:block absolute w-full h-full object-cover"
          src="./assets/banner.jpg"
          alt="/"
        />
        <div className="bg-black/60 fixed top-0 left-0 w-full h-screen"></div>
        <div className="fixed w-full px-4 py-24 z-50">
          <div className="max-w-[450px] h-[600px] mx-auto bg-black/75 text-white">
            <div className="max-w-[320px] mx-auto py-16">
              <h1 className="text-3xl font-bold">Sign Up</h1>
              <form className="w-full flex flex-col py-4">
                <input
                  className="p-3 my-2 bg-gray-700 rounded"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  type="username"
                  placeholder="Username"
                  autoComplete="username"
                />
                <input
                  className="p-3 my-2 bg-gray-700 rounded"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  type="email"
                  placeholder="Email"
                  autoComplete="email"
                />
                <input
                  className="p-3 my-2 bg-gray-700 rounded"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  type="password"
                  placeholder="Password"
                  autoComplete="current-password"
                />
                <input
                  className="p-3 my-2 bg-gray-700 rounded"
                  value={password2}
                  onChange={(e) => setPassword2(e.target.value)}
                  type="password2"
                  placeholder="Repeat Password"
                  autoComplete="current-password"
                />
                <button
                  className="bg-red-600 py-3 my-6 rounded font-bold"
                  onClick={handleSignup}
                >
                  Sign Up
                </button>
                <div className="flex justify-between items-center text-sm text-gray-600">
                  <p>
                    <input className="mr-2" type="checkbox" />
                    Remember me
                  </p>
                  <p>Need help?</p>
                </div>
                <p className="py-8">
                  <span className="text-gray-600">
                    Already subscribed to Netflix?
                  </span>{" "}
                  <Link to="/login">Sign In</Link>{" "}
                </p>
              </form>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Signup;

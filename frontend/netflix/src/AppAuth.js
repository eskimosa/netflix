import { Route, Routes } from "react-router-dom";
import NavbarAuth from "./pages/NavbarAuth";
import HomeAuth from "./pages/HomeAuth";
import SignupAuth from "./pages/SignupAuth";
import LoginAuth from "./pages/LoginAuth";
import { AuthProvider } from "./components/AuthProvider";

function AppAuth() {
  return (
    <>
      <AuthProvider>
        <NavbarAuth />
        <Routes>
          <Route path="/" element={<HomeAuth />} />
          <Route path="/login" element={<LoginAuth />} />
          <Route path="/signup" element={<SignupAuth />} />
        </Routes>
      </AuthProvider>
    </>
  );
}

export default AppAuth;

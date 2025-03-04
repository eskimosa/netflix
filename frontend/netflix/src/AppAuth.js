import { Route, Routes } from "react-router-dom";
import NavbarAuth from "./components/NavbarAuth";
import HomeAuth from "./pages/HomeAuth";
import SignupAuth from "./pages/SignupAuth";
import LoginAuth from "./pages/LoginAuth";
import Account from "./pages/Account";
import { AuthProvider } from "./components/AuthProvider";
import ProtectedRoute from "./components/ProtectedRoute";

function AppAuth() {
  return (
    <>
      <AuthProvider>
        <NavbarAuth />
        <Routes>
          <Route path="/" element={<HomeAuth />} />
          <Route path="/login" element={<LoginAuth />} />
          <Route path="/signup" element={<SignupAuth />} />
          <Route
            path="/account"
            element={
              <ProtectedRoute>
                <Account />
              </ProtectedRoute>
            }
          />
        </Routes>
      </AuthProvider>
    </>
  );
}

export default AppAuth;

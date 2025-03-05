import { Route, Routes } from "react-router-dom";
import NavbarAuth from "./components/Navbar";
import HomeAuth from "./pages/Home";
import SignupAuth from "./pages/Signup";
import LoginAuth from "./pages/Login";
import Account from "./pages/Account";
import { AuthProvider } from "./components/AuthProvider";
import ProtectedRoute from "./components/ProtectedRoute";

function App() {
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

export default App;

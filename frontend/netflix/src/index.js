import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import AppAuth from "./AppAuth";
import { BrowserRouter as Router } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(

    <Router>
      <AppAuth />
    </Router>

);

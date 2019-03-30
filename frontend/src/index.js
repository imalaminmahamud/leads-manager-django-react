// Built in & Third Party Library Components
import React from "react";
import ReactDOM from "react-dom";

// Custom Components
import App from "./components/App";

// Stylesheets
// import "./index.css";

const wrapper = document.getElementById("root");
wrapper ? ReactDOM.render(<App />, wrapper) : null;

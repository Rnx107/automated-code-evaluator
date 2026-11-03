import "./App.css";
import Login from "./pages/login";
import Signup from "./pages/signup";

export default function App() {
  return window.location.pathname === "/signup" ? <Signup /> : <Login />;
}
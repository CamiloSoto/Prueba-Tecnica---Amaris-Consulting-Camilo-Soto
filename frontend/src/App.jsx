import React from "react";

import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";

import FundsPage from "./pages/FundsPage";
import SubscribePage from "./pages/SubscribePage";

const App = () => {
  return (
    <React.Fragment>
      <Router>
        <nav className="bg-blue-600 p-4 text-white flex justify-between">
          <div className="font-bold">Plataforma de Fondos</div>
          <div className="space-x-4">
            <Link to="/">Fondos</Link>
            <Link to="/subscribe">Suscribirse</Link>
          </div>
        </nav>
        <Routes>
          <Route path="/" element={<FundsPage />} />
          <Route path="/subscribe" element={<SubscribePage />} />
        </Routes>
      </Router>
    </React.Fragment>
  );
};

export default App;

import React from "react";

import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";

import SubscribePage from "./pages/SubscribePage";
import HistoryPage from "./pages/HistoryPage";
import FundsPage from "./pages/FundsPage";

const App = () => {
  return (
    <React.Fragment>
      <Router>
        <nav className="bg-blue-600 p-4 text-white flex justify-between">
          <div className="font-bold">Plataforma de Fondos</div>
          <div className="space-x-4">
            <Link to="/">Fondos</Link>
            <Link to="/subscribe">Suscribirse</Link>
            <Link to="/history">Historial</Link>
          </div>
        </nav>
        <Routes>
          <Route path="/" index element={<FundsPage />} />
          <Route path="/subscribe" element={<SubscribePage />} />
          <Route path="/history" element={<HistoryPage />} />
        </Routes>
      </Router>
    </React.Fragment>
  );
};

export default App;

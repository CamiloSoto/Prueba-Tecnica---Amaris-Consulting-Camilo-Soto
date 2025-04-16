import React, { useEffect } from "react";
import useFunds from "../hooks/useFunds";

const FundsPage = () => {
  const { funds, errors, getFunds } = useFunds();

  // eslint-disable-next-line react-hooks/exhaustive-deps
  useEffect(() => getFunds, []);
  return (
    <React.Fragment>
      <div className="p-8">
        {errors ? (
          <div
            class="bg-red-100 border border-red-300 text-red-800 px-4 py-3 rounded relative"
            role="alert"
          >
            <strong class="font-bold">Error: </strong>
            <span class="block sm:inline">{errors}</span>
          </div>
        ) : null}
        <h1 className="text-2xl font-bold mb-4">Fondos Disponibles</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {funds.map((fund) => (
            <div key={fund.id} className="bg-white p-4 rounded-xl shadow">
              <h2 className="text-lg font-semibold">{fund.nombre}</h2>
              <p className="text-sm">Categoría: {fund.categoria}</p>
              <p className="text-sm text-gray-700">
                Monto mínimo:{" "}
                <strong>COP ${fund.monto_minimo.toLocaleString()}</strong>
              </p>
            </div>
          ))}
        </div>
      </div>
    </React.Fragment>
  );
};

export default FundsPage;

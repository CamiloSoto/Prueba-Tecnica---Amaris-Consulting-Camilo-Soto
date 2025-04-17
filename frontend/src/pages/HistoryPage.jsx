import React from "react";
import useHistory from "../hooks/useHistory";

const HistoryPage = () => {
  const { history, err, values, handleChange, handleSubmit } = useHistory();
  return (
    <React.Fragment>
      <div className="p-8">
        <h1 className="text-2xl font-bold mb-6">Historial de Transacciones</h1>
        <form onSubmit={handleSubmit}>
          <div className="max-w-md space-y-4">
            <input
              type="text"
              placeholder="ID del Cliente"
              value={values.clienteId}
              name="clienteId"
              id=""
              onChange={handleChange}
              className="w-full border rounded px-3 py-2"
            />
            <button
              type="submit"
              className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
            >
              Buscar
            </button>

            {err ? <p className="text-red-600">{err}</p> : null}

            {history.length > 0 && (
              <div className="mt-6 space-y-4">
                {history.map((item) => (
                  <div key={item.id} className="border p-4 rounded shadow-sm">
                    <p>
                      <strong>Tipo:</strong> {item.tipo}
                    </p>
                    <p>
                      <strong>Fondo ID:</strong> {item.fondo_id}
                    </p>
                    <p>
                      <strong>Monto:</strong> COP ${item.monto.toLocaleString()}
                    </p>
                    <p>
                      <strong>Fecha:</strong>{" "}
                      {new Date(item.fecha).toLocaleString()}
                    </p>
                    <p>
                      <strong>Notificado por:</strong> {item.notificado_por}
                    </p>
                  </div>
                ))}
              </div>
            )}
          </div>
        </form>
      </div>
    </React.Fragment>
  );
};

export default HistoryPage;

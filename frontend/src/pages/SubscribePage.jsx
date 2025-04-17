import React, { useEffect } from "react";
import useSubscribe from "../hooks/useSubscribe";
import useFunds from "../hooks/useFunds";

const SubscribePage = () => {
  const { message, values, handleChange, handleSubmit } = useSubscribe();
  const { funds, getFunds } = useFunds();

  // eslint-disable-next-line react-hooks/exhaustive-deps
  useEffect(() => getFunds, []);

  return (
    <React.Fragment>
      <div className="p-8">
        <h1 className="text-2xl font-bold mb-6">Suscribirse a un Fondo</h1>
        <form onSubmit={handleSubmit} className="space-y-4 max-w-md">
          <div>
            <label className="block font-medium">ID del Cliente</label>
            <input
              type="text"
              id="clienteId"
              name="clienteId"
              value={values.clienteId}
              onChange={handleChange}
              className="w-full border rounded px-3 py-2"
              required
            />
          </div>
          <div>
            <label className="block font-medium">Seleccionar Fondo</label>
            <select
              className="w-full border rounded px-3 py-2"
              value={values.fondoId}
              id="fondoId"
              name="fondoId"
              onChange={handleChange}
              required
            >
              <option value="">-- Selecciona un fondo --</option>
              {funds.map((fondo) => (
                <option key={fondo.id} value={fondo.id}>
                  {fondo.nombre} (COP ${fondo.monto_minimo.toLocaleString()})
                </option>
              ))}
            </select>
          </div>
          <div>
            <label className="block font-medium">Medio de Notificación</label>
            <select
              className="w-full border rounded px-3 py-2"
              value={values.notification}
              name="notification"
              id="notification"
              onChange={handleChange}
            >
              <option value="email">Email</option>
              <option value="sms">SMS</option>
            </select>
          </div>
          <button
            type="submit"
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            Suscribirse
          </button>
        </form>

        {message && (
          <div className="mt-6 p-4 border rounded bg-gray-50 text-sm">
            {message}
          </div>
        )}
      </div>
    </React.Fragment>
  );
};

export default SubscribePage;

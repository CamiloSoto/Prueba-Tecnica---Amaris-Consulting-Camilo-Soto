import { useFormik } from "formik";
import { useState } from "react";
import * as Yup from "yup";
import axiosClient from "../config/axiosClient";

const useSubscribe = () => {
  const [message, setMessage] = useState("");
  const subscribeFrm = useFormik({
    initialValues: {
      fondoId: "",
      clienteId: "",
      notification: "",
    },
    validationSchema: Yup.object({
      fondoId: Yup.string().required("campo requerido"),
      clienteId: Yup.string().required("campo requerido"),
      notification: Yup.string().required("campo requerido"),
    }),
    onSubmit: async (values) => {
      setMessage("");
      const data = {
        cliente_id: values.clienteId,
        fondo_id: parseInt(values.fondoId),
        notificacion: values.notification,
      };

      await axiosClient
        .post("/funds/suscribir", data)
        .then((response) => {
          setMessage(`✅ Suscripción exitosa. ID: ${response.data.id}`);
        })
        .catch((err) => {
          setMessage(
            `❌ Error: ${err?.response?.data?.detail || "Algo salió mal"}`
          );
        });
      console.log(data);
    },
  });
  return { message, ...subscribeFrm };
};

export default useSubscribe;

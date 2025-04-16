import { useFormik } from "formik";
import { useState } from "react";
import * as Yup from "yup";
import axiosClient from "../config/axiosClient";

const useHistory = () => {
  const [err, setErr] = useState("");
  const [history, setHistory] = useState([]);

  const HistoryFrm = useFormik({
    initialValues: {
      clienteId: "",
    },
    validationSchema: Yup.object({
      clienteId: Yup.string().required("Campo requerido"),
    }),
    onSubmit: async (values) => {
      setErr("");
      setHistory([]);
      await axiosClient
        .get(`/historial/${values.clienteId}`)
        .then((response) => {
          setHistory(response.data);
        })
        .catch(() => {
          setErr("No se pudo obtener el historial.");
        });
    },
  });
  return { err, history, ...HistoryFrm };
};

export default useHistory;

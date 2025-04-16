import { useState } from "react";
import axiosClient from "../config/axiosClient";

const useFunds = () => {
  const [errors, setErrors] = useState("");

  const [funds, setFunds] = useState([]);

  const getFunds = async () => {
    await axiosClient
      .get("/funds/")
      .then((res) => {
        setFunds(res.data);
      })
      .catch(() => {
        setErrors("No se logró obtener los fondos");
        return null;
      });
  };
  return { funds, errors, getFunds };
};

export default useFunds;

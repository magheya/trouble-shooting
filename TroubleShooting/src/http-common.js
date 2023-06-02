import axios from "axios";

export default axios.create({
  baseURL: "http://localhost:8000/expert-system/",
  headers: {
    "Content-type": "application/json"
  }
});
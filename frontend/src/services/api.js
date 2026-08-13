import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const uploadFile = (formData) =>
  API.post("/upload", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

export const validateFiles = () =>
  API.post("/validate");

export const scanRepository = (repoUrl) =>
  API.post("/scan-repository", {
    repo_url: repoUrl,
  });

export default API;
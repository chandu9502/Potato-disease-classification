import "./App.css";
import React, { useState } from "react";
import axios from "axios";

function Test() {
  const [file, setFile] = useState();

  function handleChange(event) {
    setFile(event.target.files[0]);
  }

  function handleSubmit(event) {
    event.preventDefault();
    const url = "http://localhost:8000/predict";
    const formData = new FormData();
    console.log(file);
    formData.append("file", file);
    formData.append("fileName", file.name);
    console.log(formData);
    const config = {
      headers: {
        "content-type": "multsipart/form-data",
      },
    };
    axios.post(url, { formData, Boom: "Boom" }, config).then((response) => {
      console.log(response.data);
    });
  }

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <h1>React File Upload</h1>
        <input type="file" onChange={handleChange} />
        <button type="submit">Upload</button>
      </form>
    </div>
  );
}

export default Test;

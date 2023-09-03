import React, { useState } from "react";

const FaceDetection = () => {
  const [file, setFile] = useState(null);
  const [faces, setFaces] = useState([]);
  const [errorMessage, setErrorMessage] = useState("");

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    setFile(selectedFile);
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please select an image to upload.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://localhost:8000/upload/", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        setFaces(data.detected_faces); // Store base64-encoded images

        setErrorMessage("");
      } else {
        alert("Error uploading the image.");
      }
    } catch (error) {
      console.error("Error:", error);
      setErrorMessage("An error occurred while processing the request.");
    }
  };

  return (
    <div>
      <h1>Face Detection</h1>
      <input type="file" accept="image/*" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>

      {file && (
        <div>
          <h2>Uploaded Image</h2>
          <img src={URL.createObjectURL(file)} alt="Uploaded" width="300" />
        </div>
      )}

      {faces.length > 0 && (
        <div>
          <h2>Detected Faces</h2>
          <ul>
            {faces.map((base64Image, index) => (
              <li key={index}>
                {/* Create an image element with a Data URL */}
                <img
                  src={`data:image/png;base64,${base64Image}`}
                  alt={`Detected Face ${index + 1}`}
                  width="300"
                />
              </li>
            ))}
          </ul>
        </div>
      )}
      {errorMessage && <p className="error">{errorMessage}</p>}
    </div>
  );
};

export default FaceDetection;

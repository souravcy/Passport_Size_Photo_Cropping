from mtcnn import MTCNN
import cv2
import tempfile
from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import base64

app = FastAPI()

detector= MTCNN()
# Configure CORS to allow requests from your React frontend
app.add_middleware(
    CORSMiddleware,
    # Update with the actual origin of your frontend
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    # You can restrict HTTP methods if needed (e.g., ["GET", "POST"])
    allow_methods=["*"],
    allow_headers=["*"],  # You can restrict headers if needed
)

# ... Define your routes and handlers ...




# Apply the request body size limit middleware (e.g., limit to 100 MB)



@app.get("/")
def read_root():
    return {"message": "Welcome to the Face Detection API"}


@app.post("/upload/")
async def upload_file(file: UploadFile):
    try:
        # Save the uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(file.file.read())
            temp_file_path = temp_file.name

        # Load the uploaded image
        image = cv2.imread(temp_file_path)

        # Perform face detection using MTCNN
        faces = detector.detect_faces(image)

        detected_faces = []

        # Iterate through the detected faces
        for i, face in enumerate(faces):
            x, y, width, height = face['box']

            # Extract the face region
            face_region = image[y:y+height, x:x+width]

            # Encode the face image as base64
            _, encoded_image = cv2.imencode(".png", face_region)
            base64_image = base64.b64encode(encoded_image).decode("utf-8")

            detected_faces.append(base64_image)  # Store base64-encoded image

        return {"detected_faces": detected_faces}

    except Exception as e:
        return JSONResponse(content={"error": str(e)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)





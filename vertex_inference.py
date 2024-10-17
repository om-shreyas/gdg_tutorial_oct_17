import base64
import vertexai

from vertexai.generative_models import GenerativeModel, Part

PROJECT_ID = "shl-assigment"
vertexai.init(project=PROJECT_ID, location="us-central1")

model = GenerativeModel("gemini-1.5-flash-002")
last_image_data = None

def process_image(image_path):
    """Reads and encodes the image from the provided path."""
    global last_image_data

    with open(image_path, "rb") as f:
        image_data = f.read()

    last_image_data = base64.b64encode(image_data).decode("utf-8")
    
    return last_image_data

def query_image_model(base64_image, query):
    """Generates a response from the model based on the image and query."""
    response = model.generate_content(
        [
            Part.from_data(
                mime_type="image/jpeg",
                data=base64_image
            ),
            query,
        ]
    )
    return response.text

def chatbot_input(user_input):
    """Processes the user input and responds accordingly."""
    global last_image_data
    
    if user_input.startswith("image:"):
        image_path = user_input.split("image:", 1)[1].strip()
        print(image_path)
        try:
            process_image(image_path)
            return "Image successfully uploaded. Ask me anything about it!"
        except Exception as e:
            return f"Error processing the image: {str(e)}"
    
    elif last_image_data is not None:
        return query_image_model(last_image_data, user_input)
    
    else:
        return "Please upload an image first using 'image:<image_path>'."

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        break

    response = chatbot_input(user_input)
    print(f"Bot: {response}")
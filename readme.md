# Vertex AI Chatbot with Image Processing

This project demonstrates the integration of Google's Vertex AI with generative models, specifically using the **Gemini-1.5-Flash-002** model, to build an interactive chatbot. The chatbot supports both text-based interactions and image-based queries, making it versatile for a range of use cases.

## Features

- **Text-based Interaction**: Users can ask the chatbot any text-based questions and receive responses from the generative AI model.
- **Image-based Interaction**: Users can upload an image and ask questions about it, leveraging the power of AI to generate context-specific responses based on the provided image.

## Prerequisites

- Python 3.7+
- Google Cloud account with access to Vertex AI
- Installed Google Cloud SDK
- Enabled Vertex AI API in your project

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/vertex-ai-chatbot.git
   cd vertex-ai-chatbot
   ```

2. **Install dependencies**:
   ```bash
   pip install google-cloud-aiplatform
   ```

3. **Set up Google Cloud Project**:
   Ensure that the Vertex AI API is enabled in your Google Cloud project:
   - Visit [Google Cloud Console](https://console.cloud.google.com/vertex-ai).
   - Enable the **Vertex AI API**.

4. **Authenticate**:
   Use the Google Cloud SDK to authenticate and set your project:
   ```bash
   gcloud auth application-default login
   gcloud config set project <your-project-id>
   ```

5. **Modify Project Details**:
   Update the `PROJECT_ID` in the code to match your Google Cloud project:
   ```python
   PROJECT_ID = "your-google-cloud-project-id"
   ```

## Files

### `vertex_ai.py`

This script initializes the Vertex AI generative model and provides a simple text-based chatbot interface. Users can interact with the chatbot by typing questions, and the model will generate relevant responses.

### `vertex_inference.py`

This script allows the chatbot to process both images and text. Users can upload an image, and the model will generate responses based on both the image and the user's query.

**Usage**:
- To upload an image, use the command: `image:<image_path>`.
- After uploading an image, ask questions about the content of the image.

## Usage

1. **Text-based Chatbot**:
   Run the `vertex_ai.py` script for a basic text chatbot:
   ```bash
   python vertex_ai.py
   ```

   The chatbot will prompt you to ask questions:
   ```
   Welcome to the chatbot! Ask me anything. Type 'exit' to quit.
   You: <Your question>
   Chatbot: <Bot response>
   ```

2. **Image-based Chatbot**:
   Run the `vertex_inference.py` script to interact with both images and text:
   ```bash
   python vertex_inference.py
   ```

   Example usage:
   ```
   You: image:/path/to/your/image.jpg
   Bot: Image successfully uploaded. Ask me anything about it!
   You: What is shown in the image?
   Bot: <AI-generated response>
   ```

3. **Exit**:
   To exit either chatbot, type `exit`.

## Error Handling

- If the chatbot encounters an issue with processing the image or generating a response, it will notify the user with an error message and prompt for re-input.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with improvements.

## License

This project is licensed under the MIT License.
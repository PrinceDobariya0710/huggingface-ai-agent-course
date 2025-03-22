# AI Agent Course Exercises with Gemini

This repository contains exercises from Hugging Face's AI Agent Course, modified to use Google's Gemini API instead of Hugging Face's deployed models. This adaptation ensures that users can complete the exercises without worrying about API quota limitations that they might face with Hugging Face's models.

## Why Gemini?

- Free tier with generous limits
- Reliable performance
- Easy to set up and use
- Cost-effective for learning purposes

## Getting Started

### Setting up Google AI Studio API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)

2. Sign in with your Google account

3. Click on "Create API Key" button
   - If you don't have any existing API keys, you'll be prompted to create one
   - If you already have keys, you can find the "Create API Key" option in the settings

4. Copy your newly generated API key

5. Create a `.env` file in the root directory of this project and add your API key:
   ```
   GEMINI_API_KEY=your-api-key-here
   GOOGLE_API_KEY=your-api-key-here
   HF_TOKEN=your-api-key-here <Create API keys with write permissions on huggingface if you want to push models>
   LANGFUSE_PUBLIC_KEY=your-api-key-here
   LANGFUSE_SECRET_KEY=your-api-key-here
   SERPAPI_API_KEY=your-api-key-here
   ```
   Note: Both GEMINI_API_KEY and GOOGLE_API_KEY should have the same value

### Setting up Langfuse API Keys

1. Visit [Langfuse Cloud](https://cloud.langfuse.com/)

2. Sign up or log in to your Langfuse account

3. Navigate to your project settings or create a new project

4. In the project settings, find the "API Keys" section

5. Generate new API keys:
   - Click "Create API Key"
   - You'll receive both a public key and a secret key
   - Copy both keys

6. Add these keys to your `.env` file:
   ```
   LANGFUSE_PUBLIC_KEY=your-public-key-here
   LANGFUSE_SECRET_KEY=your-secret-key-here
   ```

### API Key Security

- Never commit your `.env` file to version control
- Keep your API key confidential
- If you suspect your key has been compromised, regenerate it immediately from Google AI Studio

## Repository Structure

This repository follows the same structure as the original Hugging Face AI Agent Course, with modifications to use Gemini API instead of Hugging Face's models. Each unit contains exercises that have been adapted to work with Gemini while maintaining the same learning objectives.

## Prerequisites

- Python 3.7 or higher
- Basic understanding of Python
- Google account for API access

## Getting Help

If you encounter any issues:
- Check Google AI Studio documentation
- Ensure your API keys are correctly set up
- Verify your environment variables are properly configured

Happy Learning! 🚀
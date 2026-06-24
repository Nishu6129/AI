from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(
    api_key="AIzaSyDoOJYcfyWXa1VYMrpvbN1F34TmgdENlJ8"
)

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)



# curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent" \
#   -H 'Content-Type: application/json' \
#   -H 'X-goog-api-key: AIzaSyDoOJYcfyWXa1VYMrpvbN1F34TmgdENlJ8' \
#   -X POST \
#   -d '{
#     "contents": [
#       {
#         "parts": [
#           {
#             "text": "Explain how AI works in a few words"
#           }
#         ]
#       }
#     ]
#   }'
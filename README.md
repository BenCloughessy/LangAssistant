# LangAssistant
Have you ever read a book in a foreign language? It's a great way to grow language skills, but it can be frustrating as it often results in frequent googling to understand words and expressions.

However, Google has no context and can't help us understand contextual expressions, character behaviours, or other specific information. Only someone with knowledge of the book can do that.

LangAssitant is a simple idea. More of a toy/proof of concept than a real project. But it moves towards solving this problem. 

The book is loaded into Vectara, a GenAI conversational search platform that handles it's own embeddings and has it's own internal vector store, simplifying the process of prepping a document for LLM access.

As a bonus, it handles 11 major world languages well, making it ideal for our multi-lingual project.

The user then types a query, which first is passed to Vectara to pull relevant context from the vector store. That context is passed to ChatGPT, which synthesises a response for us.

# Use Cases
Assistance with grammar, contextual questions such as phrases, locations, characters, or remembering details.

# Real-World Implementation
Messaging - Set up a whatsapp chatbot with access to your current book. Just text your questions.
Ebook - Click on a word, character, or phrase to see an explanation. Little prep required for the distributor.

# Limitations 
Hallucination - This is minimized by setting temperature to 0 when calling the api. However, in a production environment we would need to test and find ways to minimize hallucination

Poor Translations - The quality of explanations and translations is higher than ChatGPT because of access to context. However, it is by no means a substitute for a trained translator in regards to quality and accuracy.
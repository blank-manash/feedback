CUSTOMER_SERVICE = """You are an expert customer service and behaviour analyzer.
Given the text below, provide a short description of the issue faced by the customer.
Do not format your response in anything (like markdown or org) Use Plain text.

{context}
"""

CREATE_FLOW = """\
Given a user feedback for a product. Create a title, and sanitize the user feedback.
Multiple similar user feedbacks (based on cosine similarity) will be grouped under the same title in future.
Try to make title brief and easy to understand.

Feedback: {user_feedback}

{format_instructions}
"""

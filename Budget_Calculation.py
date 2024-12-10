# import os
# from openai import OpenAI

# # Create an OpenAI client instance
# client = OpenAI(api_key=os.getenv("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"))

# # openai.api_key = os.getenv("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")

# def budget_calculating(income, fixed_costs):
#     prompt = f"""
#     Given the monthly income of {income} and fixed costs of {fixed_costs}, calculate a personalized budget plan.
#     Please generate reasonable percentages for the following categories:
#     - Savings
#     - Investment
#     - Eating Out
#     - Guilt-free Spending
#     The total of all categories (including fixed costs) should sum up to 100% of the income.
#     Provide the percentage breakdown for each category, along with the actual dollar amount allocated to each.
#     """

#     response = openai.ChatCompletion.create(
#         engine="gpt-3.5-turbo",
#         prompt=prompt,
#         max_tokens=100,
#         )
    
#     return response.choices[0].text.strip()

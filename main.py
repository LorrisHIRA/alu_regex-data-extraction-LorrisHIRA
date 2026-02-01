import re
# Data extraction using reglex 

# this main file  script does:
#  get  emails, URLs, phone numbers, and credit card numbers
#   from messy raw text (like logs or API responses).
# and if an invalid input is used it will ignore them.
# 

#  REGEX PATTERNS
# 

# Emails: basic validation for normal addresses
# so it will  allow letters, numbers, dots, hyphens before @,
# and a valid domain with at least 2 letters .
# This will ignore obvious mistakes like "user@com"
email_pattern = re.compile(
    r'\b[a-zA-Z0-9._%+-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b'
)
# 2.URLS
# URLs: It will only accept http or https and ignore anything which is invalid 
# Which has spaces or <> symbols
url_pattern = re.compile(
    r'\bhttps?:\/\/[^\s<>"]+\b'
)

# so on the phone numbers i used the numbers from US formats
# examples : (123) 456-7890, 123-456-7890, 123.456.7890
# Rejects letters or too-short/long numbers

phone_pattern = re.compile(
      r'\(\d{3}\)\s\d{3}-\d{4}'
)


# so on  Credit cards i used a decision where it shouldd have 16 digits only, spaces or even dashes 
# and it will ignore obviously invalid stuff like letters in the number
credit_card_pattern = re.compile(
    r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
)



# Now we are going to extract data from the input text 

try:
    with open("sample_input.txt", "r", encoding="utf-8") as file:
        raw_text = file.read()
except FileNotFoundError:
    print("Oops! input.txt is missing.")
    exit()



#  Now we are going to extract data and using reglex

# Pull out matches using our patterns
emails_found = set(email_pattern.findall(raw_text))
urls_found = set(url_pattern.findall(raw_text))
phones_found = set(phone_pattern.findall(raw_text))
cards_found = set(credit_card_pattern.findall(raw_text))


# Protection of user data this means on the output instead of showing 
#everthing it will show only few inputs ex on credit cards it will only show 
# 4 last digits while on emails it can be only 1 letter 


def mask_email(email: str) -> str:
    """
    Hide most of the email address so it’s safe to display.
    Example: john.doe@example.com -> j***@example.com
    """
    try:
        name, domain = email.split("@")
        return name[0] + "***@" + domain
    except ValueError:
        # If something invalid happens, just return original
        return email

def mask_credit_card(card: str) -> str:
    
    #it will only show  credit card number except the last 4 digits.
    #Example: 4111 1111 1111 1111 -> **** **** **** 1111
    
    digits = re.sub(r'\D', '', card)  # remove anything that's not a number
    if len(digits) == 16:
        return "**** **** **** " + digits[-4:]
    return card  # return original if somehow invalid


safe_emails = [mask_email(e) for e in emails_found]
safe_cards = [mask_credit_card(c) for c in cards_found]



# STRUCTURED OUTPUT
# ON the output's structure i used symbols like = or * to make it look structured


output_lines = []

#  USER Emails
output_lines.append("***** Extracted User Emails *****")
if safe_emails:
    for e in sorted(safe_emails):
        output_lines.append(f"- {e}")
else:
    output_lines.append("No valid emails found.")

# URLs
output_lines.append("\n===== Extracted URLs =====")
if urls_found:
    for u in sorted(urls_found):
        output_lines.append(f"- {u}")
else:
    output_lines.append("No valid URLs found.")

# Phone numbers
output_lines.append("\n***** Extracted Phone Numbers *****")
if phones_found:
    for p in sorted(phones_found):
        output_lines.append(f"- {p}")
else:
    output_lines.append("No valid phone numbers found.")

#  with this code it will get the Credit cards for the users and if failed it will give the output saying invalid credit card
output_lines.append("\n===== Extracted Credit Cards =====")
if safe_cards:
    for c in sorted(safe_cards):
        output_lines.append(f"- {c}")
else:
    output_lines.append("No valid credit cards found.")


# and with this code it will save the  output to file which is named output .txt
with open("sample_output.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(output_lines))

print(" Done! Check 'sample_output.txt' for results.")

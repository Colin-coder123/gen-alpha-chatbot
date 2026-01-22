import re

# Memory
current_problem = None
current_answer = None
user_name = None

# Explain math like real life
def explain_problem(expr):
    steps = []
    step = 1

    # Detect simple multiplication like 5*5
    mult_match = re.match(r"^\s*(\d+)\s*\*\s*(\d+)\s*$", expr)
    if mult_match:
        a = int(mult_match.group(1))
        b = int(mult_match.group(2))

        steps.append(f"Step {step}: Think of {a} × {b} like real life 👀")
        step += 1
        steps.append(f"Step {step}: You have {b} groups of {a} (like {b} hands with {a} fingers each ✋)")
        step += 1
        steps.append(f"Step {step}: That means you add {a}, {b} times ➜ " + " + ".join([str(a)] * b))

        return "\n".join(steps)

    # Fallback explanation
    if "(" in expr:
        steps.append("Step 1: Do the brackets first")
    if "*" in expr or "/" in expr:
        steps.append("Step 2: Handle multiplication or division")
    if "+" in expr or "-" in expr:
        steps.append("Step 3: Handle addition or subtraction")

    return "\n".join(steps)

# Detect user intent
def detect_intent(text):
    text = text.lower()
    if text in ["hi", "hello", "yo", "hey"]:
        return "greeting"
    if "help" in text:
        return "help"
    if "explain" in text or "again" in text:
        return "explain_again"
    if "name is" in text:
        return "set_name"
    if re.match(r"^[0-9+\-*/(). ]+$", text):
        return "math"
    return "unknown"

# Start chat
print("🤖 Gen Alpha Math Bot (REAL-LIFE EXPLANATIONS)")
print("I explain math like a human, not a calculator")
print("Type 'quit' to exit\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "quit":
        print("Bot: aight I’m out ✌️")
        break

    intent = detect_intent(user_input)

    # Greetings
    if intent == "greeting":
        name_msg = f" {user_name}" if user_name else ""
        print(f"Bot: yo{name_msg} 😎 what math we cookin today?")
        continue

    # Help
    if intent == "help":
        print("Bot: drop a math problem and I’ll explain it IRL style 🧠")
        continue

    # Explain again
    if intent == "explain_again":
        if current_problem:
            print("Bot:")
            print(explain_problem(current_problem))
        else:
            print("Bot: explain WHAT bro 😭 give me math first")
        continue

    # Set user name
    if intent == "set_name":
        parts = user_input.split("name is")
        user_name = parts[1].strip().capitalize()
        print(f"Bot: aight {user_name} 😎 I’ll remember you!")
        continue

    # If waiting for answer
    if current_problem is not None:
        try:
            if float(user_input) == current_answer:
                print("Bot: ✅ W answer fr fr 🧠🔥")
            else:
                print("Bot: ❌ nah bro 💀 think about the groups again")
            current_problem = None
            current_answer = None
        except:
            print("Bot: drop a NUMBER bro 💀")
        continue

    # Math input
    if intent == "math":
        try:
            expr = user_input.replace("^", "**")
            current_answer = eval(expr)
            current_problem = user_input
            print("Bot:")
            print(explain_problem(user_input))
            print("\n🧠 Your turn: finish the math and drop the answer 👇 (no cap)")
        except:
            print("Bot: this math ain’t mathing 💀")
        continue

    # Unknown
    print("Bot: Collin is to lazy to make you even samrter so just put the equation 5*6 or something")

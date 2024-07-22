def password_Strength_checker(password):
    #criteria Weights
    length_weight = 2
    complexity_weight = 1
    
    #scroing variables
    score = 0
    
    # length check
    if len(password) >= 8:
        score += length_weight
        
    #complexity check
    complexity = any(char.isupper() for char in password) and \
                 any(char.islower() for char in password) and \
                 any(char.isdigit() for char in password) and \
                 any(not char.isalnum() for char in password)
    
    if complexity:
        score += complexity_weight
        
    return score

def password_Strength_feedback(score):
    if score >= 3:
        return "Strong Password! Excellent job!"
    elif score == 2:
        return "Good Password! Keep it up!"
    else:
        return "Weak Password. Please choose a stronger Password."
    
def main():
    password = input("Enter your Password: ")
    strength_score = password_Strength_checker(password)
    feedback = password_Strength_feedback(strength_score)
    print("Password strength score:",strength_score)
    print("Feedback:",feedback)
    
if __name__ == "__main__":
    main()

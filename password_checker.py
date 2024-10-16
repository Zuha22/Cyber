import password_strength

def password_checker(password):
  """Assesses the strength of a password based on given criteria."""
  # Create a PasswordStats object using the password to assess
  stats = password_strength.PasswordStats(password)
  # Get the strength score (0-1) and convert it to an integer (1-4) for simplicity
  strength = int(stats.strength() * 4) + 1
  # Map the numeric strength to a descriptive feedback
  if strength >= 4:
    feedback = "Strong"
  elif strength >= 2:
    feedback = "Medium"
  else:
    feedback = "Weak"
  return feedback

password = input("Enter your password: ")
strength = password_checker(password)
print(f"Password strength: {strength}")

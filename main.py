import hashlib
import color

choice = input("Are you\n(1) Signing Up\n(2) Signing In?\n ")

password = input("Password: ")

# creates SHA256 hash of password and adds salt (random unique string at the end of password) to ensure encryption rulsults in different has value when 2 passwords are the same

# pbkdf2_hmac returns bytes
password = hashlib.pbkdf2_hmac(
    'sha256',
    password.encode('utf-8'), b'salt', 100000)

# convert bytes to a string of hex
password = password.hex()

if choice == "1":
  with open("save.dat", "w") as results:
    results.write(f"{password}")
    print(color.BLUE + "Sign Up Complete!")
elif choice == "2":
  try:
    with open("save.dat", "r") as file:
      for line in file:
        line = line.replace("\n", " ")
        print()
        if password == line:
          print(color.GREEN + "Correct Password!")
        else:
          print(color.RED + "Incorrect Password!")
  except FileNotFoundError:
    print(color.RED + "No Account Found!")
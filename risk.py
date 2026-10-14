def check_risk(amount):
    if amount > 500:
        return "High Risk"
    elif amount > 100:
        return "Medium Risk"
    else:
        return "Low Risk"

print(check_risk(850))
print(check_risk(200))
print(check_risk(50))

assert check_risk(850) == "High Risk"
assert check_risk(200) == "Medium Risk"
assert check_risk(50) == "Low Risk"
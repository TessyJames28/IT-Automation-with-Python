# def count_users(group):
#     count = 0
#     for member in get_members(group):
#         count += 1
#         if is_group(member):
#             count += count_users(member)  # Recursively counts members of nested groups
#     return count


def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    print(index)
    # new_email = email[:index] + "@" + new_domain
    new_email = email[index+1:]
    return new_email
  return email


print(replace_domain("tessy@gmail.com", "gmail.com", "littlelemon.com"))
def subject_by_datatypes(arg1):
  if type(arg1) == str:
    return "Literature"
  elif type(arg1) == int or type(arg1) == float:
    return "Math"
  elif type(arg1) == bool:
    return "Science"
  else:
    return "Unknown"
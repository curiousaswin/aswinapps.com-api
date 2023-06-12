def get_data():
  """Returns the data in XML format."""
  data = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "phone": "123-456-7890"
  }
  return xml.etree.ElementTree.tostring(data, encoding="utf-8")
